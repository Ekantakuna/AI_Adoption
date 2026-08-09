---
id: PRM-CODEX-BOOT-001
title: Establish the AI Adoption repository operating model
type: bootstrap
version: 1.1.0
status: active
owner_role: repository-maintainer
created_at: 2026-08-01
updated_at: 2026-08-05
roadmap_stage: bootstrap
source_access: repository_only
allowed_paths: [AGENTS.md, README.md, ARCHITECTURE.md, CONTRIBUTING.md, CHANGELOG.md, docs, project/status]
prohibited_actions: [commit, push, source_body_access, unsupported_claims]
required_inputs: [repository]
expected_outputs: [operating_model, documentation, status]
validation: [repository_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Task: Establish the AI Adoption repository operating model

You are working in the root of the AI Adoption repository.

## Objective

Create a self-describing, maintainable repository that can be understood and
operated by humans and AI agents.

The repository supports:

- evidence source inventory
- controlled content extraction
- evidence management
- knowledge management
- knowledge graph construction
- current-state assessment
- project and progress management
- audience-specific reports
- audience-specific presentations
- incremental processing when source information changes

## Mandatory first actions

Before changing files:

1. Read all existing top-level documentation.
2. Read any existing `AGENTS.md`, `GEMINI.md`, `README.md`, architecture,
   governance, source-management, status, schema, configuration, workflow,
   script, and test files.
3. Inspect the repository directory structure.
4. Inspect Git status and current branch.
5. Identify what is already implemented.
6. Do not infer that a planned component exists without evidence in the repo.
7. Do not access or analyze external source document contents during this task.

## Source-data boundary

External source documents may exist outside Git and may be accessible locally.

For this task:

- do not open or read source-document contents
- do not copy source documents into the repository
- do not extract knowledge from source documents
- do not modify source documents
- source metadata and the existing source catalogue may be inspected

## Required outputs

Create or update the following, preserving existing useful content:

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `ARCHITECTURE.md`
- `CHANGELOG.md`
- `docs/index.md`
- `docs/project-purpose.md`
- `docs/repository-map.md`
- `docs/architecture/information-flow.md`
- `docs/architecture/agent-operating-model.md`
- `docs/architecture/publication-pipeline.md`
- `docs/governance/documentation-policy.md`
- `docs/governance/change-management.md`
- `docs/operations/local-development.md`
- `docs/reference/identifiers.md`
- `docs/reference/statuses.md`
- `project/status/repository-baseline.md`

If an equivalent document already exists under another appropriate path, update
and link it rather than creating unnecessary duplication.

## Required repository explanation

Document the repository as a layered system:

1. Source layer
2. Evidence layer
3. Knowledge layer
4. Assessment and outlook layer
5. Project and progress layer
6. Publication layer
7. Presentation layer
8. Automation and validation layer

Explain that the intended flow is:

Source assets
→ metadata catalogue
→ content processing
→ atomic evidence
→ structured knowledge
→ relationships and impact analysis
→ assessments and progress views
→ reports
→ presentations

Clarify that this describes the target architecture. Clearly distinguish:

- implemented
- partially implemented
- planned
- not yet implemented

Do not describe planned functionality as operational.

## AGENTS.md requirements

`AGENTS.md` must be the authoritative operating contract for repository agents.

It must include:

### Repository purpose

Explain the purpose and intended outcomes of the AI Adoption repository.

### Instruction precedence

Use this precedence order:

1. Explicit user instruction for the current task
2. `AGENTS.md`
3. Stage-specific prompt
4. Repository policies
5. Directory README files
6. Existing conventions

An agent must report material conflicts rather than silently choosing.

### Mandatory inspection

Before editing, agents must inspect:

- relevant implementation
- relevant documentation
- schemas and controlled configuration
- tests and validation
- current project status
- Git status

### Evidence protection

Agents must never:

- modify original evidence documents
- silently replace evidence
- invent evidence locations
- create unsupported claims
- mark AI-created knowledge as human-approved
- commit sensitive source documents

### Documentation obligation

An implementation is incomplete until the relevant documentation is updated.

When an agent adds or changes a:

- concept
- object type
- schema
- taxonomy
- metadata field
- status
- workflow
- script
- command
- directory
- automation
- publication type
- presentation type

the same change must document:

- what it is
- why it exists
- inputs
- outputs
- identifier rules
- lifecycle
- relationships
- validation rules
- ownership or review responsibility
- operational procedure
- limitations

### Change explanation

At the end of every task, Codex must report:

- files inspected
- files created
- files modified
- files deleted
- implementation decisions
- documentation updated
- validation performed
- test results
- unresolved issues
- suggested next action

### Status obligation

Every stage implementation must create or update a stage status document under
`project/status/`.

### Decision obligation

Material architectural decisions must be recorded as Architecture Decision
Records under `project/decisions/`.

### Human review boundaries

AI agents may create drafts and review proposals.

Only an authorized human reviewer may approve:

- authoritative knowledge
- policies
- current-state conclusions
- target-state commitments
- recommendations presented as organizational decisions
- publication-ready executive claims

### Git behavior

Unless explicitly instructed, agents must:

- not commit
- not push
- not merge
- not rewrite Git history
- not delete branches
- not modify unrelated files

### Validation obligation

Before completion, agents must run all relevant:

- YAML parsing
- schema validation
- repository validators
- tests
- documentation checks
- `git diff --check`

### No silent normalization

Agents must not silently reconcile conflicting terms, definitions, assessments,
or source claims.

Conflicts must be represented explicitly.

## Architecture documentation requirements

Document:

- system context
- logical layers
- information flow
- source-of-truth boundaries
- authoritative versus generated data
- local-only versus Git-tracked data
- human review points
- planned incremental update model
- intended publication and presentation generation

Use Mermaid diagrams where useful, but ensure the surrounding prose is complete
without relying only on diagrams.

## Repository map requirements

For every significant top-level directory, document:

- purpose
- accepted content
- prohibited content
- upstream inputs
- downstream consumers
- main validation mechanism
- implementation status

## Baseline status requirements

`project/status/repository-baseline.md` must describe what currently exists,
based only on repository inspection.

For each relevant component, classify it as:

- implemented
- partial
- planned
- absent
- unknown

Include evidence in the form of repository paths.

Do not claim that content extraction, knowledge graph operation, incremental
processing, reporting, or presentation automation is implemented unless the
corresponding repository files demonstrate it.

## Documentation style

- Use clear English.
- Define specialized terminology.
- Avoid marketing language.
- Avoid claiming future capabilities as current capabilities.
- Link documents to one another using relative repository links.
- Prefer one authoritative explanation over duplicated explanations.
- Add YAML front matter only where the repository already uses it consistently.

## Validation

After implementation:

1. Run existing repository validation.
2. Validate YAML files.
3. Run existing tests.
4. Run documentation or MkDocs validation if configured.
5. Run `git diff --check`.
6. Run `git status --short`.

## Final response

Provide:

1. Repository findings before changes
2. Files created
3. Files updated
4. Major documentation decisions
5. Implemented versus planned capability summary
6. Validation results
7. Warnings or unresolved gaps
8. Recommended next step

Do not commit or push.
