---
id: PRM-CODEX-MAINT-HEALTH
title: Check repository health
type: maintenance
version: 1.0.0
status: active
owner_role: repository-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: [., project/status, scripts, tests, docs, prompts, .github]
prohibited_actions: [commit, push, source_body_access, unrelated_implementation, silent_fix]
required_inputs: [repository]
expected_outputs: [health_report, findings]
validation: [yaml_parse, repository_validators, tests, git_status, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Repository health check

Read `AGENTS.md` and inspect Git status/diff. Check invalid YAML, validator
failures, broken references, undocumented implementation, stale status files,
missing roadmap evidence, untracked generated files, source binaries
accidentally added to Git, and unexpected AI records marked approved or
verified. Use repository metadata only; do not inspect external source bodies.
Report each finding with severity, path, evidence, and recommendation. Do not
silently fix unrelated findings or automatically approve anything. Run
available validators/tests and `git diff --check`; finish with unresolved
issues, human-review needs, and a complete report. Do not commit or push.
