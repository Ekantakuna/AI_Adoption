#!/usr/bin/env python3
"""Validate source processing authorizations, runs, and catalogue gates."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


AUTH_ID_RE = re.compile(r"^AUTH-[0-9]{6}$")
RUN_ID_RE = re.compile(r"^RUN-[0-9]{6}$")
AMBIGUOUS_REVIEWERS = {"ai", "agent", "codex", "user"}
PROCESSABLE_STATES = {"approved_for_processing", "extraction_in_progress", "extracted", "reviewed"}
EVIDENCE_ELIGIBLE_REVIEW = {"verified", "approved"}


@dataclass
class ValidationResult:
    source_records: int = 0
    authorization_records: int = 0
    approved_authorizations: int = 0
    processing_runs: int = 0
    evidence_eligible_runs: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML: {exc}")
        return None


def _records(data: Any, path: Path, expected_register: str, errors: list[str]) -> list[Any]:
    if not isinstance(data, dict) or data.get("register") != expected_register:
        errors.append(f"{path}: expected register {expected_register!r}")
        return []
    records = data.get("records")
    if not isinstance(records, list):
        errors.append(f"{path}: expected top-level 'records' list")
        return []
    return records


def _definitions(data: Any, key: str, path: Path, errors: list[str]) -> dict[str, dict[str, Any]]:
    entries = data.get(key) if isinstance(data, dict) else None
    if not isinstance(entries, list):
        errors.append(f"{path}: expected top-level '{key}' list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            errors.append(f"{path}: invalid '{key}' entry")
            continue
        if entry["id"] in result:
            errors.append(f"{path}: duplicate '{key}' ID {entry['id']!r}")
            continue
        result[entry["id"]] = entry
    return result


def _string_values(data: Any, key: str, path: Path, errors: list[str]) -> set[str]:
    values = data.get(key) if isinstance(data, dict) else None
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        errors.append(f"{path}: expected top-level '{key}' string list")
        return set()
    return set(values)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_repository(
    root: Path | str, *, verify_local_outputs: bool = False
) -> ValidationResult:
    root = Path(root).resolve()
    result = ValidationResult()

    catalogue_path = root / "sources/catalogue.yaml"
    catalogue = _load_yaml(catalogue_path, result.errors)
    catalogue_records = (
        catalogue.get("records") if isinstance(catalogue, dict) else None
    )
    if not isinstance(catalogue_records, list):
        result.errors.append(f"{catalogue_path}: expected top-level 'records' list")
        catalogue_records = []
    sources: dict[str, dict[str, Any]] = {}
    for record in catalogue_records:
        source_id = record.get("id") if isinstance(record, dict) else None
        if not isinstance(source_id, str):
            result.errors.append(f"{catalogue_path}: source record requires a string id")
        elif source_id in sources:
            result.errors.append(f"{catalogue_path}: duplicate source ID {source_id}")
        else:
            sources[source_id] = record
    result.source_records = len(sources)

    config_path = root / "config/source-processing.yaml"
    config = _load_yaml(config_path, result.errors)
    routes = _definitions(config, "routes", config_path, result.errors)
    tools = _definitions(config, "tools", config_path, result.errors)
    authorization_statuses = _string_values(
        config, "authorization_statuses", config_path, result.errors
    )
    run_statuses = _string_values(config, "run_statuses", config_path, result.errors)
    tool_statuses = _string_values(config, "tool_statuses", config_path, result.errors)
    environments = _string_values(config, "environments", config_path, result.errors)

    authorization_path = root / "sources/processing-authorizations.yaml"
    authorization_data = _load_yaml(authorization_path, result.errors)
    authorization_records = _records(
        authorization_data,
        authorization_path,
        "source_processing_authorizations",
        result.errors,
    )
    result.authorization_records = len(authorization_records)
    authorizations: dict[str, dict[str, Any]] = {}
    approved_by_source: dict[str, str] = {}

    for record in authorization_records:
        if not isinstance(record, dict):
            result.errors.append(f"{authorization_path}: authorization must be a mapping")
            continue
        authorization_id = record.get("id")
        if not isinstance(authorization_id, str) or not AUTH_ID_RE.fullmatch(authorization_id):
            result.errors.append(f"{authorization_path}: invalid authorization ID {authorization_id!r}")
            continue
        if authorization_id.endswith("000000"):
            result.errors.append(f"{authorization_path}: placeholder authorization ID is not production")
        if authorization_id in authorizations:
            result.errors.append(f"{authorization_path}: duplicate authorization ID {authorization_id}")
            continue
        authorizations[authorization_id] = record

        source_id = record.get("source_id")
        source = sources.get(source_id) if isinstance(source_id, str) else None
        if source is None:
            result.errors.append(f"{authorization_path}: {authorization_id} has unknown source ID {source_id!r}")
            continue
        classification = record.get("classification")
        if classification != source.get("classification"):
            result.errors.append(
                f"{authorization_path}: {authorization_id} classification does not match {source_id}"
            )
        status = record.get("status")
        if status not in authorization_statuses:
            result.errors.append(f"{authorization_path}: {authorization_id} has invalid status {status!r}")
        route_id = record.get("route_id")
        route = routes.get(route_id) if isinstance(route_id, str) else None
        if route is None:
            result.errors.append(f"{authorization_path}: {authorization_id} has unknown route {route_id!r}")
        elif classification not in route.get("allowed_classifications", []):
            result.errors.append(f"{authorization_path}: {authorization_id} route disallows {classification!r}")
        tool_id = record.get("tool_id")
        tool = tools.get(tool_id) if isinstance(tool_id, str) else None
        if tool is None:
            result.errors.append(f"{authorization_path}: {authorization_id} has unknown tool {tool_id!r}")
        else:
            if tool.get("status") not in tool_statuses:
                result.errors.append(
                    f"{authorization_path}: {authorization_id} tool has invalid approval status"
                )
            elif status == "approved" and tool.get("status") != "approved":
                result.errors.append(
                    f"{authorization_path}: {authorization_id} uses an unapproved tool"
                )
            if source.get("source_type") not in tool.get("source_types", []):
                result.errors.append(f"{authorization_path}: {authorization_id} tool disallows source type")
            if source.get("file_extension") not in tool.get("extensions", []):
                result.errors.append(f"{authorization_path}: {authorization_id} tool disallows extension")
            if route_id not in tool.get("allowed_routes", []):
                result.errors.append(f"{authorization_path}: {authorization_id} tool disallows route")
        environment = record.get("environment")
        if environment not in environments:
            result.errors.append(f"{authorization_path}: {authorization_id} has invalid environment")
        if classification == "restricted" and environment != "approved_on_prem":
            result.errors.append(f"{authorization_path}: {authorization_id} restricted source requires approved_on_prem")
        reviewer = record.get("approved_by")
        if status == "approved" and (
            not isinstance(reviewer, str)
            or not reviewer.strip()
            or reviewer.strip().lower() in AMBIGUOUS_REVIEWERS
        ):
            result.errors.append(f"{authorization_path}: {authorization_id} requires an identified human approver")
        if status == "approved":
            result.approved_authorizations += 1
            if source.get("processing_status") == "blocked":
                result.errors.append(f"{authorization_path}: {authorization_id} authorizes blocked source {source_id}")
            elif source.get("processing_status") not in PROCESSABLE_STATES:
                result.errors.append(
                    f"{authorization_path}: {authorization_id} source {source_id} is not in a processable state"
                )
            if source_id in approved_by_source:
                result.errors.append(f"{authorization_path}: multiple approved authorizations for {source_id}")
            else:
                approved_by_source[source_id] = authorization_id

    for source_id, source in sources.items():
        if source.get("processing_status") in PROCESSABLE_STATES and source_id not in approved_by_source:
            result.errors.append(
                f"{catalogue_path}: {source_id} is processable without an approved authorization"
            )

    run_path = root / "sources/processing-runs.yaml"
    run_data = _load_yaml(run_path, result.errors)
    run_records = _records(
        run_data, run_path, "source_processing_runs", result.errors
    )
    result.processing_runs = len(run_records)
    seen_runs: set[str] = set()
    for record in run_records:
        if not isinstance(record, dict):
            result.errors.append(f"{run_path}: processing run must be a mapping")
            continue
        run_id = record.get("id")
        if not isinstance(run_id, str) or not RUN_ID_RE.fullmatch(run_id):
            result.errors.append(f"{run_path}: invalid run ID {run_id!r}")
            continue
        if run_id.endswith("000000"):
            result.errors.append(f"{run_path}: placeholder run ID is not production")
        if run_id in seen_runs:
            result.errors.append(f"{run_path}: duplicate run ID {run_id}")
            continue
        seen_runs.add(run_id)
        authorization_id = record.get("authorization_id")
        authorization = authorizations.get(authorization_id)
        if authorization is None or authorization.get("status") != "approved":
            result.errors.append(f"{run_path}: {run_id} lacks an approved authorization")
            continue
        source_id = record.get("source_id")
        source = sources.get(source_id)
        if source is None:
            result.errors.append(f"{run_path}: {run_id} has unknown source ID {source_id!r}")
            continue
        for field_name in ("source_id", "classification", "route_id", "tool_id", "environment"):
            if record.get(field_name) != authorization.get(field_name):
                result.errors.append(f"{run_path}: {run_id} {field_name} does not match authorization")
        if record.get("source_hash_sha256") != source.get("content_hash_sha256"):
            result.errors.append(f"{run_path}: {run_id} source hash does not match catalogue")
        status = record.get("status")
        if status not in run_statuses:
            result.errors.append(f"{run_path}: {run_id} has invalid status {status!r}")
        review_status = record.get("review_status")
        reviewer = record.get("reviewer")
        if review_status in EVIDENCE_ELIGIBLE_REVIEW and (
            not isinstance(reviewer, dict)
            or not isinstance(reviewer.get("name"), str)
            or not reviewer.get("name", "").strip()
            or not reviewer.get("reviewed_at")
        ):
            result.errors.append(f"{run_path}: {run_id} reviewed run requires reviewer metadata")
        if status == "succeeded" and review_status in EVIDENCE_ELIGIBLE_REVIEW:
            result.evidence_eligible_runs += 1
        if verify_local_outputs and status == "succeeded":
            output_ref = record.get("output_ref")
            if not isinstance(output_ref, str) or not output_ref:
                result.errors.append(f"{run_path}: {run_id} has no local output reference")
                continue
            output_path = Path(output_ref)
            if not output_path.is_absolute():
                output_path = root / output_path
            output_path = output_path.resolve()
            extracted_root = (root / "sources/extracted").resolve()
            if not output_path.is_relative_to(extracted_root):
                result.errors.append(
                    f"{run_path}: {run_id} local output escapes sources/extracted"
                )
            elif not output_path.is_file():
                result.errors.append(f"{run_path}: {run_id} local output is missing")
            elif _sha256_file(output_path) != record.get("output_hash_sha256"):
                result.errors.append(
                    f"{run_path}: {run_id} local output hash does not match"
                )

    return result


def _print_result(result: ValidationResult) -> None:
    print("Source processing validation passed." if result.ok else "Source processing validation failed.")
    print(f"Source records: {result.source_records}")
    print(f"Authorization records: {result.authorization_records}")
    print(f"Approved authorizations: {result.approved_authorizations}")
    print(f"Processing runs: {result.processing_runs}")
    print(f"Evidence-eligible runs: {result.evidence_eligible_runs}")
    print(f"Errors: {len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root",
    )
    parser.add_argument(
        "--verify-local-outputs",
        action="store_true",
        help="require succeeded outputs under sources/extracted and verify their hashes",
    )
    args = parser.parse_args(argv)
    result = validate_repository(
        args.root, verify_local_outputs=args.verify_local_outputs
    )
    _print_result(result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
