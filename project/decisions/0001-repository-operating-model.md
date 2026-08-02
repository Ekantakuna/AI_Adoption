# ADR 0001: Repository operating model

- Status: accepted
- Date: 2026-07-30
- Reviewed by: Maksim Zakharenkau
- Reviewed at: 2026-08-02
- Decision owners: repository maintainers and authorized human reviewers
- Proposed by: Codex during the repository operating-model stage

## Context

The repository has a source metadata inventory, source-control policies,
controlled configuration, empty structured registers, domain scaffolding, and a
small number of source-linked knowledge notes. It does not have an explicit
end-to-end architecture, downstream object schemas, graph operation,
incremental processing, or publication automation.

Without explicit layers and source-of-truth boundaries, scaffolded directories
can be mistaken for implemented capabilities and generated outputs can be
mistaken for authoritative records.

## Decision

Organize repository responsibilities as eight logical layers:

1. source;
2. evidence;
3. knowledge;
4. assessment and outlook;
5. project and progress;
6. publication;
7. presentation;
8. automation and validation.

Use the target flow:

**Source assets → metadata catalogue → content processing → atomic evidence →
structured knowledge → relationships and impact analysis → assessments and
progress views → reports → presentations.**

Original evidence remains authoritative outside Git. Git-tracked reviewed
Markdown and approved schema-valid registers are canonical for repository
knowledge and control records. Generated manifests, graph projections, reports,
decks, and websites are replaceable derivatives. Downstream objects reference
stable upstream IDs and do not overwrite upstream provenance.

Capabilities must be described as implemented, partial, planned, absent, or
unknown from repository evidence. AI agents may draft but cannot approve the
human-review-bound content listed in `AGENTS.md`.

## Consequences

- Every new object type requires an identifier, lifecycle, schema, provenance,
  validation, ownership, and operational documentation.
- Stage work updates implementation, documentation, status, validation, and
  material ADRs together.
- Publication and presentation automation must consume approved canonical
  content and retain claim-level traceability.
- Incremental processing requires explicit downstream relationships, stale or
  invalidated states, and review gates before it can be called operational.
- Some duplication may remain as generated views, but each view identifies its
  authority and reconciliation behavior.
- Source catalogue conflicts require explicit attributed reconciliation; the
  2026-08-02 reconciliation records the current decision without erasing
  historical states.

## Alternatives considered

### Directory-only convention

Rely on existing directory names and README files without a cross-repository
model. Rejected because directory presence does not establish authority,
information flow, review gates, or implementation status.

### Generated outputs as primary records

Treat reports or presentations as the maintained source. Rejected because this
loses reusable evidence/knowledge structure and makes provenance and incremental
change impact difficult.

### Single undifferentiated knowledge store

Place source metadata, evidence, interpretation, assessment, and publication
content in one record family. Rejected because each has different authority,
review, classification, and lifecycle requirements.

## Validation and review

Reviewers should verify the layer boundaries, human approval roles,
canonical/derived distinction, and compatibility with the source-management
policy. If accepted, record the reviewer and decision date and update the
status. Maksim Zakharenkau accepted this ADR on 2026-08-02 with the retained
implementation limitations documented below.

## Acceptance implementation review — 2026-08-02

Stage 9 and accepted ADRs 0005–0007 implement the empty evidence/knowledge
framework and review boundaries. Accepted ADR 0010 implements source-processing
authorization/run contracts and the explicit catalogue reconciliation. The
assessment, publication, presentation, graph-traversal, and incremental-
processing layers remain partial, planned, or absent. Accepting this ADR
approves the target operating model, not those unimplemented capabilities.
