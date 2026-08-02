# Knowledge object model

## Common contract

Production records have a globally unique six-digit ID, configured `type`,
classification, controlled `review_status`, `origin`, creator, creation date,
and type-specific content. Evidence-required objects contain `evidence_ids`.
Verified and approved records contain an identified reviewer and review date.
Markdown objects store metadata in YAML front matter; evidence and relationship
records are YAML-only. Templates use `000000`, carry `template: true`, contain
no substantive claims, and are excluded from production validation counts.

## Object families

| Family | Prefix | Role | Evidence rule |
| --- | --- | --- | --- |
| Atomic evidence | `EVID` | Source-attributable statement | cites source, locator, and processing run |
| Glossary term | `TERM` | Controlled definition | required |
| Concept | `CONCEPT` | Interpreted reusable idea | required |
| Framework | `FRAME` | Organizing or evaluation model | required |
| Metric | `METRIC` | Measure definition | required |
| Risk | `RISK` | Evidence-backed risk knowledge | required |
| Trend | `TREND` | Pattern over time | required |
| Use case | `USECASE` | Application and intended outcome | required |
| Relationship | `REL` | Typed knowledge-object link | required |
| Assumption | `ASSUMPTION` | Explicit unverified proposition | required for context, not verification |
| Knowledge decision | `DECISION` | Evidence-backed knowledge decision | required |
| Reference | `REF` | Stable contextual pointer | required and does not replace evidence |

The complete directory, format, schema, and evidence controls are in
`config/knowledge-types.yaml`. Relationships cannot use evidence or another
relationship as endpoints; evidence remains a supporting reference rather than
a graph endpoint in this model.
