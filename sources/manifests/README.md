# Source manifests

Domain manifests are domain-specific views of the canonical source catalogue.

`sources/catalogue.yaml` is authoritative. Any manifest in this directory must remain consistent with the catalogue, preserve stable source IDs, and use the same provenance and handling decisions.

## What manifests may contain

- stable source IDs
- source-root references
- filenames and relative paths
- file metadata and hashes
- classification and processing-state values
- duplicate markers and exception flags

## What manifests may not contain

- summaries
- interpretation
- analysis
- generated conclusions

This directory is metadata-only. Body analysis belongs elsewhere and only after the source is approved for processing.

## Duplicate handling

Duplicate candidates stay as separate manifest entries until the catalogue records their relationship. A duplicate flag does not replace the stable source ID and does not authorize deletion or overwrite.

## Exception handling

Unreadable files, blocked files, superseded sources, and processing exceptions must be recorded in the catalogue and reflected in the manifest view. Exceptions are administrative states, not analysis outputs.

## Consistency rule

If a manifest and the catalogue disagree, the catalogue wins. The manifest must be updated to match the catalogue before any inventory review is considered complete.
