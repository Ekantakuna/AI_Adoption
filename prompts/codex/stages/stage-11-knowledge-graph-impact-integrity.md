---
id: PRM-CODEX-STAGE-011
title: Implement knowledge graph and impact integrity
type: stage
version: 1.0.0
status: active
owner_role: stage-implementer
created_at: 2026-08-14
updated_at: 2026-08-14
roadmap_stage: stage-11
source_access: repository_only
allowed_paths: [AGENTS.md, ARCHITECTURE.md, README.md, CHANGELOG.md, config, knowledge, schemas, scripts, tests, docs, project/status, project/decisions, project/roadmap.yaml, project/roadmap/implementation-roadmap.md, project/roadmap, prompts/codex]
prohibited_actions: [commit, push, merge, rewrite_git_history, source_body_access, new_extraction, bulk_knowledge_extraction, canonical_record_duplication, implicit_relationship_inference, automatic_knowledge_approval, automatic_adr_approval, stage_10_record_change, stage_12_implementation, automatic_invalidation_or_regeneration]
required_inputs: [AGENTS.md, approved_roadmap, closed_stage_10_review, approved_relationship_identifier_contract, approved_traversal_contract, canonical_knowledge_records]
expected_outputs: [relationship_lifecycle_contract, impact_reference_validator, synthetic_traversal_tests, stage_11_status, human_review_package]
validation: [yaml_parse, schema_validation, knowledge_validation, relationship_impact_validation, repository_validation, prompt_validation, roadmap_validation, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Stage 11 — Knowledge graph and impact integrity

## Objective and roadmap authority

Implement only `stage-11` of approved roadmap `ROADMAP-000001`: controlled
relationship traversal and impact references for reviewed knowledge. The graph
is a derived navigation and integrity capability. Canonical evidence and
knowledge records remain authoritative and must not be replaced by a competing
graph store.

Read `AGENTS.md`, both approved roadmap representations, the roadmap lifecycle,
Stage 10 status and review packet, relevant accepted ADRs and policies, current
knowledge contracts and records, validators, tests, CI, documentation, and Git
state before editing.

## Entry gate

Confirm from repository evidence that:

- the Stage 10 pilot is complete and its mandatory human review is closed;
- the stable relationship identifier contract is approved; and
- the traversal contract is approved.

Record the supporting path for every criterion. If any criterion is missing or
ambiguous, report `STAGE-11 ENTRY GATE: BLOCKED` and stop. Do not create or
approve a missing entry-gate contract merely to make this prompt executable.

## Source and canonical-data boundary

This is repository-only work. Do not inspect external source documents or
private extraction derivatives, perform extraction, or modify source content.
Existing repository evidence and knowledge may be inspected only as governed
records.

Traversal must resolve explicit stable-ID references to canonical repository
objects. A derived index, in-memory graph, or traversal result is replaceable
and must not duplicate claims or become a second source of truth. Preserve all
stable IDs, provenance, classifications, review states, and visible conflicts.

## Required scope

Deliver the roadmap-required:

- relationship lifecycle contract;
- impact-reference validator and controlled traversal;
- synthetic traversal and integrity tests; and
- `project/status/stage-11-knowledge-graph-impact-integrity.md`.

Implement only the supporting schema, configuration, CI, and documentation
changes necessary for those deliverables. Do not implement Stage 12 assessment
or outlook contracts, or Stage 16 change detection, invalidation, and
regeneration.

## Relationship contract

Define and document:

- permitted relationship types, directions, semantics, subjects, and objects;
- stable `REL-NNNNNN` identity and non-reuse rules;
- creation, review, rejection, deprecation, and supersession lifecycle;
- evidence and human-review requirements;
- explicit conflict representation without silent reconciliation;
- invalid relationship behavior;
- behavior for missing, rejected, deprecated, or superseded endpoints; and
- traversal boundaries.

Relationships must arise only from explicit repository records. Similar words
or inferred semantic proximity do not establish a relationship. Evidence-backed
relationships retain their evidence references.

## Traversal and impact behavior

Provide a documented, reproducible operation that can identify from explicit
references:

- knowledge objects that depend on an evidence record;
- objects explicitly related to a knowledge object;
- reviewed knowledge potentially affected by an upstream change; and
- downstream records that reference a given canonical object.

Define direction, controlled depth, cycle handling, repeated-node handling,
missing-node behavior, and deprecated/superseded-node behavior. Preserve
conflicts in traversal results. Do not mutate, invalidate, or regenerate
affected records automatically.

Differentiate structurally invalid cycles from legitimate reciprocal or
conceptual links and from repeated traversal paths. Do not assume every cycle
is an error.

## Integrity validation and tests

Validation must identify at least:

- dangling source and target endpoints;
- unknown IDs and relationship types;
- prohibited self-relations where the relationship semantics prohibit them;
- duplicate relationship IDs and invalid review states;
- missing evidence references;
- deprecated or superseded references where policy requires an error or
  warning; and
- impact chains that cannot resolve to canonical objects.

Use temporary synthetic fixtures rather than fake production knowledge. Cover
a valid one-hop relationship, valid multi-hop traversal, dangling source,
dangling target, unknown relationship type, duplicate relationship ID, missing
evidence, cycle policy, deprecated-object behavior, upstream impact traversal,
and preservation of canonical-object boundaries.

## Documentation, status, and decisions

Document what the repository knowledge graph means and does not mean;
relationship lifecycle; traversal and impact semantics; canonical versus
derived data; validation; operational use; limitations; and the future Stage 16
boundary. Update affected architecture, concept, operations, directory, schema,
repository-map, prompt-library, and changelog documentation.

Create an ADR proposal only if implementation requires a material architectural
decision not already approved. Leave every AI-authored ADR proposed until an
authorized human records approval.

The Stage 11 status must cite entry-gate evidence, implemented files,
relationship and traversal models, validation, tests, limitations, unresolved
conflicts, exit-gate evidence, human-review state, and Stage 12 readiness. Do not
mark Stage 11 complete or update the roadmap to `implemented` before human
review.

## Validation and exit gates

Run all available repository checks, including:

```text
python scripts/validate_schemas.py
python scripts/validate_source_processing.py
python scripts/validate_knowledge.py
python scripts/validate_prompts.py
python scripts/validate_roadmap.py
python -m unittest discover -s tests -p "test_*.py"
git diff --check
git status --short
```

Also run the Stage 11 relationship/impact validator, YAML parsing, and available
documentation/link checks. Report unavailable checks rather than treating them
as passed.

Assess explicitly whether dangling and cyclic behavior is documented and
validated, canonical boundaries remain intact, and authorized human review is
recorded. Demonstrate whether explicit references identify affected downstream
objects while unresolved conflicts remain visible. Leave the stage in review
until the human-review gate is recorded.

## Git and final report

Do not commit, push, merge, rewrite history, or modify Stage 10 reviewed
records. Stop after preparing a concise human-review package listing files,
relationship types, lifecycle and traversal rules, cycle and impact policies,
validator behavior, synthetic tests, validation results, unresolved issues,
ADR proposals, proposed status transition, and exact human decisions required.
