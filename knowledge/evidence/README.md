# Atomic evidence

- **Purpose:** store one attributable source statement or observation per YAML record.
- **Accepted:** schema-valid atomic evidence created from an approved processing run and precise source locator.
- **Prohibited:** source binaries, raw extraction dumps, synthesis, unsupported claims, and approved status without human review.
- **Identifier prefix:** `EVID`; use `EVID-NNNNNN` and never reuse an ID.
- **Template:** `evidence-template.yaml` (placeholder `EVID-000000`, never a production record).
- **Evidence requirement:** the record is evidence; it must cite a catalogue `source_id`, locator, and processing-run ID.
- **Review requirement:** AI output starts as `draft` or `needs_review`; `verified` and `approved` require reviewer identity and date.
- **Upstream inputs:** `sources/catalogue.yaml` and an approved, recorded source-processing run.
- **Downstream consumers:** knowledge objects, relationships, assessments, outlook content, reports, and presentations.
- **Current production set:** `EVID-000001` is an AI-origin internal evidence
  statement verified by Maksim Zakharenkau; verification does not establish
  organizational implementation or broader approval.
  `EVID-000002`–`000009` are internal AI-origin drafts awaiting source-fidelity
  review for the three newly ingested implemented-use-case decks.
