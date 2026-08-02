---
id: ADR-0006
title: Separate evidence from interpreted knowledge
status: proposed
date: 2026-07-30
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
directory model separates source inventory from knowledge. Atomic evidence and
interpreted-knowledge contracts remain to be approved and implemented.

The separation rule is proposed. Approval of the model would not create or
approve production evidence.

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
`knowledge/` holds provisional knowledge material; and policies in `project/`
define the proposed promotion boundary. Existing root-level knowledge notes
remain provisional synthesis documents, not atomic evidence records. Atomic
schemas, identifiers, templates, workflow, and cross-reference validation are
not yet implemented.

## Validation

Review each proposed record's object type, source locator, provenance,
classification, and review label when a record contract exists. Automated
knowledge validation is not currently available and cannot confirm source
fidelity, reviewer authority, or semantic truth.

## References

- [Information objects](../../docs/concepts/information-objects.md)
- [Information-handling rules](../information-handling.md)
- [Source management policy](../source-management-policy.md)
- [Knowledge directory contract](../../knowledge/README.md)
- [Repository baseline](../status/repository-baseline.md)
- [Accepted operating model](0001-repository-operating-model.md)
