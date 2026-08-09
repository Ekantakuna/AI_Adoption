---
id: PRM-CODEX-REV-DOC
title: Review documentation impact of current changes
type: review
version: 1.0.0
status: active
owner_role: repository-reviewer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [docs, project, prompts, scripts, tests, .github, README.md, ARCHITECTURE.md, AGENTS.md, CHANGELOG.md]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation]
required_inputs: [git_diff]
expected_outputs: [documentation_impact_findings, updated_docs_if_authorized]
validation: [repository_validators, git_diff_check]
human_review: required
supersedes: prompts/codex/maintenance/review-documentation-impact.md
superseded_by: null
---

# Review documentation impact

Inspect the current Git diff and relevant implementation context. For each
changed schema, configuration, script, test, workflow, metadata field, object,
taxonomy, status, command, directory, automation, prompt, publication, or
presentation, identify documentation required for purpose, inputs, outputs,
IDs, lifecycle, relationships, validation, ownership, procedure, and
limitations. Report findings before any correction. Separate facts from
recommendations and prohibit unrelated implementation. Check architecture,
directory map, policy, status, ADR, changelog, and operational documentation.
Run applicable validation and `git diff --check`; report gaps and human-review
needs. Do not inspect source bodies or commit/push.
