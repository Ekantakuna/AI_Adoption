---
id: ADR-0006
title: Separate evidence from interpreted knowledge
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

# ADR-0006 — Separate evidence from interpreted knowledge

## Context

Repository policy distinguishes original source assets, metadata, extraction,
evidence, and interpreted knowledge. It prohibits treating extraction output as
authoritative evidence or approved knowledge merely because it exists. The
directory model separates source inventory from knowledge. Stage 9 adds an
empty controlled model for atomic evidence and interpreted knowledge without
performing source-content extraction.

The separation rule is already operative. Maksim Zakharenkau accepted this
AI-authored ADR and the Stage 9 framework contracts on 2026-08-02. Approval of
the model does not create or approve production evidence.

## Decision

Keep these lifecycle boundaries distinct:

1. an original source asset is immutable external evidence;
2. source metadata is administrative inventory, not source content;
3. extraction is a derivative representation, not reviewed evidence;
4. evidence is an attributable observation or statement;
5. knowledge is an interpreted claim, concept, assumption, decision,
   definition, or relationship supported by evidence.

Do not promote an object across these boundaries implicitly. Preserve source
locators, classification, provenance, review state, and unresolved conflicts.

## Rationale

The objects have different authority, handling, review, and change lifecycles.
Conflating them would allow tool output or interpretation to appear as fact and
would weaken traceability.

## Alternatives considered

### Treat extraction as evidence automatically

Not selected because extraction can contain tool errors, missing context, or
classification constraints and has not passed evidence review.

### Store evidence and interpretation in one undifferentiated record

Not selected because reviewers could not reliably distinguish what a source
states from what the project infers.

### Treat synthesis notes as atomic evidence

Not selected because current synthesis notes combine interpretation and source
references and do not implement an atomic-evidence contract.

## Consequences

### Positive

- Claims can retain a clear chain back to attributable source material.
- Review can address extraction accuracy separately from interpretation.
- Conflicting source statements can remain visible.

### Negative

- More object types and review transitions are required.
- Downstream work cannot assume that available extraction is approved
  knowledge.

### Risks

- Contributors may mistake an approved empty framework for approved production
  content or a functioning extraction pipeline.
- Users may infer operational evidence management from directory scaffolding.

## Implementation implications

`sources/` holds metadata and controlled derivatives;
`knowledge/` contains the controlled empty evidence and knowledge framework;
and policies in `project/` define the promotion boundary. Existing root-level
knowledge notes remain provisional synthesis documents, not atomic evidence
records. Stage 9 implements approved evidence and knowledge schemas,
six-digit identifiers, templates, a review workflow, and cross-reference
validation. It does not implement a processing-run register or approve any
production record.

## Validation

Run `python scripts/validate_schemas.py` and
`python scripts/validate_knowledge.py`, then review each record's object type,
source locator, provenance, classification, and review label. The validators
check schema, structural, and reference boundaries but cannot confirm source
fidelity, processing-run existence, reviewer authority, or semantic truth.

## References

- [Information objects](../../docs/concepts/information-objects.md)
- [Information-handling rules](../information-handling.md)
- [Source management policy](../source-management-policy.md)
- [Knowledge directory contract](../../knowledge/README.md)
- [Knowledge management policy](../knowledge-management-policy.md)
- [Knowledge review workflow](../knowledge-review-workflow.md)
- [Repository baseline](../status/repository-baseline.md)
- [Accepted operating model](0001-repository-operating-model.md)

## Post-acceptance implementation note — 2026-08-02

Accepted ADR 0010 subsequently added the approved processing-run contract,
empty run register, source-processing validator, and evidence-to-reviewed-run
integrity check. No successful run or production evidence exists. This note
updates implementation status without changing this ADR's decision.
