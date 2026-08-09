---
id: PRM-CODEX-STAGE-010
title: Run the reviewed evidence-to-knowledge pilot
type: stage
version: 1.0.0
status: active
owner_role: stage-implementer
created_at: 2026-08-08
updated_at: 2026-08-08
roadmap_stage: stage-10
source_access: metadata_only
allowed_paths: [AGENTS.md, ARCHITECTURE.md, README.md, config, knowledge, schemas, scripts, tests, docs, project/status, project/roadmap.yaml, project/roadmap/implementation-roadmap.md, sources/README.md, sources/catalogue.yaml, sources/processing-authorizations.yaml, sources/processing-runs.yaml, CHANGELOG.md]
prohibited_actions: [commit, push, source_body_access, source_modification, new_extraction, wholesale_provisional_note_migration, automatic_approval, unsupported_claims]
required_inputs: [AGENTS.md, approved_roadmap, stage-09-status, validated_processing_controls, candidate_provenance]
expected_outputs: [pilot_evidence_review_packet, selected_knowledge_review_proposals, justified_relationship_proposals, pilot_review_report, stage-10-status]
validation: [yaml_parse, schema_validation, knowledge_validation, source_processing_validation, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Stage 10 — Run the reviewed evidence-to-knowledge pilot

## Objective

Run a deliberately small, traceable pilot from existing verified processing-run
metadata and candidate records to atomic evidence, selected knowledge, and
relationships. Preserve draft, review, classification, provenance, and conflict
boundaries. The pilot must demonstrate traceability without claiming that the
broader knowledge framework or downstream pipeline is operational.

## Roadmap authority and preconditions

Read `AGENTS.md`, `project/roadmap.yaml`, and
`project/roadmap/implementation-roadmap.md`. This prompt implements only
`stage-10` of approved roadmap `ROADMAP-000001`.

Before editing, confirm:

- `ROADMAP-000001` has `status: approved` and `review_status: approved`.
- Stage 09 is closed and its knowledge, schema, and review controls validate.
- Source-processing authorizations and runs validate, including provenance and
  evidence-eligible run review.
- Candidate evidence and knowledge records have stable IDs and repository-held
  provenance metadata.
- A named authorized human reviewer is available for source-fidelity review and
  any promotion to `verified` or `approved`.
- Git branch, status, and relevant diff have been inspected.

If a prerequisite fails, stop implementation, record the blocker in the stage
status, and do not bypass the gate.

## Scope

- Select a small pilot set from existing validated runs and candidate records.
- Check source-ID, authorization-ID, run-ID, input/output hash, classification,
  locator, and evidence/knowledge references against repository metadata.
- Prepare or correct only the minimum atomic evidence and selected knowledge
  records needed to demonstrate run → evidence → knowledge traceability.
- Prepare relationship records only where both endpoints and supporting evidence
  are explicit and the relationship is justified by the available record.
- Preserve all conflicts, exclusions, uncertainty, and limitations for review.
- Produce a review packet that identifies the exact records requiring human
  source-fidelity, semantic, and authority decisions.
- Update the Stage 10 status record with implemented, partial, planned, absent,
  and unknown capabilities and repository paths.

## Out of scope

- Do not implement Stage 11 or any later stage.
- Do not create graph traversal, impact invalidation, assessments, publications,
  presentations, or incremental-processing automation.
- Do not migrate `knowledge/current_state_search_20.md` or
  `knowledge/public-source-analysis.md` wholesale.
- Do not perform new extraction or open external source-document bodies.
- Do not copy source files or extraction derivatives into Git.
- Do not change source IDs, catalogue records, authorization records, or run
  provenance to make a candidate pass.
- Do not mark AI-created evidence or knowledge `verified` or `approved`; do not
  record human approval on behalf of a reviewer.
- Do not silently reconcile conflicting claims, terms, classifications, or
  statuses.

## Source and information boundary

Metadata-only source access is allowed for the repository paths listed in the
front matter. External source-document bodies and local extraction derivatives
are outside this prompt's access boundary. Existing repository candidate text
may be inspected only as a draft record; it is not source-body authorization.
Generated material inherits the highest classification of its inputs. Original
source files must never be modified.

## Required implementation and outputs

Use the existing approved schemas, controlled values, templates, validators, and
review workflow. Create or update only the directly related pilot records and
documentation:

- a bounded evidence review packet with source, run, locator, classification,
  confidence, review state, and unresolved questions;
- selected knowledge records that cite valid evidence IDs and retain AI-origin
  and draft/needs-review status until human review;
- relationship proposals with valid endpoints and supporting evidence, if
  justified;
- `project/status/stage-10-reviewed-evidence-knowledge-pilot.md`;
- directly required README, schema/reference, operations, or changelog updates;
- an ADR proposal only if the pilot introduces a material architectural decision.

Do not add records to an empty register without an approved schema. Preserve
stable identifiers and use controlled values from `config/`.

## Human review and exit gates

The agent prepares a reviewable pilot and may validate technical integrity. An
authorized human must review source fidelity, semantic interpretation,
classification, conflicts, and any promotion to `verified` or `approved`.

The stage may close only when:

- every promoted record has eligible processing-run provenance;
- human review identity, decision, and date are recorded where required;
- conflicts and exclusions remain explicit;
- no provisional note was migrated wholesale;
- run-to-evidence-to-knowledge references validate; and
- the Stage 10 status records the result, limitations, and unresolved issues.

If human review is pending, leave the stage in review or partial status and do
not claim completion.

## Documentation and validation

Document what changed and why, inputs and outputs, identifiers and lifecycle,
relationships, ownership/review responsibility, operating procedure,
validation, downstream consumers, and limitations. Run:

```text
python scripts/validate_schemas.py
python scripts/validate_source_processing.py
python scripts/validate_knowledge.py
python -m unittest discover -s tests -p "test_*.py"
git diff --check
git status --short
```

Also run YAML parsing and all applicable repository validators. A documentation
builder is not configured; do not report one as passing. Link checking may be
run if available. Validators do not grant source access or human approval.

## Git and final report

Do not commit, push, merge, rewrite history, or delete branches. Preserve
pre-existing worktree changes and do not modify unrelated files. Report files
inspected, created, modified, and deleted; implementation decisions;
documentation; validation results; human-review state; unresolved issues; and
the recommended next action.
