#!/usr/bin/env python3
"""Run the controlled repository text reader for an authorized planned run."""

from __future__ import annotations

import argparse
import hashlib
import html.parser
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from scripts.validate_source_processing import validate_repository
except ModuleNotFoundError:  # Direct execution: python scripts/extract_text.py
    from validate_source_processing import validate_repository


TEXT_EXTENSIONS = {".mmd", ".md", ".markdown", ".txt", ".text"}
HTML_EXTENSIONS = {".html", ".htm"}


class _HTMLTextExtractor(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.suppressed_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.suppressed_depth += 1
        elif tag in {"br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.suppressed_depth:
            self.suppressed_depth -= 1
        elif tag in {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.suppressed_depth:
            self.parts.append(data)


def extract_content(path: Path) -> str:
    suffix = path.suffix.lower()
    raw = path.read_text(encoding="utf-8")
    if suffix in TEXT_EXTENSIONS:
        text = raw
    elif suffix in HTML_EXTENSIONS:
        parser = _HTMLTextExtractor()
        parser.feed(raw)
        text = "".join(parser.parts)
    else:
        raise ValueError(f"unsupported repository text-reader extension: {suffix}")
    lines = [" ".join(line.split()) for line in text.splitlines()]
    return "\n".join(line for line in lines if line).strip() + "\n"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_output_path(root: Path, requested: Path, classification: str) -> Path:
    output = requested.resolve() if requested.is_absolute() else (root / requested).resolve()
    extracted_root = (root / "sources/extracted").resolve()
    if not output.is_relative_to(extracted_root):
        raise ValueError("output must remain under sources/extracted")
    if classification in {"internal", "restricted"}:
        private_root = (extracted_root / "private").resolve()
        if not output.is_relative_to(private_root):
            raise ValueError(
                f"{classification} output must remain under sources/extracted/private"
            )
    return output


def _load(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    root = args.root.resolve()

    validation = validate_repository(root)
    if not validation.ok:
        for error in validation.errors:
            print(error, file=sys.stderr)
        return 1

    runs = _load(root / "sources/processing-runs.yaml")["records"]
    run = next((record for record in runs if record.get("id") == args.run_id), None)
    if run is None:
        print(f"unknown processing run: {args.run_id}", file=sys.stderr)
        return 1
    if run.get("tool_id") != "repository_text_reader":
        print(f"run {args.run_id} does not authorize repository_text_reader", file=sys.stderr)
        return 1
    if run.get("status") not in {"planned", "in_progress"}:
        print(f"run {args.run_id} is not ready for execution", file=sys.stderr)
        return 1

    catalogue = _load(root / "sources/catalogue.yaml")
    source = next(
        (record for record in catalogue["records"] if record.get("id") == run.get("source_id")),
        None,
    )
    if source is None:
        print(f"run {args.run_id} references an unknown source", file=sys.stderr)
        return 1
    source_root = Path(catalogue["source_root"]["path"]).resolve()
    source_path = (source_root / source["relative_path"]).resolve()
    if not source_path.is_relative_to(source_root):
        print("resolved source path escapes the approved source root", file=sys.stderr)
        return 1
    actual_source_hash = sha256_file(source_path)
    if actual_source_hash != run.get("source_hash_sha256"):
        print(
            f"source hash mismatch for {run.get('source_id')}: expected "
            f"{run.get('source_hash_sha256')}, got {actual_source_hash}",
            file=sys.stderr,
        )
        return 1
    try:
        output_path = resolve_output_path(root, args.output, run["classification"])
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if output_path.exists():
        print(f"refusing to overwrite existing output: {output_path}", file=sys.stderr)
        return 1

    extracted = extract_content(source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(extracted, encoding="utf-8")
    output_hash = hashlib.sha256(extracted.encode("utf-8")).hexdigest()
    print(f"Run: {args.run_id}")
    print(f"Output: {output_path}")
    print(f"SHA-256: {output_hash}")
    print("Update the run record with completion metadata before evidence use.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
