# Sources

This directory contains source metadata, manifests, source notes, authorization
and run registers, and controlled extraction areas. It is partially
implemented: the canonical catalogue conflict has been explicitly reconciled,
approved authorization/run contracts and 57 per-source authorizations exist,
and a controlled repository text reader is available. No successful reviewed
run or production evidence exists.

The canonical source inventory is `sources/catalogue.yaml`. `../registers/sources.yaml` is retained only as a legacy compatibility snapshot.

The approved machine-readable contract for the catalogue is
`../schemas/sources.yaml`. Its decision rationale, approval boundary, reviewer,
and decision date are recorded in
`../project/decisions/0002-canonical-source-catalogue-schema.md`.

The `extracted/private/` path is excluded from Git. Other extracted artifacts are not automatically excluded; they may be tracked only after classification and information-handling review confirms that repository storage is permitted.

## Source-access boundary

The original evidence remains outside Git under the approved local source root recorded in `config/source-types.yaml`. This directory may contain only approved metadata, manifests, notes, hashes, summaries, and normalized derivatives that comply with `project/source-management-policy.md`.

Manifest conventions are documented in `manifests/README.md`, while controlled source-root values, states, ignored patterns, and file-type controls are defined in `config/source-types.yaml`.

## Processing control records

`processing-authorizations.yaml` binds a source to an approved classification,
route, tool, environment, reviewer, date, and decision basis. A valid
authorization permits a run; it is not proof that processing occurred.
`processing-runs.yaml` preserves each execution, source hash, output reference
and hash, outcome, operator, and review state. IDs use `AUTH-NNNNNN` and
`RUN-NNNNNN`, are allocated monotonically, and are never reused.

The authorization register contains 57 approved records. The run register
contains one successful, technically verified pilot. Use the templates in
`templates/` to create one planned run at a time and validate changes with
`python scripts/validate_source_processing.py`. Only a successful run reviewed
as `verified` or `approved` may support production evidence.

Three newly catalogued PPTX sources, `SRC-UC-000012`–`000014`, remain
unclassified and metadata-only pending the exact approval recorded in
`project/status/implemented-use-cases-ingestion.md`.
