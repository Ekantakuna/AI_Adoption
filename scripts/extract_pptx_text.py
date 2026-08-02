#!/usr/bin/env python3
"""Extract slide text from an authorized PPTX processing run."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any

import yaml

try:
    from scripts.extract_text import resolve_output_path, sha256_file
    from scripts.validate_source_processing import validate_repository
except ModuleNotFoundError:  # Direct execution from repository root.
    from extract_text import resolve_output_path, sha256_file
    from validate_source_processing import validate_repository


DRAWING_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
SLIDE_RE = re.compile(r"^ppt/slides/slide([0-9]+)\.xml$")


def extract_pptx_content(path: Path) -> str:
    slides: list[tuple[int, str]] = []
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            match = SLIDE_RE.fullmatch(name)
            if not match:
                continue
            root = ET.fromstring(archive.read(name))
            parts = [
                (node.text or "").strip()
                for node in root.findall(f".//{{{DRAWING_NS}}}t")
                if (node.text or "").strip()
            ]
            slides.append((int(match.group(1)), "\n".join(parts)))
    if not slides:
        raise ValueError("PPTX contains no readable slide XML")
    sections = [f"=== Slide {number} ===\n{text}" for number, text in sorted(slides)]
    return "\n\n".join(sections).rstrip() + "\n"


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
    if run is None or run.get("tool_id") != "pptx_xml_reader":
        print(f"run {args.run_id} does not authorize pptx_xml_reader", file=sys.stderr)
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
    actual_hash = sha256_file(source_path)
    if actual_hash != run.get("source_hash_sha256"):
        print(f"source hash mismatch for {run.get('source_id')}", file=sys.stderr)
        return 1
    try:
        output_path = resolve_output_path(root, args.output, run["classification"])
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if output_path.exists():
        print(f"refusing to overwrite existing output: {output_path}", file=sys.stderr)
        return 1

    extracted = extract_pptx_content(source_path)
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
