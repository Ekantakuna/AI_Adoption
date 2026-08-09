---
id: PRM-CODEX-VAL-FINAL
title: Perform final stage validation
type: validation
version: 1.0.0
status: active
owner_role: stage-reviewer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [project/roadmap, project/status, scripts, tests, docs, schemas, config]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation, automatic_approval]
required_inputs: [active_stage_definition, worktree]
expected_outputs: [validation_report, human_review_readiness]
validation: [yaml_parse, schema_validation, repository_validators, tests, documentation_alignment, git_diff_check]
human_review: required
supersedes: prompts/codex/maintenance/final-stage-validation.md
superseded_by: null
---

# Perform final stage validation

Read `AGENTS.md`, the active stage definition and status, roadmap requirements,
and current diff. Run applicable YAML/schema/controlled-value/reference
validators and tests. Check documentation alignment, exit gates, status and
changelog/ADR impact, then run `git diff --check`, `git status --short`, and
`git diff --stat`. Correct only defects directly caused by the stage after
reporting them. Report commands, passed checks, corrected failures, remaining
failures, changed files, and whether the stage is ready for human review. Do
not claim approval or commit/push.
