---
id: ADR-0004
title: Use Markdown and YAML as canonical tracked formats
status: proposed
date: 2026-07-30
decision_owners:
  - repository maintainers
supersedes:
superseded_by:
---

# ADR-0004 — Use Markdown and YAML as canonical tracked formats

## Context

Repository guidance consistently identifies reviewed Markdown and structured
YAML records as canonical tracked content. The implementation uses Markdown for
policies, decisions, status, knowledge notes, and operating documentation, and
YAML for configuration, source metadata, schemas, manifests, and register
scaffolds.

This format rule is proposed for the repository. It does not make every
Markdown file authoritative or every YAML scaffold operational. Canonical
authority still depends on the designated location, classification, schema
where applicable, provenance, and review state.

## Decision

Maintain human-oriented canonical records in Markdown and structured canonical
records and controlled configuration in YAML. Use approved schemas for
structured record types before they become operational.

Treat rendered reports, slides, websites, indexes, and other generated files as
derivatives rather than substitutes for canonical Markdown or YAML inputs.

## Rationale

Markdown and YAML are text-based, reviewable in Git, portable across tools, and
suited respectively to narrative records and structured validation.

## Alternatives considered

### Office documents as canonical repository records

Not selected because binary review, merge, validation, and provenance tracking
are weaker in the current Git workflow.

### A database as the only canonical store

Not selected because no database, migration workflow, access model, or export
contract is implemented, and repository review depends on inspectable tracked
changes.

### Generated publications as canonical records

Not selected because audience outputs are lossy selections and must remain
rebuildable from reviewed upstream content.

## Consequences

### Positive

- Changes remain readable and diffable.
- YAML records can be constrained by machine-readable schemas.
- Canonical inputs remain tool-independent.

### Negative

- Complex relationships and rich presentation layout require derived tools or
  projections.
- YAML schemas and repository-level validators must be maintained separately.

### Risks

- Contributors may confuse Git tracking or valid syntax with authority or
  approval.
- Hand-edited YAML may be syntactically valid while violating cross-record
  rules.

## Implementation implications

Markdown is used throughout `docs/`, `project/`, and `knowledge/`. YAML is used
in `config/`, `sources/`, `schemas/`, and `registers/`. New structured object
types require an approved object-specific schema, lifecycle, ownership, and
validation before records are added.

Most object-specific schemas and repository validators remain absent. This
decision does not approve ad hoc YAML shapes or claim that the planned
publication pipeline exists.

## Validation

Parse YAML safely, run applicable schema and repository validators, inspect
Markdown links and documentation builds when configured, and run
`git diff --check`. YAML parsing is not schema validation, and the repository
currently lacks an automated documentation build and general register
validator.

## References

- [Agent operating contract](../../AGENTS.md)
- [Repository README](../../README.md)
- [Contribution guide](../../CONTRIBUTING.md)
- [Register contract](../../registers/README.md)
- [Schema contract](../../schemas/README.md)
- [Repository baseline](../status/repository-baseline.md)
