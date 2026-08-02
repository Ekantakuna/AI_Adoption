# ADR 0002: Canonical source catalogue schema

- Status: approved
- Date: 2026-07-30
- Decision owners: repository maintainers and authorized human reviewers
- Proposed by: Codex during source-governance reconciliation
- Approved by: Maksim Zakharenkau
- Approved on: 2026-07-30

## Context

Repository policy designates `sources/catalogue.yaml` as the canonical source
inventory, but `schemas/sources.yaml` previously described the incompatible
legacy shape stored in `registers/sources.yaml`. The canonical catalogue uses
fields such as `id` and `processing_status`; the legacy register uses
`source_id` and `processing_state` and contains disputed later classification
and processing claims.

Changing the canonical catalogue to the legacy shape at this point would mix a
schema migration with resolution of those disputed values. That would make it
difficult to distinguish structural changes from human-approved governance
decisions.

## Decision

Use `schemas/sources.yaml` as a JSON Schema Draft 2020-12 contract for the
existing `sources/catalogue.yaml` record shape.

The schema:

- identifies `sources/catalogue.yaml` as a metadata-only catalogue;
- validates the existing field names without importing legacy-register values;
- constrains source IDs, source-root IDs, hashes, timestamps, controlled
  classifications, and administrative statuses;
- requires all currently implemented catalogue fields;
- preserves the current heterogeneous `notes` field temporarily and records
  its normalization as later migration work;
- does not treat schema conformance as classification approval, processing
  authorization, evidence review, or permission to inspect source bodies.

`config/source-types.yaml` and `project/source-management-policy.md` remain the
authoritative definitions of source controlled values and handling behavior.
The corresponding enums in the schema are validation copies and must be changed
with those authorities in the same reviewed change.

## Inputs and outputs

The schema consumes the structure and controlled values currently implemented
by:

- `sources/catalogue.yaml`;
- `config/source-types.yaml`;
- `project/source-management-policy.md`.

Its output is a pass/fail schema-validation result when a Draft 2020-12
validator is configured. It does not generate or modify catalogue records.

## Identifier and lifecycle rules

Source IDs retain the `SRC-<allocation-prefix>-<six digits>` form and must
remain stable. Source-root IDs retain the `SROOT-<four digits>` form. Schema
approval does not authorize renumbering, reuse, deletion, or silent merging of
duplicate records.

Catalogue records move through the processing states defined by source policy.
A state transition requires its own supporting review and cannot be inferred
from schema validity.

## Relationships

`duplicate_of` may reference another stable source ID. Referential integrity,
prefix membership, record-count equality, uniqueness, domain membership, and
cross-file catalogue/manifest consistency require repository-level validation;
JSON Schema alone does not establish all of them.

## Ownership and review

Repository maintainers own the schema. Maksim Zakharenkau approved this ADR on
2026-07-30 as the authorized human reviewer. Any later incompatible field
change requires a documented migration and review.

## Operational procedure

1. Edit controlled values in their authoritative policy/configuration location.
2. Update the matching schema validation copies in the same change.
3. Validate YAML syntax and run a Draft 2020-12 schema validator.
4. Run repository-level integrity and cross-file consistency checks when those
   validators exist.
5. Review the diff for stable-ID or provenance changes before acceptance.

## Limitations

- The schema does not resolve conflicting catalogue, legacy-register, manifest,
  or status values.
- `notes` accepts the three representations found in the current catalogue.
- The absolute source-root path remains machine-specific.
- Cross-record and cross-file rules require a future repository validator.

## Alternatives considered

### Adopt the legacy register shape immediately

Not selected because it would combine a structural migration with unresolved
classification, route, and extraction claims.

### Keep the informal required-field list

Not selected because it cannot be executed by a standard schema validator and
does not describe the authoritative catalogue.

## Validation and review

The authorized reviewer accepted the chosen field shape, controlled-value
ownership, identifier patterns, required fields, and temporary handling of
`notes` on 2026-07-30. This approval does not approve disputed classifications,
processing routes, extraction claims, or source-body access.
