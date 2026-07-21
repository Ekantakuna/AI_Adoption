# Source manifests

This directory is reserved for repository-safe metadata records about original evidence. It must not contain original source documents or unapproved source content.

## Required identity and provenance fields

- `source_id`
- `source_root_id`
- `original_filename`
- `original_relative_path`
- `current_filename`
- `current_relative_path`
- `path_history`
- `domain_ids`
- `source_type`
- `extension`
- `size_bytes`
- `filesystem_modified_at`
- `hash_algorithm`
- `content_hash`
- `hash_calculated_at`

The originally observed and current paths are both required when a source was previously relocated. Paths are relative to the controlled source root; manifests must not expose unnecessary workstation details in publications.

## Required handling fields

- `processing_state`
- `classification`
- `classification_basis`
- `classification_reviewed_by`
- `classification_reviewed_at`
- `processing_route`
- `processing_route_approved_by`
- `processing_route_approved_at`
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
- `derived_classification`
- `review_status`

Hashes and extraction metadata may be populated only through an approved processing route. Potential duplicates remain independent records until an approved local hash comparison confirms equivalence.

Document-content analysis has not started. Initial manifests must contain metadata only and use `pending` classification or processing states wherever a decision has not been approved.
