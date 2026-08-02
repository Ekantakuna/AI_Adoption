---
id: ADR-0005
title: Preserve stable identifiers
status: accepted
date: 2026-07-30
reviewed_by: Maksim Zakharenkau
reviewed_at: 2026-08-02
decision_owners:
  - repository maintainers
supersedes:
superseded_by:
---

# ADR-0005 — Preserve stable identifiers

## Context

Stable identifiers are required to connect records without depending on
filenames, paths, titles, or presentation order. The repository implements a
project ID, a source-root ID, 58 source IDs, configured source-ID prefixes, and
source-ID validation patterns. Policy requires IDs to survive path and filename
changes and prohibits reuse or presentation-only renumbering.

This rule is implemented for project, source-root, source, and the empty Stage
9 knowledge framework. Maksim Zakharenkau accepted this AI-authored ADR on
2026-08-02. The Stage 9 knowledge identifiers are approved contracts;
identifier models for assessments, most project records, publications, and
presentations remain absent. Evidence records carry a `RUN-NNNNNN` reference
shape, but no processing-run identity registry exists.

## Decision

Allocate an identifier once for each object type that has an approved identity
contract. Preserve that identifier across path, filename, title, state, and
domain changes. Never reuse it for a different object.

Represent duplicates, replacement, and supersession through explicit
relationships or lifecycle state. Do not delete, merge, or renumber an identity
merely to simplify presentation.

Do not invent identifiers for object types whose allocation and validation
rules have not been approved.

## Rationale

Stable identity preserves provenance, supports downstream references, and makes
change and conflict history reviewable.

## Alternatives considered

### Use paths or filenames as identifiers

Not selected because they can change without changing the underlying source.

### Renumber records for display

Not selected because presentation order would break references and obscure
history.

### Allocate prefixes for every scaffold now

Not selected because most object schemas, ownership rules, and lifecycle
contracts do not exist.

## Consequences

### Positive

- References remain stable across ordinary metadata changes.
- Duplicate and supersession history can be preserved.
- Downstream provenance can point to durable identities.

### Negative

- Mistaken allocations require explicit correction or supersession rather than
  reuse.
- Repository-level uniqueness and referential-integrity validation is needed.

### Risks

- The semantic-looking source prefix may be mistaken for permanent domain
  ownership.
- Format validation alone may conceal duplicate or dangling identifiers.

## Implementation implications

`config/project.yaml` defines `AI-ADOPTION`;
`config/source-types.yaml` defines `SROOT-0001` and source prefixes;
`sources/catalogue.yaml` contains implemented source IDs; and
`schemas/sources.yaml` validates their format. Stage 9 adds the proposed
knowledge prefixes in `config/knowledge-types.yaml`, object schemas, templates,
and `scripts/validate_knowledge.py`, which checks production knowledge ID
format, global uniqueness, reserved IDs, and explicit references. The initial
production knowledge set is empty.

The source catalogue still lacks a repository-level uniqueness and
referential-integrity validator, and non-reuse across Git history is not
automated. Future object types need separate ADRs or approved schemas before
allocation.

## Validation

For knowledge, run `python scripts/validate_schemas.py` and
`python scripts/validate_knowledge.py` to check schema conformance, current-tree
format, uniqueness, reserved IDs, and references. For sources, validate source
ID format, uniqueness, configured-prefix membership, `duplicate_of`
references, and non-reuse across history. The source schema checks format only;
those repository-level source checks are not currently automated.

## References

- [Identifier rules](../../docs/reference/identifiers.md)
- [Source configuration](../../config/source-types.yaml)
- [Canonical source catalogue](../../sources/catalogue.yaml)
- [Canonical catalogue schema](../../schemas/sources.yaml)
- [Change management](../../docs/governance/change-management.md)
- [Knowledge identifier rules](../../docs/reference/knowledge-identifiers.md)
- [Knowledge type configuration](../../config/knowledge-types.yaml)
- [ADR-0002](0002-canonical-source-catalogue-schema.md)

## Post-acceptance implementation note — 2026-08-02

Accepted ADR 0010 subsequently approved `AUTH-NNNNNN` and `RUN-NNNNNN`
contracts and repository validation. Fifty-seven authorization IDs are
allocated, and `RUN-000001` is the first processing-run ID. This note updates
implementation status without changing this ADR's decision.
