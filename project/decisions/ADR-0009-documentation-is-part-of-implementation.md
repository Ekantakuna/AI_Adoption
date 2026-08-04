---
id: ADR-0009
title: Treat agent documentation as part of implementation
status: accepted
date: 2026-07-30
reviewed_by: Maksim Zakharenkau
reviewed_at: 2026-08-02
decision_owners:
  - repository maintainers
supersedes:
superseded_by:
---

# ADR-0009 — Treat agent documentation as part of implementation

## Context

The authoritative agent contract requires implementation changes to update
their relevant documentation, project status, and notable change history. It
also requires material architectural decisions to be recorded and capabilities
to be described from repository evidence rather than directory intent.

This is an operative repository rule. Maksim Zakharenkau accepted this
AI-authored ADR on 2026-08-02. Automated documentation builds, link checking,
policy linting, and completeness enforcement are not configured.

## Decision

Treat documentation as part of implementation for work performed by repository
agents. In the same change as a new or changed concept, object type, schema,
taxonomy, metadata field, status, workflow, script, command, directory,
automation, publication type, or presentation type, document:

- purpose and rationale;
- inputs and outputs;
- identifier and lifecycle rules;
- relationships;
- validation;
- ownership and review responsibility;
- operational procedure;
- limitations and actual implementation status.

Update the applicable stage status, record material architectural choices as
ADRs, and update `CHANGELOG.md` for notable changes. Do not describe proposed or
scaffolded capability as operational.

## Rationale

Repository outcomes must remain understandable and reproducible. Code or
structure without authority, lifecycle, operation, and limitation
documentation cannot safely participate in the traceable information flow.

## Alternatives considered

### Document changes in a later cleanup stage

Not selected because implementation and documentation would drift and reviewers
could not evaluate the complete change.

### Rely only on inline comments

Not selected because cross-repository concepts, ownership, operating
procedures, and status need discoverable authoritative documentation.

### Infer capability from directory names

Not selected because scaffolding does not demonstrate an implemented workflow.

## Consequences

### Positive

- Reviewers can evaluate implementation, authority, operation, and limitations
  together.
- Planned and implemented capabilities remain distinguishable.
- Future agents have an evidence-backed operating context.

### Negative

- Even small architectural changes may touch several documentation records.
- Duplicate explanations must be avoided through links to authoritative pages.

### Risks

- Documentation may state intended behavior that implementation does not
  enforce.
- Manual link and completeness review can miss drift without automation.

## Implementation implications

`AGENTS.md` is the authoritative contract. `ARCHITECTURE.md`, `docs/`,
directory READMEs, `project/status/`, `project/decisions/`, and `CHANGELOG.md`
provide the required documentation surfaces.

This ADR adds no documentation automation. Contributors must run available
checks and explicitly report unavailable validation.

## Validation

Review the diff for corresponding authoritative documentation, stage status,
ADR, and changelog updates. Check relative links, documentation builds, and
linting when configured, then run `git diff --check`. No automated
documentation-completeness validator is currently available.

## References

- [Agent operating contract](../../AGENTS.md)
- [Contribution guide](../../CONTRIBUTING.md)
- [Documentation policy](../../docs/governance/documentation-policy.md)
- [Change management](../../docs/governance/change-management.md)
- [Documentation review status](../status/documentation-review.md)
