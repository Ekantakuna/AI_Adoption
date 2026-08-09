---
id: PRM-CODEX-MAINT-LEGACY-FINAL
title: Perform final stage validation (legacy path)
type: validation
version: 1.0.0
status: deprecated
owner_role: repository-reviewer
created_at: 2026-08-01
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [project/status, scripts, tests, docs]
prohibited_actions: [commit, push, source_body_access]
required_inputs: [stage_definition, worktree]
expected_outputs: [validation_report]
validation: [repository_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: PRM-CODEX-VAL-FINAL
---

# Task: Perform final stage validation

Inspect all current uncommitted changes.

Read `AGENTS.md` and the current stage status document.

Validate:

- YAML syntax
- schemas
- controlled values
- identifier uniqueness
- cross-file references
- source-catalogue references
- evidence references
- tests
- documentation links
- documentation alignment with implementation
- stage status completeness
- changelog impact
- ADR impact
- Git whitespace errors

Run all existing repository validators and tests.

Run:

- `git diff --check`
- `git status --short`
- `git diff --stat`

Do not make unrelated improvements.

Correct defects that are directly caused by the current stage.

Do not commit or push.

Report:

1. Commands executed
2. Passed checks
3. Failed checks corrected
4. Remaining failures
5. Files changed during validation
6. Whether the stage is ready for human review and commit
