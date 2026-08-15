# Architecture Decision Records

This directory records significant architectural and operating decisions for the
AI Adoption repository.

An ADR is required when a change materially affects:

- repository architecture
- canonical data format
- identifiers
- evidence handling
- knowledge representation
- review and approval
- automation boundaries
- publication generation
- presentation generation
- source-of-truth decisions

## Naming

Use:

`ADR-NNNN-short-title.md`

Example:

`ADR-0001-markdown-and-yaml-as-canonical-formats.md`

The pre-existing `0001-...` and `0002-...` filenames are retained as stable
records. New ADRs follow the `ADR-NNNN-...` convention and continue the same
number sequence. New ADRs use the front matter and section structure in
`template.md`; the template itself remains unchanged.

## Statuses

- proposed
- accepted
- superseded
- deprecated
- rejected

## Rule

Accepted ADRs must not be silently rewritten to represent a later decision.
Create a new ADR and mark the previous decision as superseded.

AI-authored ADRs remain `proposed` until an authorized human reviewer records
approval. An ADR may document an already-operative rule while the new decision
record itself awaits review.

## Index

| ADR | Decision | Record status | Implementation distinction |
| --- | --- | --- | --- |
| [0001](0001-repository-operating-model.md) | Repository operating model | accepted | Eight-layer target architecture; downstream capabilities remain partial, planned, or absent |
| [0002](0002-canonical-source-catalogue-schema.md) | Canonical source catalogue schema | approved | Catalogue schema is approved and executable Draft 2020-12 validation is configured |
| [0003](ADR-0003-source-assets-outside-git.md) | Source assets outside Git and metadata-only catalogue | accepted | Operative storage boundary; extraction and enforcement remain incomplete |
| [0004](ADR-0004-markdown-and-yaml-canonical-formats.md) | Markdown and YAML canonical formats | accepted | Formats are in use; not every tracked file is authoritative or schema-valid |
| [0005](ADR-0005-stable-identifiers.md) | Stable identifiers | accepted | Implemented for project, source root, sources, and the empty Stage 9 knowledge framework |
| [0006](ADR-0006-separate-evidence-and-knowledge.md) | Evidence and knowledge separation | accepted | Approved boundary; empty Stage 9 schemas, templates, workflow, and validator implemented |
| [0007](ADR-0007-human-review-for-authority.md) | Human review for authority | accepted | Approved review rule; Stage 9 knowledge reviewer gates implemented, broader automation absent |
| [0008](ADR-0008-publications-are-derivatives.md) | Publications as derivatives | accepted | Operative source-of-truth boundary; generation pipeline remains planned |
| [0009](ADR-0009-documentation-is-part-of-implementation.md) | Documentation as implementation | accepted | Operative agent obligation; automated documentation checks remain absent |
| [0010](ADR-0010-source-processing-authorizations-and-runs.md) | Explicit source-processing authorizations and run records | accepted | Approved contracts, 57 authorizations, and one successful pilot awaiting review; no evidence |
| [0011](ADR-0011-explicit-relationship-traversal-contract.md) | Explicit relationship traversal without replacing canonical records | accepted | Traversal contract approved by MZ on 2026-08-14 and implemented through human-approved Stage 11 |
| [0012](ADR-0012-assessment-scoring-and-audience-controls.md) | Control assessment scoring and audience use before Stage 12 | accepted | Framework, identifiers, unscored-first mode, `AUD-000001`, and ownership assignments approved by MZ on 2026-08-15; configuration remains unimplemented |
