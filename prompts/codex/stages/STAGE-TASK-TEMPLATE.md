---
id: PRM-TEMPLATE-STAGE-TASK
title: Legacy stage task template
type: template
version: 1.0.0
status: draft
owner_role: stage-implementer
created_at: 2026-08-01
updated_at: 2026-08-05
roadmap_stage: stage-specific
source_access: repository_only
allowed_paths: []
prohibited_actions: [commit, push, source_body_access]
required_inputs: [approved_roadmap, stage_id]
expected_outputs: [stage_work, stage_status]
validation: [applicable_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Stage N — Replace with stage name

## Objective

Describe the outcome of this stage.

## Preconditions

- Relevant preceding stages are complete.
- Repository validation passes.
- Git status has been inspected.
- `AGENTS.md` has been read.
- Relevant policies, schemas, status files, scripts, tests, and documentation
  have been inspected.

## Scope

Describe exactly what must be implemented.

## Out of scope

Describe what must not be done.

## Source-data access

Choose one:

- No source-content access is allowed.
- Metadata-only source access is allowed.
- Source-content access is allowed only for the explicitly listed source IDs.
- Incremental processing of changed approved sources is allowed.

Original source files must never be modified.

## Required implementation

List required files, schemas, scripts, workflows, and tests.

## Required documentation

For every implementation change, update the corresponding:

- architecture documentation
- concept documentation
- operational procedure
- directory README
- schema reference
- status report
- ADR when a material decision is introduced
- changelog when appropriate

The documentation must explain:

- what changed
- why it changed
- inputs
- outputs
- lifecycle
- identifiers
- relationships
- validation
- operational use
- limitations

## Required status update

Create or update:

`project/status/stage-NN-<name>.md`

Include:

- objective
- status
- work completed
- files created or updated
- validation results
- metrics
- decisions
- risks
- unresolved issues
- next stage

## Validation

Run:

- relevant YAML parsing
- schema validation
- repository validators
- tests
- documentation build
- `git diff --check`
- `git status --short`

## Git restrictions

Do not commit, push, merge, rewrite history, or delete branches unless explicitly
instructed.

## Final report

Report:

1. Files inspected
2. Files created
3. Files modified
4. Files deleted
5. Implementation details
6. Documentation changes
7. Decisions made
8. Validation results
9. Remaining risks and gaps
10. Recommended next action
