# Source-state reconciliation proposal

- Status: approved and implemented
- Proposed by: Codex
- Review owner: Maksim Zakharenkau
- Proposal date: 2026-08-02
- Approved by: Maksim Zakharenkau
- Approval date: 2026-08-02
- Source-body access: none

## Purpose

Resolve the conflict among `sources/catalogue.yaml`, the legacy source register,
manifests, and historical status reports without treating AI classifications or
unreproducible extraction claims as authoritative.

All 58 stable source IDs and hashes align across the canonical catalogue and
legacy register. The conflict concerns 57 classifications and 56 processing
states. The later classification records name `codex` as reviewer, and route
records mostly name only `user`; this proposal therefore requires a new,
identified human approval rather than copying those review claims.

## Proposed classification decision

Approve the following classification groups after metadata review. These are
the exact 58 source IDs; no source body was inspected to prepare the proposal.

### Public — 32

`SRC-AGT-000001`, `SRC-AGT-000002`, `SRC-AGT-000003`, `SRC-AGT-000004`,
`SRC-AGT-000005`, `SRC-AGT-000006`, `SRC-AGT-000007`, `SRC-GLO-000001`,
`SRC-GOV-000003`, `SRC-GOV-000004`, `SRC-MAT-000001`, `SRC-MIS-000001`,
`SRC-MIS-000002`, `SRC-MIS-000003`, `SRC-ORG-000001`, `SRC-ORG-000004`,
`SRC-PRM-000002`, `SRC-PRM-000004`, `SRC-SCO-000001`, `SRC-SEC-000001`,
`SRC-SEC-000002`, `SRC-SEC-000003`, `SRC-UC-000004`, `SRC-UC-000005`,
`SRC-UC-000006`, `SRC-UC-000007`, `SRC-UC-000008`, `SRC-UC-000009`,
`SRC-VIS-000005`, `SRC-VIS-000006`, `SRC-VIS-000007`, `SRC-VIS-000008`.

### Internal — 21

`SRC-GOV-000001`, `SRC-GOV-000002`, `SRC-MIS-000004`, `SRC-MIS-000005`,
`SRC-ORG-000002`, `SRC-ORG-000003`, `SRC-ORG-000005`, `SRC-ORG-000006`,
`SRC-PRE-000001`, `SRC-PRE-000002`, `SRC-PRM-000001`, `SRC-PRM-000003`,
`SRC-UC-000001`, `SRC-UC-000002`, `SRC-UC-000003`, `SRC-UC-000010`,
`SRC-UC-000011`, `SRC-VIS-000001`, `SRC-VIS-000002`, `SRC-VIS-000003`,
`SRC-VIS-000004`.

### Restricted — 5

`SRC-AGT-000008`, `SRC-GOV-000005`, `SRC-GOV-000006`, `SRC-GOV-000007`,
`SRC-RSK-000001`.

## Proposed processing state

Set 57 sources to `approved_for_processing` for a fresh, controlled run. Do not
copy the 32 historical `extracted` claims into the canonical catalogue because
the derivative corpus and run provenance are not currently reproducible.

Keep `SRC-VIS-000005` as `blocked`; its Pages format has no approved extraction
tool in the proposed configuration.

## Proposed route, tool, and environment authorization

Use `local_only` for every approved source. This is deliberately narrower than
the historical `external_processing_approved` claims and does not authorize any
external AI or cloud service. Allocate `AUTH-000001` through `AUTH-000057` in
source-ID sort order, excluding the blocked Pages source.

- `pdftotext_local` for 34 PDFs: `SRC-AGT-000001`–`SRC-AGT-000008`,
  `SRC-GLO-000001`, `SRC-GOV-000003`, `SRC-GOV-000004`, `SRC-GOV-000006`,
  `SRC-MAT-000001`, `SRC-MIS-000001`–`SRC-MIS-000003`, `SRC-ORG-000001`,
  `SRC-ORG-000004`, `SRC-PRM-000002`, `SRC-PRM-000004`, `SRC-RSK-000001`,
  `SRC-SCO-000001`, `SRC-SEC-000001`–`SRC-SEC-000003`,
  `SRC-UC-000004`–`SRC-UC-000009`, and `SRC-VIS-000006`–`SRC-VIS-000008`.
- `textutil_local` for `SRC-GOV-000005`, `SRC-GOV-000007`, and
  `SRC-UC-000011`.
- `repository_text_reader` for `SRC-GOV-000001`, `SRC-GOV-000002`,
  `SRC-MIS-000004`, `SRC-MIS-000005`, `SRC-ORG-000002`, `SRC-ORG-000003`,
  `SRC-ORG-000005`, `SRC-ORG-000006`, `SRC-PRE-000001`, `SRC-PRE-000002`,
  `SRC-PRM-000001`, `SRC-PRM-000003`, `SRC-UC-000010`, `SRC-VIS-000001`,
  `SRC-VIS-000002`, `SRC-VIS-000003`, and `SRC-VIS-000004`.
- `human_visual_review` for `SRC-UC-000001`, `SRC-UC-000002`, and
  `SRC-UC-000003`.

Use `approved_local` for public and internal sources. Use `approved_on_prem` for
the five restricted sources. Approval therefore includes confirmation that the
environment used for restricted processing is an approved on-premises
environment; automation cannot establish that fact.

## Provenance and retained conflict

The basis is repository metadata in `registers/sources.yaml`,
`sources/manifests/*.yaml`, `project/status/source-access-report.md`, and the
canonical IDs/hashes in `sources/catalogue.yaml`. Historical classifications,
routes, and extraction claims remain preserved in their original records. This
proposal does not rewrite those records or claim that historical extraction is
current.

## Effect of approval

After explicit approval, update only canonical classification and processing
state fields, populate the authorization register with reviewer identity and
date, approve the source-processing control policy/configuration and ADR 0010,
and run all validators. Source bodies remain unopened until those changes pass.

Approval unblocks controlled new runs; it does not create successful runs,
production evidence, or approval of source content.

## Implementation result

The approved classification and processing-state changes were applied to
`sources/catalogue.yaml`. `AUTH-000001` through `AUTH-000057` were allocated in
source-ID order, excluding blocked `SRC-VIS-000005`, and recorded in
`sources/processing-authorizations.yaml`. The historical records remain
unchanged. Validation passed with 58 sources, 57 approved authorizations, zero
runs, and zero errors. No source body was opened.
