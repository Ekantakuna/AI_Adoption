---
id: PRM-TEMPLATE-REVIEW
title: Review prompt template
type: template
version: 1.0.0
status: draft
owner_role: repository-reviewer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: []
prohibited_actions: [commit, push, unrelated_implementation, source_body_access]
required_inputs: [review_scope]
expected_outputs: [findings_by_severity, review_report]
validation: [git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Review: <scope>

Default to read-only inspection. Read `AGENTS.md`, the stated scope, relevant
policies, schemas, tests, status, and diff. Report findings as critical, high,
medium, low, or informational with path and evidence. Separate facts from
recommendations. Prohibit unrelated implementation. Corrections are allowed
only after findings are reported and only when directly in scope. Finish with
validation, unresolved issues, and human-review readiness.
