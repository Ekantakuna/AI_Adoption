#!/usr/bin/env python3
"""Validate Codex prompt metadata and catalogue integrity."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml


REQUIRED = {
    "id", "title", "type", "version", "status", "owner_role", "created_at",
    "updated_at", "roadmap_stage", "source_access", "allowed_paths",
    "prohibited_actions", "required_inputs", "expected_outputs", "validation",
    "human_review", "supersedes", "superseded_by",
}
STATUSES = {"draft", "active", "deprecated", "superseded", "retired"}
SOURCE_ACCESS = {"none", "repository_only", "metadata_only", "approved_source_subset", "approved_source_corpus"}
TYPES = {"bootstrap", "planning", "stage", "review", "validation", "maintenance", "extraction", "knowledge", "assessment", "reporting", "presentation", "template"}


class Result:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.prompts = 0

    @property
    def ok(self) -> bool:
        return not self.errors


def front_matter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML front matter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("unterminated YAML front matter") from exc
    value = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(value, dict):
        raise ValueError("front matter must be a mapping")
    return value


def validate_repository(root: Path) -> Result:
    result = Result()
    prompt_root = root / "prompts" / "codex"
    catalogue_path = prompt_root / "prompt-catalogue.yaml"
    if not catalogue_path.exists():
        result.errors.append(f"missing {catalogue_path.relative_to(root)}")
        return result
    try:
        catalogue = yaml.safe_load(catalogue_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        result.errors.append(f"invalid catalogue YAML: {exc}")
        return result
    entries = catalogue.get("prompts") if isinstance(catalogue, dict) else None
    if not isinstance(entries, list):
        result.errors.append("catalogue must contain a prompts list")
        entries = []

    metadata: dict[str, tuple[Path, dict]] = {}
    for path in sorted(prompt_root.rglob("*.md")):
        if path.name == "README.md":
            continue
        result.prompts += 1
        try:
            data = front_matter(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            result.errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        missing = REQUIRED - data.keys()
        if missing:
            result.errors.append(f"{path.relative_to(root)}: missing metadata {sorted(missing)}")
        for field, allowed in (("type", TYPES), ("status", STATUSES), ("source_access", SOURCE_ACCESS)):
            if data.get(field) not in allowed:
                result.errors.append(f"{path.relative_to(root)}: invalid {field} {data.get(field)!r}")
        if not isinstance(data.get("id"), str) or not data.get("id"):
            result.errors.append(f"{path.relative_to(root)}: id must be a non-empty string")
        elif data["id"] in metadata:
            result.errors.append(f"duplicate prompt ID {data['id']}")
        else:
            metadata[data["id"]] = (path, data)
        if data.get("status") in {"deprecated", "superseded"} and not data.get("superseded_by"):
            result.errors.append(f"{path.relative_to(root)}: deprecated/superseded prompt needs superseded_by")
        if data.get("type") == "template" and data.get("status") == "active":
            result.errors.append(f"{path.relative_to(root)}: templates cannot be active")

    catalogue_ids: set[str] = set()
    catalogue_paths: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            result.errors.append("catalogue entry must be a mapping")
            continue
        missing = {"id", "path", "type", "version", "status", "roadmap_stage", "purpose", "source_access", "expected_output_category"} - entry.keys()
        if missing:
            result.errors.append(f"catalogue entry missing {sorted(missing)}")
            continue
        prompt_id = entry["id"]
        path_value = entry["path"]
        if prompt_id in catalogue_ids:
            result.errors.append(f"duplicate catalogue prompt ID {prompt_id}")
        catalogue_ids.add(prompt_id)
        if path_value in catalogue_paths:
            result.errors.append(f"duplicate catalogue path {path_value}")
        catalogue_paths.add(path_value)
        candidate = root / path_value
        if not candidate.exists():
            result.errors.append(f"catalogue path does not exist: {path_value}")
        if entry["type"] not in TYPES - {"template"}:
            result.errors.append(f"catalogue entry {prompt_id}: invalid production type {entry['type']!r}")
        if entry["status"] != "active":
            result.errors.append(f"catalogue entry {prompt_id}: production status must be active")
        if entry["source_access"] not in SOURCE_ACCESS:
            result.errors.append(f"catalogue entry {prompt_id}: invalid source_access")
        if prompt_id in metadata:
            data_path, data = metadata[prompt_id]
            if str(data_path.relative_to(root)) != path_value:
                result.errors.append(f"catalogue path mismatch for {prompt_id}")
            if data.get("status") != "active":
                result.errors.append(f"catalogued prompt {prompt_id} is not active")
            for field in ("type", "version", "roadmap_stage", "source_access"):
                if data.get(field) != entry[field]:
                    result.errors.append(f"catalogue metadata mismatch for {prompt_id}: {field}")
        else:
            result.errors.append(f"catalogue references unknown prompt ID {prompt_id}")

    active_ids = {data["id"] for _, data in metadata.values() if data.get("status") == "active" and data.get("type") != "template"}
    missing_catalogue = active_ids - catalogue_ids
    for prompt_id in sorted(missing_catalogue):
        result.errors.append(f"active production prompt is not catalogued: {prompt_id}")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    result = validate_repository(args.root.resolve())
    if result.ok:
        print(f"Prompt validation passed: {result.prompts} prompt files inspected, {len(yaml.safe_load((args.root / 'prompts/codex/prompt-catalogue.yaml').read_text(encoding='utf-8')).get('prompts', []))} catalogue entries.")
        return 0
    for error in result.errors:
        print(f"ERROR: {error}")
    print(f"Prompt validation failed: {len(result.errors)} error(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
