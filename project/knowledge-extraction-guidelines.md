# Knowledge extraction guidelines

> Approved by Maksim Zakharenkau on 2026-08-02. See the
> [Stage 9 approval record](status/stage-09-approval.md). Source processing
> was subsequently unblocked through the approved reconciliation and
> source-processing controls recorded in
> [source-processing approval](status/source-processing-approval.md).

## Preconditions

Do not open a source body unless its stable source ID, classification, handling
requirements, processing route, and extraction tool have been recorded and
reviewed. Original sources stay outside Git and remain unchanged. Record the
processing run before promoting output. The approved run contract and register
are `schemas/processing-run.schema.yaml` and `sources/processing-runs.yaml`.

## From processing output to evidence

1. Work only within the approved handling route and retain the source ID.
2. Separate processing output from evidence. Raw extracted text is not an
   `EVID` record and must not be committed merely because extraction succeeded.
3. Create one atomic statement per evidence record. Preserve qualifiers,
   uncertainty, timeframe, and the source's meaning.
4. Add the exact source locator and processing-run ID; never invent a page,
   section, identifier, citation, or missing claim.
5. Assign classification inherited from the source inputs and a controlled
   confidence describing support quality, not truth or approval.
6. Set AI-created records to `draft` or `needs_review` and submit them for human
   verification before authoritative use.
7. Preserve conflicting statements as separate attributed evidence records;
   connect or assess the conflict later rather than normalizing it silently.

Evidence is the upstream input for interpreted terms, concepts, frameworks,
metrics, risks, trends, use cases, decisions, and relationships. Every
knowledge object cites at least one existing `EVID` ID. Evidence linked to an
assumption establishes context; it does not turn the assumption into a fact.

## Prohibited actions

Do not copy source documents into Git, change source catalogue IDs, claim that
metadata authorizes content access, combine several independent claims into one
evidence statement, add unsupported interpretation to an evidence record, or
mark AI-created content verified or approved.

## Validation and limitations

Run `python scripts/validate_schemas.py` and
`python scripts/validate_source_processing.py` and
`python scripts/validate_knowledge.py` after creating records. They check
schema conformance and cross-references but cannot determine whether a
statement is a faithful extraction, whether a handling decision was authorized,
or whether a source claim is true. Processing-run existence and review state
are checked structurally; source fidelity and semantic truth require human
review.
