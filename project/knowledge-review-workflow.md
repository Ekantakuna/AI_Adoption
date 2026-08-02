# Knowledge review workflow

> Approved by Maksim Zakharenkau on 2026-08-02. See the
> [Stage 9 approval record](status/stage-09-approval.md).

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
6. Run the validator and record any downstream objects requiring review.

Reviewing a knowledge object does not automatically approve an assessment,
organizational decision, report claim, or presentation. Each downstream layer
retains its own human-review boundary. Automated impact traversal is still
planned, so maintainers must search explicit IDs manually after a change.
