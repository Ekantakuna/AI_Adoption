#!/usr/bin/env python3
"""Validate explicit knowledge relationships and traverse derived impact links."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml


REVIEWED_DEFAULT = {"verified", "approved"}
REVIEWER_REQUIRED = {"verified", "approved"}


@dataclass(frozen=True)
class Record:
    path: Path
    data: dict[str, Any]

    @property
    def id(self) -> str:
        return str(self.data.get("id", ""))

    @property
    def type(self) -> str:
        return str(self.data.get("type", ""))

    @property
    def status(self) -> str:
        return str(self.data.get("review_status", ""))


@dataclass(frozen=True)
class Edge:
    edge_id: str
    source: str
    target: str
    kind: str
    relationship_id: str | None = None


@dataclass
class ValidationResult:
    records: dict[str, Record] = field(default_factory=dict)
    relationships: list[Record] = field(default_factory=list)
    relationship_types: dict[str, dict[str, Any]] = field(default_factory=dict)
    reviewed_statuses: set[str] = field(default_factory=lambda: set(REVIEWED_DEFAULT))
    audit_statuses: set[str] = field(default_factory=set)
    default_depth: int = 1
    hard_depth: int = 25
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass
class TraversalResult:
    start_id: str
    direction: str
    max_depth: int
    nodes: list[dict[str, Any]] = field(default_factory=list)
    edges: list[dict[str, Any]] = field(default_factory=list)
    alternate_paths: list[dict[str, Any]] = field(default_factory=list)
    cycles: list[dict[str, Any]] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    truncated: bool = False


def _load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        return None


def _front_matter(path: Path, errors: list[str]) -> Any:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read Markdown: {exc}")
        return None
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path}: Markdown production record requires YAML front matter")
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path}: unterminated YAML front matter")
        return None
    try:
        return yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: cannot parse YAML front matter: {exc}")
        return None


def _is_template(path: Path, data: Any) -> bool:
    return path.stem.lower().endswith("-template") or (
        isinstance(data, dict) and data.get("template") is True
    )


def _string_set(value: Any, label: str, errors: list[str]) -> set[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"{label} must be a list of strings")
        return set()
    return set(value)


def _load_contract(root: Path, result: ValidationResult) -> None:
    path = root / "config/relationship-types.yaml"
    data = _load_yaml(path, result.errors)
    if not isinstance(data, dict):
        result.errors.append(f"{path}: expected a mapping")
        return
    traversal = data.get("traversal")
    if not isinstance(traversal, dict):
        result.errors.append(f"{path}: traversal must be a mapping")
        traversal = {}
    for field_name, fallback in (("default_max_depth", 1), ("hard_max_depth", 25)):
        value = traversal.get(field_name, fallback)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            result.errors.append(f"{path}: {field_name} must be a non-negative integer")
            value = fallback
        if field_name == "default_max_depth":
            result.default_depth = value
        else:
            result.hard_depth = value
    if result.default_depth > result.hard_depth:
        result.errors.append(f"{path}: default_max_depth exceeds hard_max_depth")
    result.reviewed_statuses = _string_set(
        traversal.get("reviewed_statuses", sorted(REVIEWED_DEFAULT)),
        f"{path}: reviewed_statuses",
        result.errors,
    )
    result.audit_statuses = _string_set(
        traversal.get("audit_statuses", []),
        f"{path}: audit_statuses",
        result.errors,
    )
    definitions = data.get("relationship_types")
    if not isinstance(definitions, list):
        result.errors.append(f"{path}: relationship_types must be a list")
        return
    for item in definitions:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            result.errors.append(f"{path}: every relationship type must have a string id")
            continue
        relationship_id = item["id"]
        if relationship_id in result.relationship_types:
            result.errors.append(f"{path}: duplicate relationship type {relationship_id}")
            continue
        if item.get("direction") not in {"directed", "symmetric"}:
            result.errors.append(f"{path}: {relationship_id} has invalid direction")
        if item.get("impact_direction") not in {"from_to", "to_from", "both"}:
            result.errors.append(f"{path}: {relationship_id} has invalid impact_direction")
        if item.get("cycle_policy") not in {"acyclic_any", "acyclic_homogeneous", "conceptual"}:
            result.errors.append(f"{path}: {relationship_id} has invalid cycle_policy")
        for field_name in ("allowed_from_types", "allowed_to_types"):
            _string_set(item.get(field_name), f"{path}: {relationship_id}.{field_name}", result.errors)
        result.relationship_types[relationship_id] = item
    schema_path = root / "schemas/relationship.schema.yaml"
    if schema_path.exists():
        schema = _load_yaml(schema_path, result.errors)
        properties = schema.get("properties") if isinstance(schema, dict) else None
        relationship_property = properties.get("relationship_type") if isinstance(properties, dict) else None
        schema_values = relationship_property.get("enum") if isinstance(relationship_property, dict) else None
        if not isinstance(schema_values, list) or not all(isinstance(value, str) for value in schema_values):
            result.errors.append(f"{schema_path}: relationship_type must define a string enum")
        elif set(schema_values) != set(result.relationship_types):
            result.errors.append(f"{schema_path}: relationship types do not match {path}")


def _load_statuses(root: Path, result: ValidationResult) -> set[str]:
    path = root / "config/review-statuses.yaml"
    data = _load_yaml(path, result.errors)
    entries = data.get("review_statuses") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        result.errors.append(f"{path}: review_statuses must be a list")
        return set()
    statuses: set[str] = set()
    for entry in entries:
        value = entry.get("id") if isinstance(entry, dict) else entry
        if isinstance(value, str):
            statuses.add(value)
        else:
            result.errors.append(f"{path}: review status IDs must be strings")
    return statuses


def _load_records(root: Path, result: ValidationResult) -> list[Record]:
    type_path = root / "config/knowledge-types.yaml"
    type_data = _load_yaml(type_path, result.errors)
    definitions = type_data.get("object_types") if isinstance(type_data, dict) else None
    if not isinstance(definitions, list):
        result.errors.append(f"{type_path}: object_types must be a list")
        return []
    loaded: list[Record] = []
    for definition in definitions:
        if not isinstance(definition, dict):
            result.errors.append(f"{type_path}: invalid object type definition")
            continue
        directory = definition.get("directory")
        expected_type = definition.get("type")
        if not isinstance(directory, str) or not isinstance(expected_type, str):
            result.errors.append(f"{type_path}: object type requires string directory and type")
            continue
        object_root = root / directory
        if not object_root.exists():
            continue
        for path in sorted(object_root.iterdir()):
            if not path.is_file() or path.name.lower() == "readme.md" or path.suffix.lower() not in {".yaml", ".yml", ".md"}:
                continue
            data = _front_matter(path, result.errors) if path.suffix.lower() == ".md" else _load_yaml(path, result.errors)
            if _is_template(path, data):
                continue
            if not isinstance(data, dict):
                result.errors.append(f"{path}: production record must be a mapping")
                continue
            if data.get("type") != expected_type:
                result.errors.append(f"{path}: type {data.get('type')!r} does not match configured type {expected_type!r}")
            loaded.append(Record(path, data))
    return loaded


def _type_allowed(actual: str, allowed: Any) -> bool:
    return isinstance(allowed, list) and ("any_knowledge" in allowed or actual in allowed)


def _strong_components(nodes: Iterable[str], adjacency: dict[str, list[tuple[str, str]]]) -> list[set[str]]:
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indexes: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    components: list[set[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indexes[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for target, _ in adjacency.get(node, []):
            if target not in indexes:
                visit(target)
                lowlinks[node] = min(lowlinks[node], lowlinks[target])
            elif target in on_stack:
                lowlinks[node] = min(lowlinks[node], indexes[target])
        if lowlinks[node] == indexes[node]:
            component: set[str] = set()
            while stack:
                member = stack.pop()
                on_stack.remove(member)
                component.add(member)
                if member == node:
                    break
            components.append(component)

    for node in sorted(set(nodes)):
        if node not in indexes:
            visit(node)
    return components


def validate_repository(root: Path | str) -> ValidationResult:
    root = Path(root).resolve()
    result = ValidationResult()
    _load_contract(root, result)
    statuses = _load_statuses(root, result)
    loaded = _load_records(root, result)

    for record in loaded:
        if not record.id:
            result.errors.append(f"{record.path}: missing string id")
            continue
        if record.id in result.records:
            result.errors.append(f"{record.path}: duplicate ID {record.id}; first used by {result.records[record.id].path}")
            continue
        result.records[record.id] = record
        if record.type == "relationship":
            result.relationships.append(record)

    evidence_ids = {record.id for record in result.records.values() if record.type == "evidence_statement"}
    endpoint_ids = {
        record.id for record in result.records.values()
        if record.type not in {"evidence_statement", "relationship"}
    }
    for record in result.records.values():
        if record.status not in statuses:
            result.errors.append(f"{record.path}: invalid review status {record.status!r}")
        reviewer = record.data.get("reviewer")
        if record.status in REVIEWER_REQUIRED and (
            not isinstance(reviewer, dict)
            or not isinstance(reviewer.get("name"), str)
            or not reviewer.get("name", "").strip()
            or not reviewer.get("reviewed_at")
        ):
            result.errors.append(f"{record.path}: status {record.status!r} requires reviewer metadata")
        references = record.data.get("evidence_ids", [])
        if "evidence_ids" in record.data and not isinstance(references, list):
            result.errors.append(f"{record.path}: evidence_ids must be a list")
        elif isinstance(references, list):
            for evidence_id in references:
                if not isinstance(evidence_id, str) or evidence_id not in evidence_ids:
                    result.errors.append(f"{record.path}: unknown evidence ID {evidence_id!r}")

    semantic_keys: dict[tuple[str, str, str], str] = {}
    adjacency: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for relationship in result.relationships:
        data = relationship.data
        kind = data.get("relationship_type")
        definition = result.relationship_types.get(kind) if isinstance(kind, str) else None
        if definition is None:
            result.errors.append(f"{relationship.path}: unknown relationship type {kind!r}")
            continue
        source = data.get("from_id")
        target = data.get("to_id")
        source_record = result.records.get(source) if isinstance(source, str) else None
        target_record = result.records.get(target) if isinstance(target, str) else None
        if source not in endpoint_ids:
            result.errors.append(f"{relationship.path}: dangling or prohibited source endpoint {source!r}")
        if target not in endpoint_ids:
            result.errors.append(f"{relationship.path}: dangling or prohibited target endpoint {target!r}")
        if isinstance(source, str) and source == target:
            result.errors.append(f"{relationship.path}: self-relation is prohibited")
        evidence_refs = data.get("evidence_ids")
        if not isinstance(evidence_refs, list) or not evidence_refs:
            result.errors.append(f"{relationship.path}: relationship requires evidence_ids")
        if source_record and not _type_allowed(source_record.type, definition.get("allowed_from_types")):
            result.errors.append(f"{relationship.path}: source type {source_record.type!r} is prohibited for {kind}")
        if target_record and not _type_allowed(target_record.type, definition.get("allowed_to_types")):
            result.errors.append(f"{relationship.path}: target type {target_record.type!r} is prohibited for {kind}")
        if source_record and target_record and definition.get("same_endpoint_type_required") is True and source_record.type != target_record.type:
            result.errors.append(f"{relationship.path}: {kind} endpoints must have the same type")
        required_target_status = definition.get("target_status_required")
        if target_record and isinstance(required_target_status, str) and target_record.status != required_target_status:
            result.errors.append(f"{relationship.path}: {kind} target must be {required_target_status!r}")
        if relationship.status in result.reviewed_statuses:
            for endpoint_record, label in ((source_record, "source"), (target_record, "target")):
                if endpoint_record and endpoint_record.status == "rejected":
                    result.errors.append(f"{relationship.path}: active relationship has rejected {label} endpoint {endpoint_record.id}")
                elif endpoint_record and endpoint_record.status == "deprecated" and not (kind == "supersedes" and label == "target"):
                    result.warnings.append(f"{relationship.path}: active relationship has deprecated {label} endpoint {endpoint_record.id}")
                elif endpoint_record and endpoint_record.status not in result.reviewed_statuses and endpoint_record.status != "deprecated":
                    result.errors.append(
                        f"{relationship.path}: active relationship has non-reviewed {label} endpoint {endpoint_record.id}"
                    )
        if isinstance(source, str) and isinstance(target, str):
            key_endpoints = tuple(sorted((source, target))) if definition.get("direction") == "symmetric" else (source, target)
            key = (str(kind), key_endpoints[0], key_endpoints[1])
            if key in semantic_keys:
                result.warnings.append(f"{relationship.path}: semantic duplicate of {semantic_keys[key]}")
            else:
                semantic_keys[key] = relationship.id
            adjacency[source].append((target, str(kind)))
            if definition.get("direction") == "symmetric":
                adjacency[target].append((source, str(kind)))

    components = _strong_components(endpoint_ids, adjacency)
    reported_cycles: set[tuple[str, ...]] = set()
    for component in components:
        if len(component) < 2:
            continue
        internal_types = {
            kind for source in component for target, kind in adjacency.get(source, [])
            if target in component
        }
        cycle_key = tuple(sorted(component))
        if cycle_key in reported_cycles:
            continue
        reported_cycles.add(cycle_key)
        cycle_policies = {
            result.relationship_types[kind].get("cycle_policy")
            for kind in internal_types if kind in result.relationship_types
        }
        structurally_invalid = (
            "acyclic_any" in cycle_policies
            or (len(internal_types) == 1 and "acyclic_homogeneous" in cycle_policies)
        )
        if structurally_invalid:
            result.errors.append(f"structurally invalid relationship cycle: {', '.join(cycle_key)}")
        else:
            result.warnings.append(f"permitted conceptual cycle: {', '.join(cycle_key)}")
    return result


def _eligible(record: Record, validation: ValidationResult, include_unreviewed: bool, is_relationship: bool = False) -> bool:
    if include_unreviewed:
        return record.status in validation.audit_statuses
    if is_relationship and record.status == "deprecated":
        return False
    return record.status in validation.reviewed_statuses or record.status == "deprecated"


def _projection(validation: ValidationResult, mode: str, include_unreviewed: bool) -> dict[str, list[Edge]]:
    outgoing: dict[str, list[Edge]] = defaultdict(list)

    def add(edge: Edge) -> None:
        outgoing[edge.source].append(edge)

    for record in validation.records.values():
        if record.type in {"evidence_statement", "relationship"} or not _eligible(record, validation, include_unreviewed):
            continue
        references = record.data.get("evidence_ids", [])
        if not isinstance(references, list):
            continue
        for evidence_id in references:
            if evidence_id not in validation.records:
                continue
            down = Edge(f"EVIDENCE:{evidence_id}:{record.id}", evidence_id, record.id, "evidence_reference")
            if mode in {"downstream", "impact", "both"}:
                add(down)
            if mode in {"upstream", "both"}:
                add(Edge(down.edge_id, record.id, evidence_id, down.kind))

    for relationship in validation.relationships:
        if not _eligible(relationship, validation, include_unreviewed, is_relationship=True):
            continue
        source = relationship.data.get("from_id")
        target = relationship.data.get("to_id")
        kind = relationship.data.get("relationship_type")
        if not all(isinstance(value, str) for value in (source, target, kind)):
            continue
        definition = validation.relationship_types.get(kind)
        if not definition:
            continue

        evidence_references = relationship.data.get("evidence_ids", [])
        if isinstance(evidence_references, list):
            for evidence_id in evidence_references:
                if evidence_id not in validation.records:
                    continue
                if mode in {"downstream", "impact", "both"}:
                    for endpoint in (source, target):
                        add(Edge(
                            f"EVIDENCE:{evidence_id}:{relationship.id}",
                            evidence_id,
                            endpoint,
                            "relationship_evidence",
                            relationship.id,
                        ))
                if mode in {"upstream", "both"}:
                    for endpoint in (source, target):
                        add(Edge(
                            f"EVIDENCE:{evidence_id}:{relationship.id}",
                            endpoint,
                            evidence_id,
                            "relationship_evidence",
                            relationship.id,
                        ))

        def relationship_edge(left: str, right: str) -> Edge:
            return Edge(relationship.id, left, right, kind, relationship.id)

        pairs: set[tuple[str, str]] = set()
        if mode == "impact":
            impact = definition.get("impact_direction")
            if impact in {"from_to", "both"}:
                pairs.add((source, target))
            if impact in {"to_from", "both"}:
                pairs.add((target, source))
        elif mode == "downstream":
            pairs.add((source, target))
            if definition.get("direction") == "symmetric":
                pairs.add((target, source))
        elif mode == "upstream":
            pairs.add((target, source))
            if definition.get("direction") == "symmetric":
                pairs.add((source, target))
        else:
            pairs.update({(source, target), (target, source)})
        for left, right in pairs:
            add(relationship_edge(left, right))

    for node in outgoing:
        outgoing[node].sort(key=lambda edge: (edge.target, edge.kind, edge.edge_id))
    return outgoing


def traverse(
    validation: ValidationResult,
    start_id: str,
    direction: str = "impact",
    max_depth: int | None = None,
    include_unreviewed: bool = False,
) -> TraversalResult:
    depth_limit = validation.default_depth if max_depth is None else max_depth
    if depth_limit < 0 or depth_limit > validation.hard_depth:
        raise ValueError(f"max depth must be between 0 and {validation.hard_depth}")
    if start_id not in validation.records:
        raise ValueError(f"unknown start ID {start_id!r}")
    start = validation.records[start_id]
    if start.type == "relationship":
        raise ValueError(f"relationship ID {start_id!r} is an edge record, not a traversal node")
    if not _eligible(start, validation, include_unreviewed):
        raise ValueError(f"start ID {start_id!r} is not eligible for this traversal view")

    projection = _projection(validation, direction, include_unreviewed)
    output = TraversalResult(start_id, direction, depth_limit)
    discovered: dict[str, int] = {start_id: 0}
    queue: deque[tuple[str, int, tuple[str, ...]]] = deque([(start_id, 0, (start_id,))])
    emitted_edges: set[tuple[str, str, str]] = set()
    while queue:
        node, depth, path = queue.popleft()
        record = validation.records[node]
        output.nodes.append({
            "id": node,
            "type": record.type,
            "review_status": record.status,
            "classification": record.data.get("classification"),
            "depth": depth,
        })
        next_edges = projection.get(node, [])
        if depth >= depth_limit:
            if next_edges:
                output.truncated = True
            continue
        for edge in next_edges:
            target_record = validation.records.get(edge.target)
            if target_record is None:
                output.warnings.append(f"unresolved impact edge {edge.edge_id} to {edge.target}")
                continue
            if not _eligible(target_record, validation, include_unreviewed):
                continue
            edge_key = (edge.edge_id, edge.source, edge.target)
            if edge_key not in emitted_edges:
                output.edges.append({
                    "id": edge.edge_id,
                    "from_id": edge.source,
                    "to_id": edge.target,
                    "type": edge.kind,
                    "relationship_id": edge.relationship_id,
                })
                emitted_edges.add(edge_key)
            if edge.kind == "contradicts" and edge.edge_id not in output.conflicts:
                output.conflicts.append(edge.edge_id)
            if edge.target in path:
                output.cycles.append({"edge_id": edge.edge_id, "path": [*path, edge.target]})
                continue
            next_depth = depth + 1
            if edge.target in discovered:
                output.alternate_paths.append({
                    "to_id": edge.target,
                    "depth": next_depth,
                    "via_edge": edge.edge_id,
                })
                continue
            discovered[edge.target] = next_depth
            queue.append((edge.target, next_depth, (*path, edge.target)))
    output.nodes.sort(key=lambda item: (item["depth"], item["id"]))
    output.conflicts.sort()
    if output.truncated:
        output.warnings.append(f"traversal reached max depth {depth_limit}; impact beyond this boundary is unknown")
    for record in validation.records.values():
        if record.id in discovered and record.status == "deprecated":
            output.warnings.append(f"deprecated object included for history: {record.id}")
    return output


def _print_validation(result: ValidationResult) -> None:
    print("Relationship impact validation passed." if result.ok else "Relationship impact validation failed.")
    print(f"Canonical records: {len(result.records)}")
    print(f"Relationship records: {len(result.relationships)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    for error in result.errors:
        print(f"ERROR: {error}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")


def _traversal_payload(result: TraversalResult) -> dict[str, Any]:
    return {
        "start_id": result.start_id,
        "direction": result.direction,
        "max_depth": result.max_depth,
        "truncated": result.truncated,
        "nodes": result.nodes,
        "edges": result.edges,
        "alternate_paths": result.alternate_paths,
        "cycles": result.cycles,
        "conflicts": result.conflicts,
        "warnings": result.warnings,
    }


def _print_traversal(result: TraversalResult) -> None:
    print(f"Traversal start: {result.start_id}")
    print(f"Direction: {result.direction}")
    print(f"Maximum depth: {result.max_depth}")
    for node in result.nodes:
        print(f"NODE depth={node['depth']} id={node['id']} type={node['type']} status={node['review_status']}")
    for edge in result.edges:
        print(f"EDGE {edge['from_id']} -[{edge['type']}:{edge['id']}]-> {edge['to_id']}")
    for alternate in result.alternate_paths:
        print(
            f"ALTERNATE to={alternate['to_id']} depth={alternate['depth']} "
            f"via={alternate['via_edge']}"
        )
    for cycle in result.cycles:
        print(f"CYCLE edge={cycle['edge_id']} path={' -> '.join(cycle['path'])}")
    for relationship_id in result.conflicts:
        print(f"CONFLICT relationship={relationship_id} status=unresolved")
    for warning in result.warnings:
        print(f"WARNING: {warning}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--start-id")
    parser.add_argument("--direction", choices=("upstream", "downstream", "both", "impact"), default="impact")
    parser.add_argument("--max-depth", type=int)
    parser.add_argument("--include-unreviewed", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    validation = validate_repository(args.root)
    if args.format == "text":
        _print_validation(validation)
    if not validation.ok:
        if args.format == "json":
            print(json.dumps({"errors": validation.errors, "warnings": validation.warnings}, indent=2, sort_keys=True))
        return 1
    if not args.start_id:
        if args.format == "json":
            print(json.dumps({
                "records": len(validation.records),
                "relationships": len(validation.relationships),
                "errors": [],
                "warnings": validation.warnings,
            }, indent=2, sort_keys=True))
        return 0
    try:
        traversal = traverse(validation, args.start_id, args.direction, args.max_depth, args.include_unreviewed)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    payload = _traversal_payload(traversal)
    if args.format == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        _print_traversal(traversal)
    return 0


if __name__ == "__main__":
    sys.exit(main())
