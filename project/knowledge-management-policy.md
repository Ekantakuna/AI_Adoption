# Knowledge management policy

> Approved by Maksim Zakharenkau on 2026-08-02. See the
> [Stage 9 approval record](status/stage-09-approval.md).

## Purpose and scope

This policy controls Git-trackable atomic evidence and knowledge records under
`knowledge/`. It preserves the boundary between source metadata, extraction,
evidence, interpretation, project governance, assessments, and publications.
Generated material inherits the highest classification of its inputs and may be
stored only on an approved handling route.

## Canonical objects and boundaries

- `sources/catalogue.yaml` remains the source-metadata authority; knowledge
  records must not duplicate or amend it.
- An extraction is a processing derivative. An `EVID` record is one attributable
  statement promoted from an approved run with a source ID and precise locator.
- Terms, concepts, frameworks, metrics, risks, trends, use cases, knowledge
  decisions, and relationships are interpretations and cite `EVID` IDs.
- `ASSUMPTION` records cite the evidence context that exposed the assumption but
  remain explicitly unverified and must never be presented as facts.
- Architectural and repository-governance decisions remain in
  `project/decisions/`; `knowledge/decisions/` must not duplicate them.
- Assessments, reports, and presentations are downstream interpretations or
  derivatives and do not replace canonical evidence or knowledge.

The configured types, prefixes, directories, formats, and evidence requirements
are approved controls in `config/knowledge-types.yaml`. Object contracts are in
`schemas/*.schema.yaml`, including the contextual `REF` contract.

## Identity, lifecycle, and relationships

Production IDs use `<PREFIX>-<six digits>`, are globally unique across the
knowledge layer, and are never reused or renumbered. `000000` is reserved for
templates. Records follow `config/review-statuses.yaml`; AI-origin records may
initially use only `draft` or `needs_review`. `verified` and `approved` require
the reviewer name and review date. Rejection or deprecation preserves the ID and
audit history.

Relationships are explicit `REL` records between two existing non-evidence,
non-relationship knowledge-object IDs. A relationship cites evidence and must
not silently resolve contradictions or supersession.

## Ownership and operation

Record creators are responsible for classification, provenance, uniqueness,
schema-valid structure, and submitting the record for review. Authorized human
reviewers own verification and approval. Repository maintainers own controlled
configuration, schema, validator, and CI changes.

Create and review records through the documented operations, then run:

```text
python scripts/validate_schemas.py
python scripts/validate_source_processing.py
python scripts/validate_knowledge.py
```

Validation is an integrity check, not approval. Content extraction remains
subject to `project/source-management-policy.md` and
`project/information-handling.md`.

## Limitations

Stage 9 closed with no production evidence or structured knowledge records. The
post-stage pilot now has one human-verified, AI-origin evidence statement. It
does not implement general source extraction, automatic change impact,
assessment generation, or publication generation. Approved post-Stage-9
controls provide a processing-run register and text/HTML reader. One pilot run
is technically verified. Existing root-level knowledge notes remain
provisional and outside this policy's structured production-record set until
reviewed migration.
