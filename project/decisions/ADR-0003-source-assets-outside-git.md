---
id: ADR-0003
title: Keep source assets outside Git and catalogue metadata only
status: proposed
date: 2026-07-30
decision_owners:
  - repository maintainers
supersedes:
superseded_by:
---

# ADR-0003 — Keep source assets outside Git and catalogue metadata only

## Context

The repository processes source material with different classifications and
handling routes. The implemented source configuration identifies an external
source root with `storage: outside_git`, the source catalogue declares itself
to be metadata-only, and repository policy prohibits copying original source
documents into Git. The tracked catalogue contains administrative metadata such
as identifiers, paths, sizes, hashes, classification, and processing state
rather than source bodies.

This storage and access boundary is the proposed operating rule. Controlled
extraction, evidence promotion, and downstream processing remain partial or
planned; this decision does not claim that those capabilities operate.

## Decision

Keep original source assets in approved storage outside Git. Track only source
metadata and derivatives whose classification and approved handling route
permit repository storage.

Use `sources/catalogue.yaml` as the canonical metadata-only source inventory.
Metadata inspection does not authorize source-body access. Ignore rules are an
accidental-disclosure control, not handling approval.

## Rationale

Separating source bodies from the repository reduces disclosure risk, preserves
the original evidence boundary, and allows inventory work to proceed without
mistaking metadata collection for content processing.

## Alternatives considered

### Commit original source assets

Not selected because source classifications and routes differ, Git history is
difficult to purge safely, and repository processing must not modify or
silently replace original evidence.

### Store source content in the catalogue

Not selected because it would mix administrative inventory with evidence
content, expand the catalogue's classification, and bypass the content-access
gate.

### Treat every derivative as local-only

Not selected because approved metadata, summaries, normalized knowledge, and
publications may be tracked when their classification and handling route allow
it.

## Consequences

### Positive

- Source provenance remains anchored to an external original.
- Metadata inventory can be reviewed independently from body processing.
- Repository clones do not intentionally contain original source documents.

### Negative

- Reproducing body processing requires authorized access to the external source
  root.
- Machine-specific source locations require controlled configuration.

### Risks

- A contributor may mistake an unignored path for storage approval.
- Metadata may itself be sensitive and still requires classification-aware
  handling.

## Implementation implications

`config/source-types.yaml` records the external source root and prohibits
original binaries by default. `schemas/sources.yaml` and
`sources/catalogue.yaml` implement the metadata-only catalogue contract.
`project/source-management-policy.md` and
`project/information-handling.md` define storage and access controls.

Downstream evidence, extraction, and processing-run contracts are not yet
implemented. No run, derivative, or production evidence exists.

## Validation

Review catalogue structure against `schemas/sources.yaml`, verify the configured
source root remains `outside_git`, scan tracked source paths for unexpected
binaries, and review Git changes for source content. Automated repository-wide
enforcement is not currently configured.

Repository-wide prevention of accidentally tracked source bodies depends on
review and ignore controls.

## References

- [Source management policy](../source-management-policy.md)
- [Information-handling rules](../information-handling.md)
- [Source configuration](../../config/source-types.yaml)
- [Canonical source catalogue](../../sources/catalogue.yaml)
- [Canonical catalogue schema](../../schemas/sources.yaml)
- [Source directory contract](../../sources/README.md)
- [ADR-0002](0002-canonical-source-catalogue-schema.md)
