---
id: PRM-CODEX-PLAN-012-CONTROLS
title: Prepare Stage 12 scoring and audience control proposal
type: planning
version: 1.0.0
status: retired
owner_role: roadmap-maintainer
created_at: 2026-08-14
updated_at: 2026-08-15
roadmap_stage: stage-12-entry
source_access: repository_only
allowed_paths: [project/decisions, project/status, docs, config/README.md, CHANGELOG.md, prompts/codex]
prohibited_actions: [commit, push, merge, source_body_access, fill_scoring_configuration, fill_audience_configuration, stage_12_implementation, automatic_policy_approval, automatic_audience_authorization]
required_inputs: [AGENTS.md, approved_roadmap, closed_stage_10_and_stage_11_status, existing_information_handling_and_human_review_decisions, empty_scoring_and_audience_placeholders]
expected_outputs: [proposed_scoring_and_audience_control_ADR, stage_12_entry_gate_assessment, human_review_items]
validation: [yaml_parse, prompt_validation, roadmap_validation, tests, link_check, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Prepare Stage 12 scoring and audience control proposal

## Objective

Prepare, but do not approve or implement, the scoring and audience controls
required by the approved roadmap before Stage 12 execution. Derive the proposal
from accepted information-handling, human-authority, canonical-data, and
publication decisions.

## Required proposal

Record a proposed ADR that defines:

- scoring-model identity, versioning, lifecycle, scale semantics, missing-value
  behavior, evidence/provenance, confidence separation, aggregation rules,
  conflicts, and human approval;
- audience identity, lifecycle, purpose, classification bounds, prohibited
  content, claim/release controls, and human authorization;
- canonical versus derivative boundaries; and
- exact unresolved human choices needed before the Stage 12 gate can pass.

Existing directory names are scaffolding, not approved audience identities or
permissions. Empty configuration is not authority to invent a scale,
classification matrix, audience, or organizational target.

## Boundaries and validation

Leave `config/scoring_models.yaml` and `config/audiences.yaml` empty until the
proposal is human-approved and implementation is separately authorized. Do not
create assessment schemas or records, generate outlook content, access source
bodies, modify roadmap status, execute Stage 12, commit, or push.

Validate prompt metadata, roadmap consistency, repository tests, links, YAML,
and the Git diff. Report `STAGE-12 ENTRY GATE: BLOCKED` while either control is
unapproved.
