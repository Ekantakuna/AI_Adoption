# Source-processing approval record

- Decision: approved and activated
- Reviewer: Maksim Zakharenkau
- Reviewer role: repository owner and developer
- Approval date: 2026-08-02
- Recorded by: Codex from the reviewer's explicit confirmation
- Source-body access during reconciliation: none

## Approved scope

Maksim Zakharenkau approved the complete matrix in
`project/status/source-state-reconciliation-proposal.md`, confirmed
`approved_on_prem` for its five restricted sources, and approved:

- `project/source-processing-control-policy.md`;
- `config/source-processing.yaml`;
- `schemas/source-processing-authorization.schema.yaml`;
- `schemas/processing-run.schema.yaml`; and
- ADR 0010.

He authorized the exact catalogue classification/processing-state updates and
authorization-register population described in the proposal.

## Implemented decision

- All 58 stable source IDs and hashes were preserved.
- Canonical classifications are 32 public, 21 internal, and 5 restricted.
- Fifty-seven sources are `approved_for_processing`; `SRC-VIS-000005` remains
  blocked because no Pages tool is approved.
- `AUTH-000001` through `AUTH-000057` bind the processable sources to
  `local_only`, their approved tool, identified reviewer, and either
  `approved_local` or `approved_on_prem`.
- Historical `extracted` claims were not copied into the canonical catalogue.
  Legacy records and their conflicts remain preserved.

## Authority boundary

This decision authorizes controlled fresh processing runs. It does not claim
that processing occurred, approve any source content, create evidence, or
approve substantive knowledge. Each execution still requires a stable run
record, exact source hash, output provenance, and human run review before it can
support production evidence.
