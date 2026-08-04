# Assumptions

- **Purpose:** make unverified propositions explicit so they can be tested and reviewed.
- **Accepted:** Markdown assumptions with schema-valid front matter and optional supporting evidence.
- **Prohibited:** assumptions presented as facts, silent replacement of contradictory evidence, or approved commitments.
- **Identifier prefix:** `ASSUMPTION`; use `ASSUMPTION-NNNNNN` and never reuse an ID.
- **Template:** `assumption-template.md` (`ASSUMPTION-000000` is not production).
- **Evidence requirement:** at least one valid `EVID` reference providing the context from which the assumption was identified; the assumption remains unverified.
- **Review requirement:** AI output starts as `draft` or `needs_review`; reviewer information is mandatory for `verified` or `approved`.
- **Upstream inputs:** atomic evidence, identified unknowns, concepts, and assessment questions.
- **Downstream consumers:** relationships, assessments, decisions, outlooks, and review queues.
