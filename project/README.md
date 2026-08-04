# Project management

This directory contains repository governance and project-control
documentation. It is partially implemented: policies, proposed Architecture
Decision Records (ADRs), and status notes exist; `meeting-notes/` and `reviews/`
are empty scaffolds, and most structured project registers are empty.

## Areas

- `information-handling.md` defines classification, storage, evidence
  protection, and human-review boundaries.
- `source-management-policy.md` defines source inventory and access controls.
- `knowledge-management-policy.md`, `knowledge-extraction-guidelines.md`, and
  `knowledge-review-workflow.md` define the approved Stage 9 knowledge controls.
- `source-processing-control-policy.md` defines approved per-source
  authorization and processing-run controls.
- `decisions/` stores numbered ADRs. AI-authored ADRs remain `proposed` until an
  authorized human records approval.
- `status/` stores dated or stage-scoped evidence about repository state.
  Historical reports do not override a canonical record and must identify
  conflicts or supersession.
  `status/stage-09-knowledge-framework.md` records the implemented empty
  knowledge framework and its closed approval boundary.
  `status/source-processing-controls.md` records the approved post-Stage-9
  controls and remaining run/evidence boundary.
- `meeting-notes/` and `reviews/` are planned record locations. No identifier,
  lifecycle, or schema is approved for them.

Project records must preserve provenance, stable IDs where defined, review
state, reviewer identity where supported, and unresolved conflicts. Original
source assets do not belong here. See the
[repository map](../docs/repository-map.md) and
[status definitions](../docs/reference/statuses.md).
