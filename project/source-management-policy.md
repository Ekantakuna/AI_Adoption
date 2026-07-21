# Source management policy

## Scope

This policy controls source access for the AI Adoption Outlook project. It applies to original evidence held under the local source root and to every repository derivative created from that evidence.

The approved local source root is:

`/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`

Original source documents remain in their existing local source folders. They must not be copied into Git, renamed for taxonomy normalization, or sent to an external model before the controls below are satisfied.

## Original evidence and repository derivatives

Original evidence is the source file as held under the local source root. Its filename, current relative path, file size, modification time, and approved content hash form part of its provenance. The repository records metadata about original evidence but does not store the evidence itself.

Repository derivatives include source metadata, hashes, source IDs, extraction records, approved summaries, and normalized knowledge. A derivative must link back to its source IDs and extraction records. It must not contain credentials, personal data, or restricted operational data.

For Markdown and text types, `original_in_git: conditional` applies only to repository-native project content and approved repository derivatives. It never permits original evidence from the local source root to be copied into Git. Conditional content still requires an approved classification and processing route and, when derived, complete source provenance.

Generated content inherits the highest classification of all contributing sources. A derivative with any source whose classification or processing route is pending remains blocked from content generation and publication.

## Processing states

Only the following source-processing states are allowed:

- `discovered`: the path is known; document content has not been opened.
- `metadata_recorded`: permitted filesystem metadata has been registered.
- `classification_pending`: a final classification has not been approved.
- `route_pending`: classification is known but the processing route is not approved.
- `approved_local`: content may be processed with the recorded approved local tools.
- `approved_external`: content may be sent only to the specifically approved external service and account.
- `extraction_in_progress`: approved extraction is underway.
- `extracted`: extraction completed, but the output is not yet approved.
- `reviewed`: extraction and handling were reviewed and accepted.
- `blocked`: processing is prohibited until the recorded issue is resolved.
- `retired`: the source record is retained for provenance but is no longer active.

Movement into `approved_local` or `approved_external` requires an approved final classification and processing route. `approved_external` is not implied by public classification.

## Classification states

- `pending`: workflow sentinel; not a final classification and blocks content access.
- `public`: may be processed by approved local and cloud tools.
- `internal`: may be processed only by company-approved tools and accounts.
- `restricted`: must remain in approved on-premises environments.

Classification approval must identify the reviewer, approval date, basis, and permitted processing route. Generated content uses the highest applicable final classification in this order: `public`, `internal`, `restricted`. A contributing `pending` source blocks generation rather than being treated as a lower classification.

## Provenance and naming

Catalogue records preserve the source root ID, originally observed filename and relative path, current filename and relative path, and any known path history. Absolute local paths must not be embedded in generated publications.

Taxonomy spelling is normalized in repository labels and metadata only. Source files must not be renamed for spelling normalization. Existing filenames are evidence and remain unchanged unless a separately approved source-custody action requires otherwise.

## Ignored files

The inventory and extraction workflow ignores operating-system metadata, editor locks, and incomplete downloads listed in `config/source-types.yaml`. Ignoring a file means excluding it from source registration and processing; it does not authorize deletion.

Potential duplicates and version-labelled files are not ignored. They remain separate source candidates until an approved local hash comparison establishes their relationship.

## Content-access gate

Document-content analysis has not started. Before any source body is opened, the source must have a stable source ID, recorded metadata, approved classification, approved processing route, and a compatible approved extraction tool.
