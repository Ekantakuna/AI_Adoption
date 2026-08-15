# Knowledge relationships

- **Purpose:** store explicit, typed links between existing knowledge-object IDs.
- **Accepted:** schema-valid YAML relationships with two existing non-evidence endpoints and supporting evidence.
- **Prohibited:** dangling endpoints, relationships to templates, implicit conflict resolution, and graph exports.
- **Identifier prefix:** `REL`; use `REL-NNNNNN` and never reuse an ID.
- **Template:** `relationship-template.yaml` (`REL-000000` is not production).
- **Evidence requirement:** at least one valid `EVID` reference supporting the asserted link.
- **Review requirement:** AI output starts as `draft` or `needs_review`; authority requires identified human review.
- **Upstream inputs:** existing knowledge-object IDs and atomic evidence.
- **Downstream consumers:** impact analysis, assessments, outlooks, reports, and presentations.

## Lifecycle and traversal

ADR-0011 defines the accepted relationship directions, endpoint constraints,
impact direction, maximum depth, cycle policy, and deprecated/conflict behavior.
`config/relationship-types.yaml` is the controlled executable mapping.

AI-origin relationships start as `draft` or `needs_review`. `verified` or
`approved` requires an identified human reviewer; `rejected` and `deprecated`
records retain their IDs for audit. A relationship is never inferred from
similar wording.

Run `python scripts/validate_relationship_impact.py` for integrity validation.
Add `--start-id`, `--direction`, and `--max-depth` for a read-only derived view.
No graph projection is canonical, and the operation never updates a knowledge
record. There are currently no production `REL` records; behavior is covered by
synthetic tests.
