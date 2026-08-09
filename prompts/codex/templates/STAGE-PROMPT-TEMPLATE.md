---
id: PRM-TEMPLATE-STAGE
title: Stage prompt template
type: template
version: 1.0.0
status: draft
owner_role: repository-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: stage-specific
source_access: repository_only
allowed_paths: []
prohibited_actions: [commit, push, source_body_access, unrelated_implementation]
required_inputs: [approved_roadmap, stage_id]
expected_outputs: [stage_implementation, stage_status, validation_report]
validation: [roadmap_checks, stage_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Stage <ID> — <name>

Read `AGENTS.md`, `project/roadmap.yaml`, and the human-readable roadmap.
Record the roadmap reference, stage ID, entry criteria, dependency checks,
exact scope, outputs, out-of-scope work, source boundary, implementation and
documentation impact, ADR impact, downstream consumers, validation, exit gates,
stage-status update, roadmap-status update, human review, and final report.
Do not execute a generated prompt until separately instructed.
