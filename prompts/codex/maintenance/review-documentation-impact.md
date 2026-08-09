---
id: PRM-CODEX-MAINT-LEGACY-DOC
title: Review documentation impact of current changes (legacy path)
type: review
version: 1.0.0
status: deprecated
owner_role: repository-reviewer
created_at: 2026-08-01
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [docs, project, prompts, scripts, tests, .github]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation]
required_inputs: [git_diff]
expected_outputs: [documentation_impact_report]
validation: [repository_validators, git_diff_check]
human_review: required
supersedes: null
superseded_by: PRM-CODEX-REV-DOC
---

# Task: Review documentation impact of current changes

Inspect the current Git diff.

For every changed implementation file, determine whether related documentation
must also change.

Implementation includes:

- schemas
- configuration
- scripts
- tests
- workflows
- knowledge object types
- metadata
- status vocabularies
- prompts
- publication templates
- presentation templates
- directory structures

Check whether the diff introduces or changes:

- a concept
- an object
- an identifier
- a field
- a relationship
- a lifecycle
- a status
- a command
- a workflow
- an operating procedure
- a validation rule
- an automation
- an architectural decision

Update the relevant documentation where needed.

Do not create documentation changes merely to satisfy a mechanical count.
Documentation must accurately explain the implementation.

Do not inspect external source-document contents unless the current task
explicitly authorizes it.

Run relevant validation and `git diff --check`.

Report:

- implementation files reviewed
- documentation impacts identified
- documentation files updated
- implementation changes lacking enough context
- validation results

Do not commit or push.
