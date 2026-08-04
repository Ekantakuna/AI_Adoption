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
