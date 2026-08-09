---
id: PRM-TEMPLATE-MAINTENANCE
title: Maintenance prompt template
type: template
version: 1.0.0
status: draft
owner_role: repository-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: metadata_only
allowed_paths: []
prohibited_actions: [commit, push, automatic_approval, source_body_access]
required_inputs: [change_scope]
expected_outputs: [maintenance_report, proposals]
validation: [applicable_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Maintenance: <scope>

Define recurring or incremental scope and change-detection inputs. Read
`AGENTS.md` and applicable policies. Preserve stable IDs, record processing runs
when a governed run exists, identify stale downstream objects, and label future
prerequisites. Do not automatically approve knowledge or silently fix unrelated
findings. Report facts, proposals, validation, and human-review needs.
