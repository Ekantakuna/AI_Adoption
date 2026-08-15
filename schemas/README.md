# Schemas

This directory is the target location for machine-readable contracts used to
validate configuration, registers, and source metadata.

`sources.yaml` is the human-approved JSON Schema Draft 2020-12 contract for
`sources/catalogue.yaml`. Approval is recorded in ADR 0002. Its identifier,
controlled-value, lifecycle, ownership, operating, and limitation details are
recorded in `project/decisions/0002-canonical-source-catalogue-schema.md`.

Install `requirements-validation.txt` and run:

```text
python scripts/validate_schemas.py
```

The command checks every repository schema against the Draft 2020-12
meta-schema, enables declared format checks, validates the source catalogue,
and validates production knowledge records against configured schemas.

## Source catalogue contract

The top-level object requires the schema version, catalogue type, authority
marker, source-root metadata, embedded controlled-value copies, generation
timestamp, declared record count, and records. `authority: true` identifies the
catalogue as the designated metadata inventory; it does not approve any record's
classification, processing state, or source-body access.

Each source record requires:

- identity and display metadata: `id`, `apparent_title_from_filename`, and
  `original_filename`;
- location and domain metadata: `source_path`, `relative_path`, `domains`, and
  the legacy singular `domain` compatibility field;
- file metadata: `source_type`, `file_extension`, `file_size_bytes`,
  `content_hash_sha256`, and `filesystem_modified_at`;
- administrative lifecycle metadata: `classification`, `processing_status`,
  `readability_status`, `duplicate_status`, `date_discovered`, and
  `last_verified`;
- the optional relationship value `duplicate_of` and the legacy heterogeneous
  `notes` value.

All listed fields are structurally required, although `duplicate_of` and
`notes` may be null. The schema rejects unknown properties and constrains ID,
hash, extension, timestamp, and controlled-value shapes. JSON Schema alone does
not check record-count equality, ID uniqueness, configured-prefix membership,
cross-record references, domain taxonomy membership, source-type/source-group
mapping, or catalogue/manifest consistency; those source-catalogue rules still
need a dedicated repository validator.

## Stage 9 knowledge contracts

Stage 9 adds Draft 2020-12 YAML schemas for atomic evidence, glossary entries,
concepts, frameworks, metrics, risks, trends, use cases, relationships,
assumptions, knowledge decisions, and contextual references. They define required content,
six-digit identifiers, classifications, review statuses, AI/human origin, and
reviewer gates. All configured knowledge objects, including assumptions,
require evidence IDs; an assumption's evidence establishes context rather than
verification. Relationship endpoints are checked by the repository validator.

`python scripts/validate_schemas.py` performs standards-based instance
validation. `python scripts/validate_knowledge.py` separately performs
cross-file integrity checks such as global uniqueness and referential
integrity. `python scripts/validate_relationship_impact.py` adds ADR-0011
relationship-type, endpoint-pair, lifecycle, cycle, and traversal-integrity
checks and verifies that the schema relationship-type enum matches
`config/relationship-types.yaml`. The configuration file has no separate JSON
Schema; its consumed structure is checked by the validator. Other configuration
files and non-source registers remain without schemas; their empty production
registers must remain empty until approved contracts exist.

## Stage 12 entry-control contracts

`scoring-models.schema.yaml` validates the approved unscored initial mode in
`config/scoring_models.yaml`, including its human-review metadata, required
claim/evidence behavior, prohibited scoring operations, maintenance boundary,
and empty model list. `audiences.schema.yaml` validates the single approved
`AUD-000001` version `1.0.0` record, exact classification permissions,
prohibitions, mechanical owner, human approval authority, and review metadata.

These intentionally narrow schemas reject scoring models, additional audiences,
permission expansion, and unknown fields. They do not define assessment records
or grant audience membership, approve assessment content, or authorize public
release. `validate_schemas.py` validates both configuration instances and
reports their count with the other governed repository objects.

## Source-processing contracts

`source-processing-authorization.schema.yaml` defines stable authorization IDs,
source/classification binding, route, tool, environment, reviewer, decision
basis, and lifecycle state. `processing-run.schema.yaml` defines stable run IDs,
source and authorization binding, input/output hashes, execution lifecycle,
operator, and review state. The standards-based schema validator checks both
registers, while `scripts/validate_source_processing.py` enforces their
cross-record gates. Maksim Zakharenkau approved these contracts on 2026-08-02;
their presence alone does not grant access without an approved per-source
authorization and run.
