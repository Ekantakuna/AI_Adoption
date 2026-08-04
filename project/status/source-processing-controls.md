# Source-processing controls status

- Status: partial; controls approved and authorization gate operational
- Date: 2026-08-02
- Review owner: Maksim Zakharenkau
- Source-body access during implementation: none

## Implemented

- Proposed controlled route, tool, environment, authorization, and run values
  are defined in `config/source-processing.yaml`.
- Draft 2020-12 authorization and run contracts are defined in
  `schemas/source-processing-authorization.schema.yaml` and
  `schemas/processing-run.schema.yaml`.
- Empty production registers, non-production templates, cross-record
  validation, and synthetic tests are present under `sources/`, `scripts/`, and
  `tests/`.
- `scripts/extract_text.py` can read authorized text/HTML sources only after the
  whole source-processing repository state passes validation. It refuses output
  overwrite and reports a derivative hash.
- Production evidence must resolve to a successful processing run reviewed as
  `verified` or `approved`.

## Approved activation

- Maksim Zakharenkau approved the policy, configuration, schemas, ADR 0010, and
  exact reconciliation matrix on 2026-08-02.
- The catalogue contains 32 public, 21 internal, and 5 restricted sources; 57
  are `approved_for_processing` and `SRC-VIS-000005` remains blocked.
- `sources/processing-authorizations.yaml` contains 57 approved, identified,
  hash-compatible route/tool/environment authorizations.
- `scripts/validate_source_processing.py` passes and is enabled in CI.

## Remaining operational boundary

- `sources/processing-runs.yaml` contains one technically successful pilot run,
  `RUN-000001`, verified by Maksim Zakharenkau.
- One authorized internal source body was processed by the controlled reader
  and its derivative remains in the ignored private extraction area. No
  substantive knowledge was extracted; one AI-origin atomic evidence statement
  is human-verified, but no broader knowledge or organizational claim exists.
- PDF, office-document, and image tool execution is configured but not wrapped
  by repository commands. The Pages source has no approved tool.
- A synthetic-tested `pptx_xml_reader` is proposed for three newly catalogued
  presentation sources; tool and per-source approval remain required before
  their bodies may be opened.

## Processing sequence

1. Create one planned run at a time; process only its authorized body, record
   output provenance, and obtain human run review before creating evidence.
2. Keep restricted derivatives in the approved on-premises environment and
   outside Git unless a separately reviewed storage decision permits them.
3. Create production evidence only from a successful run reviewed as
   `verified` or `approved`.

## Validation snapshot

After the pilot, standards-based validation covers 15 schemas, 58 catalogue
records, 57 authorizations, and one verified, evidence-eligible run. Current
validation results are recorded in
`source-processing-pilot-run-000001.md`.
