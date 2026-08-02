#!/usr/bin/env python3
"""Validate controlled knowledge records and their repository references."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


ID_RE = re.compile(r"^[A-Z]+-[0-9]{6}$")
TEMPLATE_ID_RE = re.compile(r"^[A-Z]+-000000$")
MARKDOWN_FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", re.DOTALL)
REVIEWER_REQUIRED = {"verified", "approved"}
RUN_REVIEW_ELIGIBLE = {"verified", "approved"}


@dataclass
class ValidationResult:
    records: int = 0
    evidence_records: int = 0
    legacy_files: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass
class Record:
    path: Path
    data: dict[str, Any]


def _load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        return None


def _front_matter(path: Path, errors: list[str]) -> tuple[bool, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read Markdown: {exc}")
        return False, None
    match = MARKDOWN_FRONT_MATTER_RE.match(text)
    if not match:
        return False, None
    try:
        return True, yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: cannot parse YAML front matter: {exc}")
        return True, None


def _controlled_ids(data: Any, key: str, path: Path, errors: list[str]) -> set[str]:
    if not isinstance(data, dict) or not isinstance(data.get(key), list):
        errors.append(f"{path}: expected top-level '{key}' list")
        return set()
    values: set[str] = set()
    for entry in data[key]:
        value = entry.get("id") if isinstance(entry, dict) else entry
        if not isinstance(value, str):
            errors.append(f"{path}: every '{key}' entry must be a string or contain an id")
        else:
            values.add(value)
    return values


def _is_template(path: Path, data: Any) -> bool:
    return path.stem.lower().endswith("-template") or (
        isinstance(data, dict) and data.get("template") is True
    )


def _schema_required_fields(root: Path, type_definition: dict[str, Any], errors: list[str]) -> set[str]:
    schema_path = type_definition.get("schema")
    if schema_path is None:
        return {
            "id", "type", "evidence_ids", "classification", "review_status",
            "origin", "created_at", "created_by",
        }
    if not isinstance(schema_path, str):
        errors.append("knowledge type schema paths must be strings or null")
        return set()
    schema = _load_yaml(root / schema_path, errors)
    if not isinstance(schema, dict) or not isinstance(schema.get("required"), list):
        errors.append(f"{root / schema_path}: schema must define a top-level required list")
        return set()
    return {item for item in schema["required"] if isinstance(item, str)}


def validate_repository(root: Path | str) -> ValidationResult:
    root = Path(root).resolve()
    result = ValidationResult()

    catalogue_path = root / "sources/catalogue.yaml"
    catalogue = _load_yaml(catalogue_path, result.errors)
    if not isinstance(catalogue, dict) or not isinstance(catalogue.get("records"), list):
        result.errors.append(f"{catalogue_path}: expected top-level 'records' array")
        source_ids: set[str] = set()
    else:
        source_ids = {
            record.get("id")
            for record in catalogue["records"]
            if isinstance(record, dict) and isinstance(record.get("id"), str)
        }

    run_path = root / "sources/processing-runs.yaml"
    run_data = _load_yaml(run_path, result.errors)
    run_records = run_data.get("records") if isinstance(run_data, dict) else None
    if not isinstance(run_records, list):
        result.errors.append(f"{run_path}: expected top-level 'records' array")
        run_records = []
    eligible_run_ids = {
        run.get("id")
        for run in run_records
        if isinstance(run, dict)
        and isinstance(run.get("id"), str)
        and run.get("status") == "succeeded"
        and run.get("review_status") in RUN_REVIEW_ELIGIBLE
    }

    type_path = root / "config/knowledge-types.yaml"
    type_config = _load_yaml(type_path, result.errors)
    definitions = type_config.get("object_types") if isinstance(type_config, dict) else None
    if not isinstance(definitions, list):
        result.errors.append(f"{type_path}: expected top-level 'object_types' list")
        definitions = []

    type_definitions: dict[str, dict[str, Any]] = {}
    directory_types: dict[Path, str] = {}
    for definition in definitions:
        if not isinstance(definition, dict) or not isinstance(definition.get("type"), str):
            result.errors.append(f"{type_path}: invalid object type definition")
            continue
        object_type = definition["type"]
        type_definitions[object_type] = definition
        directory = definition.get("directory")
        if isinstance(directory, str):
            directory_types[(root / directory).resolve()] = object_type

    status_path = root / "config/review-statuses.yaml"
    status_config = _load_yaml(status_path, result.errors)
    statuses = _controlled_ids(status_config, "review_statuses", status_path, result.errors)
    reviewer_required_values = (
        status_config.get("reviewer_required_statuses")
        if isinstance(status_config, dict)
        else None
    )
    if reviewer_required_values is None:
        reviewer_required = REVIEWER_REQUIRED
    elif not isinstance(reviewer_required_values, list):
        result.errors.append(
            f"{status_path}: expected 'reviewer_required_statuses' list"
        )
        reviewer_required = REVIEWER_REQUIRED
    else:
        reviewer_required = {
            value for value in reviewer_required_values if isinstance(value, str)
        }
        if len(reviewer_required) != len(reviewer_required_values):
            result.errors.append(
                f"{status_path}: every 'reviewer_required_statuses' entry must be a string"
            )
    confidence_path = root / "config/evidence-confidence.yaml"
    confidences = _controlled_ids(_load_yaml(confidence_path, result.errors), "confidence_values", confidence_path, result.errors)

    required_by_type = {
        object_type: _schema_required_fields(root, definition, result.errors)
        for object_type, definition in type_definitions.items()
    }

    records: list[Record] = []
    knowledge_root = root / "knowledge"
    for path in sorted(knowledge_root.rglob("*")) if knowledge_root.exists() else []:
        if not path.is_file() or path.name.lower() == "readme.md" or path.suffix.lower() not in {".yaml", ".yml", ".md"}:
            continue
        if path.suffix.lower() == ".md":
            has_front_matter, data = _front_matter(path, result.errors)
            if not has_front_matter:
                if path.parent.resolve() == knowledge_root.resolve():
                    result.legacy_files += 1
                else:
                    result.errors.append(
                        f"{path}: Markdown production record requires YAML front matter"
                    )
                continue
        else:
            data = _load_yaml(path, result.errors)
        if _is_template(path, data):
            continue
        if not isinstance(data, dict):
            result.errors.append(f"{path}: structured record must be a YAML mapping")
            continue
        records.append(Record(path, data))

    result.records = len(records)
    result.evidence_records = sum(record.data.get("type") == "evidence_statement" for record in records)

    seen_ids: dict[str, Path] = {}
    evidence_ids: set[str] = set()
    endpoint_ids: set[str] = set()

    for record in records:
        data = record.data
        record_id = data.get("id")
        object_type = data.get("type")

        id_registered = False
        if not isinstance(record_id, str) or ID_RE.fullmatch(record_id) is None:
            result.errors.append(f"{record.path}: invalid identifier {record_id!r}")
        elif TEMPLATE_ID_RE.fullmatch(record_id):
            result.errors.append(f"{record.path}: placeholder ID cannot be used by a production record")
        elif record_id in seen_ids:
            result.errors.append(f"{record.path}: duplicate ID {record_id}; first used by {seen_ids[record_id]}")
        else:
            seen_ids[record_id] = record.path
            id_registered = True

        if not isinstance(object_type, str) or object_type not in type_definitions:
            result.errors.append(f"{record.path}: unsupported object type {object_type!r}")
            continue

        expected_type = None
        for directory, configured_type in directory_types.items():
            if record.path.resolve().is_relative_to(directory):
                expected_type = configured_type
                break
        if expected_type is None:
            result.errors.append(f"{record.path}: record is outside a configured knowledge-object directory")
        elif object_type != expected_type:
            result.errors.append(f"{record.path}: type '{object_type}' does not match directory type '{expected_type}'")

        missing = sorted(field for field in required_by_type.get(object_type, set()) if field not in data)
        if missing:
            result.errors.append(f"{record.path}: missing required fields: {', '.join(missing)}")

        prefix = type_definitions[object_type].get("prefix")
        expected_pattern = re.compile(rf"^{re.escape(str(prefix))}-[0-9]{{6}}$")
        if isinstance(record_id, str) and ID_RE.fullmatch(record_id) is not None and expected_pattern.fullmatch(record_id) is None:
            result.errors.append(f"{record.path}: invalid identifier {record_id!r} for type '{object_type}'")
        elif id_registered:
            if object_type == "evidence_statement":
                evidence_ids.add(record_id)
            elif object_type != "relationship":
                endpoint_ids.add(record_id)

        status = data.get("review_status")
        if not isinstance(status, str) or status not in statuses:
            result.errors.append(f"{record.path}: invalid review status {status!r}")
        reviewer = data.get("reviewer")
        if isinstance(status, str) and status in reviewer_required and (
            not isinstance(reviewer, dict)
            or not isinstance(reviewer.get("name"), str)
            or not reviewer.get("name", "").strip()
            or not reviewer.get("reviewed_at")
        ):
            result.errors.append(f"{record.path}: status '{status}' requires reviewer name and reviewed_at")

        if object_type == "evidence_statement":
            source_id = data.get("source_id")
            if not isinstance(source_id, str) or source_id not in source_ids:
                result.errors.append(f"{record.path}: unknown source ID {source_id!r}")
            processing_run_id = data.get("processing_run_id")
            if (
                not isinstance(processing_run_id, str)
                or processing_run_id not in eligible_run_ids
            ):
                result.errors.append(
                    f"{record.path}: processing run {processing_run_id!r} is not a reviewed successful run"
                )
            confidence = data.get("confidence")
            if not isinstance(confidence, str) or confidence not in confidences:
                result.errors.append(f"{record.path}: invalid evidence confidence {confidence!r}")

    for record in records:
        data = record.data
        object_type = data.get("type")
        if not isinstance(object_type, str) or object_type not in type_definitions:
            continue
        evidence_references = data.get("evidence_ids", [])
        evidence_required = type_definitions[object_type].get("evidence_required") is True
        if evidence_required and (not isinstance(evidence_references, list) or not evidence_references):
            result.errors.append(f"{record.path}: type '{object_type}' requires at least one evidence ID")
        if isinstance(evidence_references, list):
            for evidence_id in evidence_references:
                if not isinstance(evidence_id, str) or evidence_id not in evidence_ids:
                    result.errors.append(f"{record.path}: unknown evidence ID {evidence_id!r}")
        elif "evidence_ids" in data:
            result.errors.append(f"{record.path}: evidence_ids must be a list")

        if object_type == "relationship":
            for field_name in ("from_id", "to_id"):
                endpoint = data.get(field_name)
                if not isinstance(endpoint, str) or endpoint not in endpoint_ids:
                    result.errors.append(f"{record.path}: {field_name} references unknown knowledge-object ID {endpoint!r}")

    return result


def _print_result(result: ValidationResult) -> None:
    print("Knowledge validation passed." if result.ok else "Knowledge validation failed.")
    print(f"Production knowledge records: {result.records}")
    print(f"Evidence records: {result.evidence_records}")
    print(f"Legacy or provisional files: {result.legacy_files}")
    print(f"Errors: {len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root")
    args = parser.parse_args(argv)
    result = validate_repository(args.root)
    _print_result(result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
