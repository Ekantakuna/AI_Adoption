---
id: PRM-CODEX-MAINT-SOURCE
title: Process source metadata changes
type: maintenance
version: 1.0.0
status: active
owner_role: source-processing-owner
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: future-source-processing
source_access: metadata_only
allowed_paths: [sources/catalogue.yaml, sources/processing-authorizations.yaml, sources/processing-runs.yaml, config, schemas, project/status, knowledge]
prohibited_actions: [commit, push, source_body_access, source_modification, automatic_approval, stable_id_reuse]
required_inputs: [source_metadata_diff, approved_processing_route]
expected_outputs: [change_inventory, reprocessing_proposal, stale_object_report, processing_run_proposal, review_packet]
validation: [source_metadata_validation, hash_comparison, reference_checks, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Process source metadata changes

This is a future controlled procedure, not an assertion that incremental
processing is operational. First verify that future stages have implemented
source change detection, dependency impact, run recording, and review controls;
otherwise report the prerequisite as absent and stop before body access.

Within an approved metadata-only route, inventory new, changed, moved, and
removed sources; compare hashes; preserve stable source IDs and provenance;
propose reprocessing; identify potentially stale evidence/knowledge and other
downstream objects; and prepare a processing-run record. Do not open source
bodies, alter original sources, approve knowledge, or silently reconcile
conflicts. Require human review of classification, route, tool, reprocessing,
and downstream impact. Validate metadata, references, hashes where available,
and `git diff --check`; report facts, proposals, prerequisites, and unresolved
issues without committing or pushing.
