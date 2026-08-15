---
id: PRM-CODEX-MAINT-012-CONTROLS
title: Implement approved Stage 12 entry controls
type: maintenance
version: 1.0.2
status: active
owner_role: repository-maintainer
created_at: 2026-08-15
updated_at: 2026-08-15
roadmap_stage: stage-12-entry
source_access: repository_only
allowed_paths: [config/audiences.yaml, config/scoring_models.yaml, config/README.md, schemas, scripts/validate_schemas.py, scripts/README.md, tests/test_schema_validation.py, tests/README.md, docs, assessments/README.md, publications/README.md, project/decisions, project/status, CHANGELOG.md, prompts/codex]
prohibited_actions: [commit, push, merge, source_body_access, assessment_schema_creation, assessment_content_creation, outlook_content_creation, scoring_model_creation, additional_audience_creation, stage_12_execution, automatic_approval]
required_inputs: [AGENTS.md, accepted_ADR_0012, approved_unscored_first_assessment, approved_AUD_000001, approved_ownership_assignments, authorized_configuration_implementation]
expected_outputs: [unscored_entry_configuration, AUD_000001_configuration, configuration_schemas, schema_validation_tests, synchronized_documentation_and_status]
validation: [yaml_parse, schema_validation, knowledge_validation, relationship_impact_validation, prompt_validation, roadmap_validation, tests, link_check, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Implement approved Stage 12 entry controls

## Objective

Implement only the Stage 12 entry controls approved by MZ on 2026-08-15:

- an explicitly unscored initial assessment mode with no scoring models; and
- `AUD-000001` version `1.0.0`, Internal assessment reviewers, with its approved
  permissions, prohibitions, ownership, and review metadata.

## Required implementation

Populate `config/scoring_models.yaml` and `config/audiences.yaml` without adding
any other model or audience. Add narrowly scoped Draft 2020-12 schemas, connect
them to existing schema validation, and add synthetic tests for valid and
invalid configurations. Document identity, lifecycle, inputs, outputs,
ownership, review, operation, and limitations.

The unscored mode prohibits numeric and ordinal scores, weights, aggregation,
ranking, and implied maturity levels. It requires explicit claim types, reviewed
upstream references, visible missing/disputed evidence, and human approval
boundaries.

`AUD-000001` permits only `public` and `internal` review material through
approved tools/accounts. It prohibits restricted/unclassified material, source
bodies, secrets, credentials, unapproved personal information, false authority,
silent conflict resolution, and public/external release.

## Boundaries

Do not create assessment schemas or records, outlook content, scoring models,
additional audiences, or Stage 12 outputs. Do not alter approved semantics,
access source bodies, approve content, commit, or push.

## Validation and report

Run every repository validator, full tests, YAML parsing, offline link checks,
and `git diff --check`. Report hosted CI and the documentation build accurately.
Stage 12 remains blocked by the uncommitted Stage 11 branch state even if these
configuration controls validate.
