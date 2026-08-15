# Knowledge review workflow

> Approved by Maksim Zakharenkau on 2026-08-02. See the
> [Stage 9 approval record](status/stage-09-approval.md).
>
> MZ reviewed and approved the Stage 11 synchronization below on 2026-08-15,
> including its bounded explicit-reference traversal and manual-review and
> non-automation boundaries.

## Roles

- **Creator:** prepares a classified, traceable record and cannot self-approve
  an AI-generated record.
- **Reviewer:** checks provenance, source fidelity where authorized,
  interpretation, conflicts, classification, and intended use.
- **Maintainer:** protects IDs and controlled configuration and runs repository
  integrity checks.

## Lifecycle

`draft` → `needs_review` → `under_review` → `verified` or `approved`.
Review may instead produce `rejected`; later retained records may become
`deprecated`. `verified` means factual/evidence checking; `approved` means
acceptance for the record's stated use. Neither state is inferred from Git.

## Procedure

1. The creator validates the record and changes `draft` to `needs_review`.
2. An authorized reviewer records `under_review` when work begins.
3. The reviewer checks identity, provenance, locator, processing route,
   evidence coverage, classification, conflicts, and downstream implications.
4. Requested changes return to a non-authoritative status without changing the
   stable ID. Conflicting claims remain separately attributed.
5. For `verified` or `approved`, an authorized human adds `reviewer.name` and
   `reviewer.reviewed_at`. Preserve `origin: ai` when applicable; origin records
   authorship and does not change when a human promotes the review status.
6. Run the knowledge and relationship/impact validators. For each changed
   canonical ID, run bounded `impact` traversal and record affected IDs,
   unresolved conflicts, warnings, alternate paths, cycles, and truncation that
   may require review.

Reviewing a knowledge object does not automatically approve an assessment,
organizational decision, report claim, or presentation. Each downstream layer
retains its own human-review boundary. Stage 11 implements bounded, read-only
impact traversal over explicit canonical references; it does not infer semantic
relationships, determine that affected content is stale, alter review states,
enforce re-review, or regenerate downstream objects. Maintainers must evaluate
the reported impact and record any required review manually. See the
[relationship traversal operation](../docs/operations/traversing-knowledge-relationships.md).
