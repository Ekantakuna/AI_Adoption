# Sources

This directory contains source metadata, manifests, source notes, and controlled extraction areas; classification review is required before processing source documents.

The canonical source inventory is `../registers/sources.yaml`. `catalogue.yaml` points to that register and is not an independent source-record store.

The `extracted/private/` path is excluded from Git. Other extracted artifacts are not automatically excluded; they may be tracked only after classification and information-handling review confirms that repository storage is permitted.

## Source-access boundary

The original evidence remains under the local source root recorded in `config/source-types.yaml`. Original source documents must not be copied into this repository. This directory may contain only approved metadata, hashes, manifests, extraction records, summaries, and normalized derivatives that comply with `project/source-management-policy.md`.

Original evidence and repository derivatives are different custody layers:

- original evidence remains in its existing local folder with its filename and path preserved in the catalogue;
- repository derivatives contain traceable information produced through an approved processing route and link back to stable source IDs.

Metadata-only inventory is complete for the 42 currently known source candidates; document-content analysis has not started. `approved_for_processing` does not authorize content access. A source may be opened only after it has a stable ID, final classification, compatible approved tool, and either `approved_local` or `approved_external` route-specific approval.

## Source inventory

`registers/sources.yaml` remains the canonical source inventory. Its records conform to `schemas/source.schema.yaml` and can be reproduced with the guarded metadata scanner documented in `scripts/README.md`. Manifest conventions are documented in `manifests/README.md`, while controlled formats, states, ignored patterns, and source-ID prefixes are defined in `config/source-types.yaml`.

Source-ID prefixes represent controlled source categories rather than taxonomy domains. Each source receives one immutable prefix through the configured current-path rules; additional taxonomy relationships are recorded separately.

The local `glossary_vocabulary` source collection is a standalone cross-cutting knowledge-layer input. It uses `SRC-GLO`, maps to `knowledge_layer_ids: [glossary_vocabulary]`, and does not receive `people_and_culture` automatically.

Current-state technical evidence remains outside Git under the local `current_state` source collection. New evidence should be placed in the controlled business-domain or shared-platform folders documented in the source-access report, then catalogued and classified before content access. Existing `current_state/unclassified_research` material remains untouched until reviewed.

Maturity evidence remains outside Git under `maturity_execution`. The local collection separates framework descriptions, reference models, qualitative and quantitative assessment inputs, assessment reports and action plans. A document's folder proposes its record target but does not approve its classification or conclusions.

Decision-environment evidence remains outside Git under `decision_environment`. New sources use `SRC-DEC` and may propose decision target, type, context, choice-architecture, evidence, authority, outcome, learning and assessment records. The previously catalogued `SRC-SCO-000001` keeps its stable legacy ID while its routing metadata uses the dedicated decision-environment category.
