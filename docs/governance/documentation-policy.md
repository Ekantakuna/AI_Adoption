# Documentation policy

## Purpose

Documentation is part of the repository control system. It defines how humans
and agents distinguish implemented behavior from plans, locate canonical
records, operate workflows, and review limitations.

## Authority and placement

- `README.md`: concise repository entry point.
- `AGENTS.md`: authoritative agent operating contract.
- `ARCHITECTURE.md`: authoritative target architecture and boundaries.
- `docs/`: cross-repository architecture, governance, operations, and reference.
- directory `README.md` files: local scope and content rules.
- `project/status/`: evidence-backed implementation and stage state.
- `project/decisions/`: material architectural decisions.
- `CHANGELOG.md`: notable changes over time.

Prefer a link to the authoritative document over copying a definition. If
duplication is necessary for usability, identify the authority and keep the copy
brief.

## Required content for a changed concept

When a change adds or alters a concept, object type, schema, taxonomy, metadata
field, status, workflow, script, command, directory, automation, publication
type, or presentation type, document:

- what it is and why it exists;
- inputs and outputs;
- identifier rules and lifecycle;
- relationships to upstream and downstream objects;
- validation rules;
- ownership or review responsibility;
- operational procedure;
- known limitations and implementation status.

Update the documentation, stage status, tests/validation, and implementation in
the same change set. Record material architecture choices in an ADR.

## Status and claim language

Use the status definitions in [statuses.md](../reference/statuses.md). State
facts with repository path evidence. Label assumptions, inferences, and
recommendations. Use future or target language for planned functions.

Do not use directory existence, README intent, or an empty configuration file as
evidence of an operating capability. Do not describe a parser check as schema
validation or a draft as approval.

## Links and formatting

- Use clear English and repository-relative links.
- Define specialized terms on first use or link to their definition.
- Use Mermaid diagrams only with a complete prose explanation.
- Prompt files under `prompts/codex/` must use their defined YAML front-matter
  metadata convention; other Markdown files need not use front matter unless a
  separate contract requires it.
- Preserve stable IDs and exact controlled values in documentation.

## Review and ownership

The change author keeps documentation synchronized. Reviewers confirm accuracy,
authority boundaries, links, implementation status, and absence of unsupported
claims. Only an authorized human can approve policies and the knowledge or
organizational claims listed in `AGENTS.md`; AI-authored changes remain drafts
or proposals until that review is recorded.

## Validation

Documentation validation should include Markdown structure, relative links,
Mermaid syntax where tooling exists, duplicate authority checks, and
`git diff --check`. No documentation build or link checker is configured at
this baseline, so local review must report that limitation.
