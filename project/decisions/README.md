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
| [0001](0001-repository-operating-model.md) | Repository operating model | proposed | Eight-layer target architecture; downstream capabilities remain partial, planned, or absent |
| [0002](0002-canonical-source-catalogue-schema.md) | Canonical source catalogue schema | approved | Catalogue schema is approved; executable validation is not part of this record |
| [0003](ADR-0003-source-assets-outside-git.md) | Source assets outside Git and metadata-only catalogue | proposed | Storage boundary is documented; extraction and enforcement remain incomplete |
| [0004](ADR-0004-markdown-and-yaml-canonical-formats.md) | Markdown and YAML canonical formats | proposed | Formats are in use; object schemas and validators remain mostly absent |
| [0005](ADR-0005-stable-identifiers.md) | Stable identifiers | proposed | Project, source-root, and source IDs exist; downstream identifiers are unapproved |
| [0006](ADR-0006-separate-evidence-and-knowledge.md) | Evidence and knowledge separation | proposed | Boundary is documented; atomic evidence and knowledge contracts are planned |
| [0007](ADR-0007-human-review-for-authority.md) | Human review for authority | proposed | Human authority boundary is documented; workflow enforcement is absent |
| [0008](ADR-0008-publications-are-derivatives.md) | Publications as derivatives | proposed | Source-of-truth boundary is documented; generation pipeline remains planned |
| [0009](ADR-0009-documentation-is-part-of-implementation.md) | Documentation as implementation | proposed | Agent obligation is documented; automated completeness checks are absent |
