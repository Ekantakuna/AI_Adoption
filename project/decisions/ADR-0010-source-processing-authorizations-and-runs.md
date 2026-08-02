---
id: ADR-0010
title: Require explicit source processing authorizations and run records
status: accepted
date: 2026-08-02
reviewed_by: Maksim Zakharenkau
reviewed_at: 2026-08-02
decision_owners:
  - repository maintainers
  - authorized human reviewers
supersedes:
superseded_by:
---

# ADR-0010 — Require explicit source processing authorizations and run records

## Context

The canonical catalogue and later source records disagree about classification
and processing state. Later records identify AI classification and ambiguous
route reviewers, while historical extraction outputs and reproducible run
records are absent. Evidence schemas already require `RUN-NNNNNN`, but no run
identity contract exists.

Maksim Zakharenkau accepted this decision on 2026-08-02 together with the
exact source-state reconciliation and confirmed the approved on-premises
environment for the five restricted sources.

## Decision

Keep canonical source classification in `sources/catalogue.yaml`. Store current
human-approved route, tool, and environment decisions in
`sources/processing-authorizations.yaml`. Record every execution in
`sources/processing-runs.yaml` using a stable run ID and the exact source hash.

Do not infer current extraction success from a historical report or manifest.
Only reviewed successful runs may support production evidence.

## Rationale

Separate authorization from execution so a route decision is reviewable,
revocable, and reusable without overwriting run history. Binding runs to source
hashes prevents evidence from silently surviving a changed source.

## Alternatives considered

### Copy legacy extracted states into the catalogue

Not selected because current derivatives, tools, and run provenance are not
available to reproduce those claims.

### Add route and run history to each catalogue record

Not selected because repeating execution history inside source metadata would
blur inventory, authorization, and processing lifecycles.

## Consequences

### Positive

- Source access decisions identify a human reviewer and exact scope.
- Every evidence record can resolve its processing run.
- Revocation and failed runs remain auditable.

### Negative

- Two additional controlled registers and identifiers must be maintained.
- Existing sources require an explicit authorization migration.

### Risks

- A valid authorization may be mistaken for successful extraction.
- Environment labels require organizational verification outside automation.

## Implementation implications

The source-processing control implementation adds route/tool configuration, authorization and run
schemas/registers/templates, repository validation, operating documentation,
and evidence-to-run integrity checks. The exact approved reconciliation matrix
is implemented in the canonical catalogue and authorization register.

## Validation

Run the schema, source-processing, and knowledge validators plus the unit test
suite. Human review remains mandatory for classifications, authorizations, and
run verification.

## References

- [Source management policy](../source-management-policy.md)
- [Source processing control policy](../source-processing-control-policy.md)
- [Stage 9 approval](../status/stage-09-approval.md)
- [Source-processing approval](../status/source-processing-approval.md)
- [Repository baseline](../status/repository-baseline.md)
