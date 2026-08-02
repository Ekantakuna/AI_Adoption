# Implemented use-cases ingestion status

- Status: semantic drafts created; human evidence and use-case review required
- Date: 2026-08-02
- Review owner: Maksim Zakharenkau
- Approved by: Maksim Zakharenkau
- Approval date: 2026-08-02
- Source root: `/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`
- Source-body access for new files: controlled local extraction through verified runs

## Inventory result

Metadata comparison found three new non-ignored files. Four other implemented-
use-case files in the same tree were already catalogued as `SRC-UC-000001`–
`000003` and `SRC-UC-000011`.

| Source ID | Relative path | Size | SHA-256 |
| --- | --- | ---: | --- |
| `SRC-UC-000012` | `current_state/implemented_use_cases/customer_care/callcenter_chatbot /chatbot_2024.pptx` | 2,041,174 | `96dddca7658c182f5de39fd56be588ca2e7c00b07cf2a8036c706bf75d47c53b` |
| `SRC-UC-000013` | `current_state/implemented_use_cases/customer_care/speech_analytics/ai_speech.pptx` | 554,818 | `3b4a4aea4b1cd64521fa1464e592b7a19a90d2cdb0822efb97c5308ed296b635` |
| `SRC-UC-000014` | `current_state/implemented_use_cases/sales/life_registration/Life Registration - 2026 v1.pptx` | 9,606,553 | `b154261861217db978fd4562134bbfe5b965712147538199df0fe3f94f308bc5` |

The catalogue and current-state manifest preserve the trailing space in the
`callcenter_chatbot ` directory rather than silently renaming the source.

## Approved access decision

Classify all three sources as `internal`, consistent with the existing
implemented-use-case sources in this directory. Set them to
`approved_for_processing` using `local_only`, `approved_local`, and the approved
`pptx_xml_reader`. Allocate `AUTH-000058`–`AUTH-000060` in source-ID order.

The tool reads visible slide XML text in numeric slide order and produces a
private, slide-labelled derivative. It verifies source/output hashes and path
boundaries. It does not capture speaker notes, chart workbooks, alt text, or
text embedded only in images; evidence and semantic models must not claim
coverage of those unavailable elements.

## Approval checkpoint completed

Maksim Zakharenkau explicitly approved:

1. the `internal` classification for `SRC-UC-000012`–`000014`;
2. their transition to `approved_for_processing`;
3. `local_only` / `approved_local` handling;
4. the `pptx_xml_reader` configuration and schema enum additions; and
5. allocation of `AUTH-000058`–`AUTH-000060`.

The approval authorized private slide-labelled extraction and AI-origin
`needs_review` evidence/use-case drafting. No source claim becomes authoritative
without separate human evidence and knowledge review.

## Extraction result

`RUN-000002`–`RUN-000004` succeeded and created private ignored slide-text
derivatives of 5,988, 1,919, and 9,674 bytes respectively. Source and output
hashes were recorded in `sources/processing-runs.yaml`. Maksim Zakharenkau
subsequently verified all three runs, making them eligible to support draft
evidence.

## Run verification

Maksim Zakharenkau verified `RUN-000002`–`RUN-000004` on 2026-08-02 based on
their authorizations, matching source hashes, private extraction, output hashes,
and local-output validation. This verification covers processing provenance
only and does not approve source claims or substantive conclusions.

## Approval decision

Maksim Zakharenkau approved all five requested items on 2026-08-02 and
authorized controlled private extraction followed by AI-origin `needs_review`
evidence and use-case drafts. The approval does not approve source claims or
substantive conclusions.

## Logical and semantic structures

| Source | Authorization | Run | Atomic evidence | Semantic use case |
| --- | --- | --- | --- | --- |
| `SRC-UC-000012` | `AUTH-000058` | `RUN-000002` | `EVID-000002`–`000003` | `USECASE-000001` — Smart Chat Bot |
| `SRC-UC-000013` | `AUTH-000059` | `RUN-000003` | `EVID-000004`–`000006` | `USECASE-000002` — AI Speech Analytics Assistant |
| `SRC-UC-000014` | `AUTH-000060` | `RUN-000004` | `EVID-000007`–`000009` | `USECASE-000003` — Life Registration |

The evidence records use slide and derivative-line locators, inherit internal
classification, use medium confidence, preserve source attribution for metrics,
and remain `needs_review`. The three use-case records model problem and outcome
and cite only their corresponding evidence. They are also AI-origin
`needs_review` drafts and do not establish implementation or organizational
approval.

## Coverage limitations

The semantic pass covers visible slide XML text only. It excludes speaker
notes, chart workbooks, alt text, and text embedded exclusively in images.
Reported metrics—including the 51% chatbot closure rate and five-to-eight-minute
SIM/eSIM connection time—are source claims, not independent measurements.
