---
id: PRM-CODEX-PLAN-096
title: Review the Stage 9.5 master roadmap
type: review
version: 1.0.0
status: active
owner_role: roadmap-reviewer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: stage-09.5
source_access: repository_only
allowed_paths: [project/roadmap.yaml, project/roadmap, project/status/master-roadmap-status.md, scripts/validate_roadmap.py, tests, docs]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation, automatic_approval]
required_inputs: [roadmap_files, roadmap_validation_result]
expected_outputs: [findings_by_severity, roadmap_review_report]
validation: [roadmap_validation, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Review the Stage 9.5 roadmap

Default to read-only inspection. Read `AGENTS.md`, both roadmap forms, the
roadmap status, validator/test, relevant status and ADRs. Report findings by
severity with exact paths and evidence, separating facts from recommendations.
Check human/machine consistency, unique stable IDs, dependency cycles,
prerequisites, entry criteria, exit gates, success measures, completion claims,
roadmap status, source restrictions, documentation, validation, and rules for
future stage-prompt generation. Correct only directly related defects after
findings are recorded. Do not implement Stage 10 or later. Finish with human
approval readiness and a complete final report; do not commit or push.
