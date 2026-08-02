---
id: ADR-0008
title: Derive publications from canonical reviewed content
status: accepted
date: 2026-07-30
reviewed_by: Maksim Zakharenkau
reviewed_at: 2026-08-02
decision_owners:
  - repository maintainers
  - authorized human reviewers
supersedes:
superseded_by:
---

# ADR-0008 — Derive publications from canonical reviewed content

## Context

Repository guidance defines publications and generated outputs as downstream
derivatives of canonical project content. Reports, presentations, and websites
must not become the only location of evidence, knowledge, approval, or
decisions.

This canonical-versus-derivative boundary is already operative. Maksim
Zakharenkau accepted this AI-authored ADR on 2026-08-02. The structured
knowledge models exist as an empty approved framework. Audience
configuration, publication assembler, renderer, traceability validator, and
release workflow are planned or absent, so this ADR does not claim a working
publication pipeline.

## Decision

Build audience publications, presentations, and website outputs from reviewed
canonical Markdown or approved schema-valid structured records. Preserve links
to the upstream claims, evidence, approvals, and decisions.

Treat rendered and audience-shaped outputs as replaceable derivatives. Update a
canonical input or generator rather than making a generated output the sole
maintained source of a material claim.

Require human approval for publication-ready executive claims and audience
release.

## Rationale

Audience outputs select, summarize, and reformat information. Keeping their
authority upstream preserves reusable knowledge, provenance, and consistent
correction across output formats.

## Alternatives considered

### Author reports and decks as the only canonical records

Not selected because evidence and decisions would be duplicated or trapped in
audience-specific artifacts.

### Allow generated outputs to introduce new claims

Not selected because those claims would bypass evidence, knowledge, and review
controls.

### Implement a publication generator as part of this decision record

Not selected because no audience, template, identifier, or validation contract
is approved, and this task records existing decisions rather than adding
capabilities.

## Consequences

### Positive

- Corrections can flow from one reviewed upstream record to multiple outputs.
- Audience outputs remain traceable and replaceable.
- Evidence and approval records retain independent identities.

### Negative

- Publication tooling must carry claim-level provenance and review state.
- Direct manual edits to rendered outputs cannot serve as the lasting fix.

### Risks

- Until generation exists, manually assembled output may drift from canonical
  inputs.
- “Derived” may be mistaken for “approved” without a separate release gate.

## Implementation implications

`publications/`, `presentations/`, and `website/` currently contain only
scaffolding and boundary documentation. `config/audiences.yaml` is empty, and no
generator or publication validator exists.

Future implementation requires approved identifiers, audience definitions,
templates, inclusion rules, classification checks, provenance validation,
review metadata, reproducible commands, and tests.

## Validation

When outputs exist, verify that material claims resolve to reviewed canonical
inputs, classification permits the audience, required approvals are recorded,
and generated artifacts can be rebuilt. These checks are not currently
automated because the publication pipeline is not implemented.

## References

- [Publication directory contract](../../publications/README.md)
- [Presentation directory contract](../../presentations/README.md)
- [Publication pipeline](../../docs/architecture/publication-pipeline.md)
- [Change management](../../docs/governance/change-management.md)
- [Repository architecture](../../ARCHITECTURE.md)
- [Repository baseline](../status/repository-baseline.md)
