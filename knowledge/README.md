# Knowledge base

This directory is the controlled home for atomic evidence and interpreted
knowledge. Stage 9 implements type configuration, schemas, templates, review
controls, relationship integrity, tests, and validation. It created no
production records during Stage 9 itself. Approved post-stage processing now
supports verified runs and controlled evidence/knowledge drafting.

## Object locations

| Directory | Object | Prefix |
| --- | --- | --- |
| `evidence/` | atomic evidence statement | `EVID` |
| `glossary/` | glossary term | `TERM` |
| `concepts/` | concept | `CONCEPT` |
| `frameworks/` | framework | `FRAME` |
| `metrics/` | metric definition | `METRIC` |
| `risks/` | evidence-backed risk knowledge | `RISK` |
| `trends/` | trend | `TREND` |
| `use_cases/` | use case | `USECASE` |
| `relationships/` | typed knowledge relationship | `REL` |
| `assumptions/` | explicit assumption | `ASSUMPTION` |
| `decisions/` | knowledge decision | `DECISION` |
| `references/` | contextual reference | `REF` |

Each subdirectory README defines accepted/prohibited content, its template,
evidence rule, review requirement, upstream inputs, and downstream consumers.
Controlled details are in `config/knowledge-types.yaml`; lifecycle and
confidence values are in `config/review-statuses.yaml` and
`config/evidence-confidence.yaml`.

Extraction is not atomic evidence, and evidence is not interpreted knowledge.
Knowledge may be stored in Git only when classification permits. AI-created
material starts as `draft` or `needs_review`; only an authorized human may add
the review record required for `verified` or `approved`.

The current structured set contains nine evidence records and three use-case
records. `EVID-000001` is verified; `EVID-000002`–`000009` and
`USECASE-000001`–`000003` are AI-origin internal drafts in `needs_review`.

Run `python scripts/validate_schemas.py` and
`python scripts/validate_knowledge.py` from the repository root. They ignore
READMEs and templates and validate schema conformance, production IDs, types,
source/evidence references, relationship endpoints, statuses, confidence,
uniqueness, and reviewer gates.

## Preserved provisional files

`current_state_search_20.md` is a substantive current-state synthesis note tied
to one source, and `public-source-analysis.md` is a substantive multi-source
analysis/synthesis note. Both predate the object model, lack structured front
matter and review metadata, and are therefore retained unchanged as
legacy/provisional analysis notes. They are not atomic evidence, schema-valid
knowledge, verified facts, or approved conclusions. A later authorized
migration must atomize supported statements, establish processing-run and
locator provenance, create new stable IDs, preserve inference boundaries, and
review the resulting records; Stage 9 does not migrate their content.

See `docs/concepts/source-evidence-knowledge.md`,
`project/knowledge-management-policy.md`, and the Stage 9 status record for the
full boundaries and current limitations.
