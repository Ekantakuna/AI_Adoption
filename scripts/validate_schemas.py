#!/usr/bin/env python3
"""Validate repository schemas and schema-governed records with Draft 2020-12."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


DIALECT = "https://json-schema.org/draft/2020-12/schema"
MARKDOWN_FRONT_MATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", re.DOTALL
)


@dataclass
class ValidationResult:
    schemas: int = 0
    source_records: int = 0
    authorization_records: int = 0
    processing_runs: int = 0
    knowledge_records: int = 0
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


def _load_markdown_front_matter(path: Path, errors: list[str]) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read Markdown: {exc}")
        return None
    match = MARKDOWN_FRONT_MATTER_RE.match(text)
    if not match:
        errors.append(f"{path}: Markdown production record requires YAML front matter")
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: cannot parse YAML front matter: {exc}")
        return None


def _is_template(path: Path, data: Any) -> bool:
    return path.stem.lower().endswith("-template") or (
        isinstance(data, dict) and data.get("template") is True
    )


def _format_error(path: Path, error: Any) -> str:
    location = ".".join(str(part) for part in error.absolute_path)
    suffix = f" at {location}" if location else ""
    return f"{path}: {error.message}{suffix}"


def validate_repository(root: Path | str) -> ValidationResult:
    root = Path(root).resolve()
    result = ValidationResult()
    format_checker = FormatChecker()
    validators: dict[Path, Draft202012Validator] = {}

    for schema_path in sorted((root / "schemas").glob("*.schema.yaml")):
        schema = _load_yaml(schema_path, result.errors)
        if not isinstance(schema, dict):
            result.errors.append(f"{schema_path}: schema must be a YAML mapping")
            continue
        if schema.get("$schema") != DIALECT:
            result.errors.append(
                f"{schema_path}: expected Draft 2020-12 $schema value {DIALECT!r}"
            )
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            result.errors.append(f"{schema_path}: invalid Draft 2020-12 schema: {exc.message}")
            continue
        validators[schema_path.resolve()] = Draft202012Validator(
            schema, format_checker=format_checker
        )
        result.schemas += 1

    source_schema_path = (root / "schemas/sources.yaml").resolve()
    source_schema = _load_yaml(source_schema_path, result.errors)
    if isinstance(source_schema, dict):
        if source_schema.get("$schema") != DIALECT:
            result.errors.append(
                f"{source_schema_path}: expected Draft 2020-12 $schema value {DIALECT!r}"
            )
        else:
            try:
                Draft202012Validator.check_schema(source_schema)
            except SchemaError as exc:
                result.errors.append(
                    f"{source_schema_path}: invalid Draft 2020-12 schema: {exc.message}"
                )
            else:
                validators[source_schema_path] = Draft202012Validator(
                    source_schema, format_checker=format_checker
                )
                result.schemas += 1

    catalogue_path = root / "sources/catalogue.yaml"
    catalogue = _load_yaml(catalogue_path, result.errors)
    source_validator = validators.get(source_schema_path)
    if source_validator is not None and catalogue is not None:
        for error in sorted(source_validator.iter_errors(catalogue), key=str):
            result.errors.append(_format_error(catalogue_path, error))
    if isinstance(catalogue, dict) and isinstance(catalogue.get("records"), list):
        result.source_records = len(catalogue["records"])

    governed_registers = (
        (
            "schemas/source-processing-authorization.schema.yaml",
            "sources/processing-authorizations.yaml",
            "authorization_records",
        ),
        (
            "schemas/processing-run.schema.yaml",
            "sources/processing-runs.yaml",
            "processing_runs",
        ),
    )
    for schema_name, instance_name, count_attribute in governed_registers:
        schema_path = (root / schema_name).resolve()
        instance_path = root / instance_name
        if schema_path not in validators and not instance_path.exists():
            continue
        validator = validators.get(schema_path)
        if validator is None:
            result.errors.append(f"{instance_path}: no valid schema loaded for {schema_name}")
            continue
        instance = _load_yaml(instance_path, result.errors)
        if instance is None:
            continue
        for error in sorted(validator.iter_errors(instance), key=str):
            result.errors.append(_format_error(instance_path, error))
        if isinstance(instance, dict) and isinstance(instance.get("records"), list):
            setattr(result, count_attribute, len(instance["records"]))

    type_path = root / "config/knowledge-types.yaml"
    type_config = _load_yaml(type_path, result.errors)
    definitions = type_config.get("object_types") if isinstance(type_config, dict) else None
    if not isinstance(definitions, list):
        result.errors.append(f"{type_path}: expected top-level 'object_types' list")
        definitions = []

    for definition in definitions:
        if not isinstance(definition, dict):
            result.errors.append(f"{type_path}: invalid object type definition")
            continue
        directory = definition.get("directory")
        schema_name = definition.get("schema")
        if schema_name is None:
            continue
        if not isinstance(directory, str) or not isinstance(schema_name, str):
            result.errors.append(
                f"{type_path}: schema-governed types require string directory and schema values"
            )
            continue
        schema_path = (root / schema_name).resolve()
        validator = validators.get(schema_path)
        if validator is None:
            result.errors.append(f"{type_path}: no valid schema loaded for {schema_name}")
            continue
        object_directory = root / directory
        for path in sorted(object_directory.rglob("*")) if object_directory.exists() else []:
            if (
                not path.is_file()
                or path.name.lower() == "readme.md"
                or path.suffix.lower() not in {".yaml", ".yml", ".md"}
            ):
                continue
            data = (
                _load_markdown_front_matter(path, result.errors)
                if path.suffix.lower() == ".md"
                else _load_yaml(path, result.errors)
            )
            if _is_template(path, data):
                continue
            if data is None:
                continue
            result.knowledge_records += 1
            for error in sorted(validator.iter_errors(data), key=str):
                result.errors.append(_format_error(path, error))

    return result


def _print_result(result: ValidationResult) -> None:
    print("Schema validation passed." if result.ok else "Schema validation failed.")
    print(f"Draft 2020-12 schemas checked: {result.schemas}")
    print(f"Source catalogue records: {result.source_records}")
    print(f"Source processing authorizations: {result.authorization_records}")
    print(f"Source processing runs: {result.processing_runs}")
    print(f"Production knowledge records: {result.knowledge_records}")
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
    args = parser.parse_args(argv)
    result = validate_repository(args.root)
    _print_result(result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
