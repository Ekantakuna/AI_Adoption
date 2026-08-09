---
id: PRM-CODEX-PLAN-095
title: Establish the Stage 9.5 master implementation roadmap
type: planning
version: 1.0.0
status: active
owner_role: roadmap-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: stage-09.5
source_access: repository_only
allowed_paths: [AGENTS.md, ARCHITECTURE.md, README.md, project, scripts, tests, docs, CHANGELOG.md]
prohibited_actions: [commit, push, source_body_access, stage-10-implementation, unsupported_estimates]
required_inputs: [repository_state, stage-09-status]
expected_outputs: [project/roadmap/README.md, project/roadmap/implementation-roadmap.md, project/roadmap.yaml, project/roadmap/stage-template.md, project/roadmap/stage-lifecycle.md, project/status/master-roadmap-status.md, scripts/validate_roadmap.py, tests/test_roadmap_validation.py]
validation: [yaml_parse, roadmap_validation, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Stage 9.5 — Establish the master implementation roadmap

## Objective and inspection

Read `AGENTS.md`, the current architecture, documentation, configuration,
schemas, validators, tests, workflows, all relevant `project/status/` files,
existing ADRs, branch, status, and diff. Do not inspect external source bodies.

## Scope and deliverables

Create and govern exactly the roadmap files and validator/test listed in the
metadata. Define stable stage IDs, prerequisites, entry criteria, deliverables,
validation, exit gates, success measures, and dependencies. Define how
implemented, partial, planned, absent, and unknown capabilities are represented.
Avoid dates, budgets, headcount, and unsupported effort estimates. Identify
Stage 10 as the next stage only if repository evidence and dependencies justify
it; do not implement Stage 10 or later stages.

The machine-readable and human-readable roadmaps must be mutually checkable.
The validator must detect duplicate IDs, missing references, dependency cycles,
invalid controlled status, and mismatched required fields without changing data.

## Documentation, review, and exit

Explain inputs, outputs, ID lifecycle, ownership, validation, limitations, ADR
impact, and downstream prompt generation. Preserve draft/review state. Run YAML
parsing, roadmap validation, existing validators, tests, and `git diff --check`.
Report files inspected/created/modified/deleted, decisions, documentation,
validation, unresolved issues, and next action. Do not commit or push.
