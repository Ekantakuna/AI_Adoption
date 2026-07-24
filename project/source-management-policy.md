# Source management policy

## Scope

This policy controls source access for the AI Adoption Outlook project. It applies to original source documents held outside Git and to every repository derivative created from that evidence.

The approved local source root is:

`/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`

## Repository storage

Original source documents remain outside Git in the approved local source root or its subfolders. They must not be copied into Git, renamed, moved, or modified during inventory.

Git stores source metadata, hashes, source IDs, approved summaries, normalized knowledge, and derived publications.

Repository derivatives must link back to the source IDs and provenance that produced them.

## Classifications

The approved source classifications are:

- `public`
- `internal`
- `restricted`
- `unclassified`

`unclassified` is an inventory state only. It means the source has been identified but not yet approved for classification-based processing.

## Processing states

The approved source-processing states are:

- `discovered`
- `metadata_catalogued`
- `classification_pending`
- `approved_for_processing`
- `extraction_in_progress`
- `extracted`
- `reviewed`
- `rejected`
- `superseded`
- `unreadable`
- `blocked`

`metadata_catalogued` records files and filesystem metadata only. `approved_for_processing` means a source may proceed under the recorded processing route.

## Handling rules

Generated content inherits the highest classification of its sources.

Source content must not be sent to an external AI service unless the source classification and the approved processing route permit it.

No credentials, personal data, or production datasets may be added without explicit approval.

Metadata inventory is not content analysis. Recording filenames, paths, sizes, hashes, and similar catalog fields does not authorize opening or interpreting the document body.

## Inventory rules

Renaming, moving, or modifying original source files during inventory is prohibited.

Ignored-file handling is defined in `config/source-types.yaml`. Ignoring a file excludes it from source registration and processing; it does not authorize deletion.

Potential duplicates and version-labelled files remain separate candidates until the catalogue records their relationship.

## Recommendations

- Approve the register-specific schema for `registers/sources.yaml` before adding records.
- Record the approved extraction tools and review trail for each source type before body processing starts.
- Keep source-root verification and classification decisions paired in the same review checkpoint.

## Content-access gate

Document-content analysis has not started. Before any source body is opened, the source must have a stable source ID, recorded metadata, approved classification, approved processing route, and an approved extraction tool.
