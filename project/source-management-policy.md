# Source management policy

## Scope

This policy controls source access for the AI Adoption Outlook project. It applies to original evidence held under the local source root and to every repository derivative created from that evidence.

The approved local source root is:

`/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`

Original source documents remain in their existing local source folders. They must not be copied into Git, renamed for taxonomy normalization, or sent to an external model before the controls below are satisfied.

### Source-path custody baseline

The current source paths under the approved local source root are frozen as the custody baseline effective 2026-07-21, including the separately approved standalone `glossary_vocabulary` collection. A taxonomy reorganization was explicitly authorized and completed before this policy was recorded. That event and the later recorded glossary separation are custody-history events, not permission for further source renaming.

The pre-policy paths and current custody paths are recorded in `project/status/source-access-report.md`. Future catalogue records must preserve both as `original_relative_path` and `current_relative_path`, with the reorganization represented in `path_history`. Restoring the pre-policy layout would create another custody event and is not required. Any future source move or rename requires separate approval and a recorded path-history event before execution.

Cross-cutting source collections may exist as standalone children of the source root when they are knowledge layers rather than taxonomy domains. Their metadata must identify the applicable `knowledge_layer_ids`; domain relationships remain optional and separate.

## Original evidence and repository derivatives

Original evidence is the source file as held under the local source root. Its filename, current relative path, file size, modification time, and approved content hash form part of its provenance. The repository records metadata about original evidence but does not store the evidence itself.

Repository derivatives include source metadata, hashes, source IDs, extraction records, approved summaries, and normalized knowledge. A derivative must link back to its source IDs and extraction records. It must not contain credentials, personal data, or restricted operational data.

For Markdown and text types, `original_in_git: conditional` applies only to repository-native project content and approved repository derivatives. It never permits original evidence from the local source root to be copied into Git. Conditional content still requires an approved classification and processing route and, when derived, complete source provenance.

Generated content inherits the highest classification of all contributing sources. A derivative with any source whose classification or processing route is pending remains blocked from content generation and publication.

## Processing states

Only the following source-processing states are allowed:

- `discovered`: the path is known; document content has not been opened.
- `metadata_catalogued`: permitted filesystem metadata has been registered in the canonical source inventory.
- `classification_pending`: a final classification has not been approved.
- `approved_for_processing`: final classification and general processing eligibility are approved, but document content access is not yet authorized.
- `approved_local`: content may be processed only with the recorded approved local tools and route.
- `approved_external`: content may be sent only to the specifically approved external service and account recorded in the processing route.
- `extraction_in_progress`: approved extraction is underway.
- `extracted`: extraction completed, but the output is not yet approved.
- `reviewed`: extraction and handling were reviewed and accepted.
- `rejected`: the source was assessed and is not approved for processing.
- `superseded`: a newer source record replaces this source for active use; the record remains for provenance.
- `unreadable`: the source cannot be extracted with the approved tools in its current form.

## Approval hierarchy and transitions

`approved_for_processing` is an administrative eligibility state, not content-access authorization. It requires a final classification and a compatible approved tool. A source in this state must transition to exactly one route-specific approval state before its content is opened:

- `approved_local` requires the `local` route, approved local tool, approver, and approval date.
- `approved_external` requires the `external` route, specifically approved service, approved account, approved purpose, approver, and approval date.

The route-specific states are mutually exclusive for a processing event. Movement into `approved_local` or `approved_external` requires an approved final classification and processing route. `approved_external` is not implied by public classification. A public source with no explicit external-route approval remains prohibited from external processing.

Only `approved_local`, `approved_external`, `extraction_in_progress`, `extracted`, and `reviewed` authorize continued content access under the previously approved route. Extraction may begin only from `approved_local` or `approved_external`. The allowed state transitions and routes are controlled in `config/source-types.yaml`; transitions not listed there are prohibited.

The following conditions are invalid:

- opening or extracting content directly from `approved_for_processing`;
- processing a source whose classification is `pending`;
- using an external service under a `local`, `pending`, or `prohibited` route;
- granting `approved_external` solely because classification is `public`;
- changing between local and external processing without a new route-specific approval event.

## Classification states

- `pending`: workflow sentinel; not a final classification and blocks content access.
- `public`: may be processed by approved local and cloud tools.
- `internal`: may be processed only by company-approved tools and accounts.
- `restricted`: must remain in approved on-premises environments.

Classification approval must identify the reviewer, approval date, basis, and permitted processing route. Generated content uses the highest applicable final classification in this order: `public`, `internal`, `restricted`. A contributing `pending` source blocks generation rather than being treated as a lower classification.

## Provenance and naming

Catalogue records preserve the source root ID, originally observed filename and relative path, current filename and relative path, and complete known path history. The pre-policy reorganization map in the source-access report is the authoritative starting point for those fields. Absolute local paths must not be embedded in generated publications.

Taxonomy spelling is normalized in repository labels and metadata only. Source files must not be renamed for spelling normalization. Existing filenames are evidence and remain unchanged unless a separately approved source-custody action requires otherwise.

## Source-ID assignment

Each source receives exactly one ID using the source-category prefix controlled in `config/source-types.yaml` and a six-digit sequence allocated monotonically within that prefix. Sequences start at `000001`, are never reused, and remain reserved when a source is rejected, superseded, unreadable, or otherwise inactive.

Prefix assignment uses the longest matching `current_relative_path` rule. A source with no matching rule remains unassigned until its primary source category is reviewed; `miscellaneous` must not be used as an automatic fallback. Sources spanning multiple topics still receive one primary source category and one prefix. Additional topics are recorded separately in `domain_ids` and do not create additional source IDs.

A source ID and its prefix are immutable after assignment. Moving a source, correcting taxonomy, changing classification, or adding domain relationships must not change the ID. The catalogue records `source_category`, `prefix_assignment_basis`, and any secondary domain relationships so that the assignment remains auditable.

When a dedicated source category is introduced after an ID was assigned, the existing ID remains unchanged. `prefix_assignment_basis` must record the legacy prefix, while the current category, domain proposal and extraction targets follow the approved current-path routing.

Source categories are routing labels, not automatically taxonomy domains. The default relationships in `config/source-types.yaml` are proposed metadata defaults and require review; empty defaults such as `glossary`, `scope`, and `miscellaneous` require explicit domain assignment when applicable.

## Ignored files

The inventory and extraction workflow ignores operating-system metadata, editor locks, and incomplete downloads listed in `config/source-types.yaml`. Ignoring a file means excluding it from source registration and processing; it does not authorize deletion.

Potential duplicates and version-labelled files are not ignored. They remain separate source candidates until an approved local hash comparison establishes their relationship.

## Content-access gate

Document-content analysis has not started. Before any source body is opened, the source must have a stable source ID, recorded metadata, approved classification, approved processing route, and a compatible approved extraction tool.
