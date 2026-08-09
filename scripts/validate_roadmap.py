#!/usr/bin/env python3
"""Validate the machine and human Stage 9.5 roadmap without modifying it."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


STAGE_ID_RE = re.compile(r"^stage-[0-9]+(?:\.[0-9]+)?$")
REQUIRED_STAGE_FIELDS = {
    "id", "sequence", "title", "status", "capability_status", "summary",
    "prerequisites", "entry_criteria", "deliverables", "validation",
    "exit_gates", "success_measures", "dependencies", "downstream_prompt",
}
CAPABILITY_STATUSES = {"implemented", "partial", "planned", "absent", "unknown"}
ROADMAP_STATUSES = {"draft", "in_review", "approved", "superseded", "retired"}


def _load(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        return None


def validate(root: Path | str) -> list[str]:
    root = Path(root).resolve()
    errors: list[str] = []
    machine_path = root / "project/roadmap.yaml"
    human_path = root / "project/roadmap/implementation-roadmap.md"
    data = _load(machine_path, errors)
    if not isinstance(data, dict):
        return errors or [f"{machine_path}: expected mapping"]
    if data.get("roadmap_id") != "ROADMAP-000001":
        errors.append(f"{machine_path}: roadmap_id must be ROADMAP-000001")
    if data.get("status") not in ROADMAP_STATUSES:
        errors.append(f"{machine_path}: invalid roadmap status {data.get('status')!r}")
    if data.get("review_status") not in ROADMAP_STATUSES:
        errors.append(f"{machine_path}: invalid review_status {data.get('review_status')!r}")
    stages = data.get("stages")
    if not isinstance(stages, list) or not stages:
        return errors + [f"{machine_path}: stages must be a non-empty list"]
    by_id: dict[str, dict[str, Any]] = {}
    for stage in stages:
        if not isinstance(stage, dict):
            errors.append(f"{machine_path}: each stage must be a mapping")
            continue
        missing = REQUIRED_STAGE_FIELDS - set(stage)
        if missing:
            errors.append(f"{machine_path}: {stage.get('id')!r} missing fields {sorted(missing)}")
        stage_id = stage.get("id")
        if not isinstance(stage_id, str) or not STAGE_ID_RE.fullmatch(stage_id):
            errors.append(f"{machine_path}: invalid stage ID {stage_id!r}")
            continue
        if stage_id in by_id:
            errors.append(f"{machine_path}: duplicate stage ID {stage_id}")
            continue
        by_id[stage_id] = stage
        if stage.get("status") not in CAPABILITY_STATUSES:
            errors.append(f"{machine_path}: {stage_id} has invalid stage status {stage.get('status')!r}")
        if stage.get("capability_status") not in CAPABILITY_STATUSES:
            errors.append(f"{machine_path}: {stage_id} has invalid capability status {stage.get('capability_status')!r}")
        for field in ("prerequisites", "entry_criteria", "deliverables", "validation", "exit_gates", "success_measures", "dependencies"):
            if not isinstance(stage.get(field), list) or not all(isinstance(item, str) for item in stage[field]):
                errors.append(f"{machine_path}: {stage_id}.{field} must be a string list")
        if stage.get("downstream_prompt") is not None and not isinstance(stage.get("downstream_prompt"), str):
            errors.append(f"{machine_path}: {stage_id}.downstream_prompt must be string or null")
    for stage_id, stage in by_id.items():
        refs = list(stage.get("prerequisites", [])) + list(stage.get("dependencies", []))
        for ref in refs:
            if ref not in by_id and ref != "stage-08":
                errors.append(f"{machine_path}: {stage_id} references missing stage {ref}")
        if stage_id in stage.get("dependencies", []):
            errors.append(f"{machine_path}: {stage_id} depends on itself")
    graph = {stage_id: [ref for ref in stage.get("dependencies", []) if ref in by_id] for stage_id, stage in by_id.items()}
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"{machine_path}: dependency cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency)
        visiting.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)
    try:
        text = human_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{human_path}: cannot read human roadmap: {exc}")
        return errors
    human_ids = set(re.findall(r"^## (Stage-[0-9]+(?:\.[0-9]+)?) —", text, flags=re.MULTILINE))
    human_ids = {item.lower() for item in human_ids}
    machine_ids = set(by_id)
    if human_ids != machine_ids:
        errors.append(f"{human_path}: stage headings do not match machine roadmap: human={sorted(human_ids)}, machine={sorted(machine_ids)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("Roadmap validation failed.")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Roadmap validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
