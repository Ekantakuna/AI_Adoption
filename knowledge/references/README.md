# References

- **Purpose:** maintain knowledge-layer citations or pointers that are not source-catalogue records or evidence statements.
- **Accepted:** Markdown reference records with schema-valid front matter for stable external standards or internal repository pointers when duplication in the source catalogue is inappropriate.
- **Prohibited:** source binaries, replacement source metadata, extracted claims, and opaque links without context.
- **Identifier prefix:** `REF`; use `REF-NNNNNN` and never reuse an ID.
- **Template:** `reference-template.md` (`REF-000000` is not production).
- **Schema:** `schemas/reference.schema.yaml`.
- **Evidence requirement:** at least one valid `EVID` reference establishes why the contextual pointer is used; a reference never replaces evidence.
- **Review requirement:** AI output starts as `draft` or `needs_review`; reviewer information is mandatory for `verified` or `approved`.
- **Upstream inputs:** controlled repository or external reference metadata.
- **Downstream consumers:** evidence notes, knowledge objects, assessments, documentation, and publications.
