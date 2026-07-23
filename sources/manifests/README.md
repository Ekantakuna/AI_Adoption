# Source manifests

This directory is reserved for repository-safe metadata records about original evidence. It must not contain original source documents or unapproved source content.

## Required identity and provenance fields

- `source_id`
- `source_category`
- `prefix_assignment_basis`
- `source_root_id`
- `original_filename`
- `original_relative_path`
- `current_filename`
- `current_relative_path`
- `path_history`
- `domain_ids`
- `proposed_domain_ids`
- `knowledge_layer_ids`
- `business_domain_ids`
- `ai_technique_ids`
- `proposed_record_types`
- `source_type`
- `extension`
- `size_bytes`
- `filesystem_modified_at`
- `hash_algorithm`
- `content_hash`
- `hash_calculated_at`

The originally observed and current paths are both required when a source was previously relocated. Paths are relative to the controlled source root; manifests must not expose unnecessary workstation details in publications.

For sources affected by the pre-policy taxonomy reorganization, initialize these fields from the authoritative path map in `project/status/source-access-report.md`. Use the current path as the custody baseline, retain the pre-policy path as the originally observed path, and record the dated reorganization in `path_history`.

Each manifest has exactly one primary `source_category`, selected by the longest matching current-path rule in `config/source-types.yaml`. Multi-topic relationships belong in `domain_ids`; they do not create additional source IDs. Once assigned, `source_id` and its prefix are immutable. Sequence numbers are allocated monotonically per prefix and are never reused.

Glossary sources use `source_category: glossary` and `knowledge_layer_ids: [glossary_vocabulary]`. They do not receive `people_and_culture` automatically; any domain relationship requires separate review.

Decision-environment sources use `source_category: decision_environment`, the `SRC-DEC` prefix for new IDs, and proposed decision-domain record targets. The previously assigned `SRC-SCO-000001` remains stable; its `prefix_assignment_basis` records the legacy prefix while current routing supplies the decision-environment category and proposed relationships.

## Required handling fields

- `processing_state`
- `classification`
- `classification_basis`
- `classification_reviewed_by`
- `classification_reviewed_at`
- `processing_route`
- `processing_route_approved_by`
- `processing_route_approved_at`
- `approved_external_service`
- `approved_account`
- `approved_purpose`
- `contains_personal_data`
- `contains_credentials`
- `contains_restricted_operational_data`
- `rights_or_license_status`
- `handling_notes`

## Required extraction and relationship fields

- `extraction_record_ids`
- `approved_tool`
- `tool_version`
- `ocr_required`
- `duplicate_status`
- `duplicate_of_source_id`
- `approved_summary_ref`
- `normalized_knowledge_refs`
- `candidate_record_refs`
- `field_evidence_refs`
- `derived_classification`
- `review_status`

Hashes and extraction metadata may be populated only through an approved processing route. Potential duplicates remain independent records until an approved local hash comparison confirms equivalence.

Document-content analysis has not started. Initial manifests must contain metadata only, use `processing_state: metadata_catalogued`, `classification: pending` and `processing_route: pending`, and leave all hash fields unset. Folder-derived taxonomy relationships belong in `proposed_domain_ids`; `domain_ids` remains empty until review approves the relationship.

Each record must conform to `schemas/source.schema.yaml`. Metadata inventory may read directory entries and basic filesystem metadata only. It must not calculate hashes, inspect document bodies, follow symbolic links or invoke an extraction tool.

`approved_for_processing` records general eligibility only and must not be used as content-access authorization. A manifest must reach exactly one of `approved_local` or `approved_external` before extraction begins. External approval requires the named service, account, purpose, approver, and approval date; public classification alone is insufficient.

Extraction from current-state collections may propose records only for the target types controlled in `config/record-types.yaml`. Every proposed field must retain an evidence reference; candidate records remain non-canonical until human review.
