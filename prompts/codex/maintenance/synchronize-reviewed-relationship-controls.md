---
id: PRM-CODEX-MAINT-REL-CONTROLS
title: Synchronize reviewed relationship controls and CI
type: maintenance
version: 1.0.0
status: active
owner_role: repository-maintainer
created_at: 2026-08-14
updated_at: 2026-08-14
roadmap_stage: post-stage-11
source_access: repository_only
allowed_paths: [.github/workflows/validate.yml, project/knowledge-review-workflow.md, project/status/stage-11-knowledge-graph-impact-integrity.md, docs/operations/local-development.md, CHANGELOG.md, prompts/codex]
prohibited_actions: [commit, push, merge, source_body_access, knowledge_record_change, roadmap_change, stage_12_implementation, automatic_approval]
required_inputs: [AGENTS.md, accepted_ADR_0011, closed_stage_11_status, authorized_governance_and_CI_synchronization]
expected_outputs: [synchronized_knowledge_review_workflow, relationship_impact_CI_gate, synchronized_documentation_and_status]
validation: [yaml_parse, schema_validation, knowledge_validation, relationship_impact_validation, prompt_validation, roadmap_validation, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Synchronize reviewed relationship controls and CI

## Objective

Synchronize the approved Stage 9 knowledge-review workflow with the accepted
ADR-0011 and the human-approved, closed Stage 11 implementation. Add the
Stage 11 relationship/impact validator to the existing repository CI workflow.

## Required changes

- Replace the workflow's obsolete statement that automated impact traversal is
  planned with the implemented bounded, explicit-reference review procedure.
- Preserve canonical-data, stable-ID, classification, conflict, and human-review
  boundaries.
- Add `scripts/validate_relationship_impact.py` as a distinct CI validation
  step without removing or weakening existing checks.
- Synchronize current local-development documentation, Stage 11 status, prompt
  catalogue/documentation, and changelog wording.

## Boundaries

Do not inspect source bodies, change evidence or knowledge records, approve
content, modify roadmap state, implement Stage 12, or add automatic invalidation
or regeneration. The traversal result identifies potentially affected records;
it does not determine staleness or alter review state. Do not commit or push.

## Validation and report

Run every configured repository validator, YAML parsing, the complete automated
test suite, an offline documentation link check if available, and
`git diff --check`. Report hosted CI as not run from an uncommitted worktree.
List modified files, retained limitations, unresolved issues, and any remaining
human decisions.
