---
id: PRM-CODEX-REV-STAGE
title: Review stage quality
type: review
version: 1.0.0
status: active
owner_role: stage-reviewer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [project/roadmap, project/status, docs, scripts, tests, prompts]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation, automatic_approval]
required_inputs: [stage_id, stage_diff, stage_status]
expected_outputs: [findings_by_severity, stage_quality_report]
validation: [applicable_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Review stage quality

Read `AGENTS.md`, the active stage definition, roadmap requirements, status,
diff, documentation, schemas, validators, and tests. Default to read-only.
Review scope fidelity, prerequisites, entry/exit gates, stable IDs,
implementation versus documentation, source boundary, evidence/provenance,
validation, ADR impact, downstream consumers, and unsupported completion or
approval claims. Report critical/high/medium/low/informational findings with
paths. Only after reporting may you correct directly related defects. Run
applicable checks and finish with human-review readiness. Do not commit or push.
