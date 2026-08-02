# Source management policy

Amendments made by an AI agent remain review proposals until an authorized
human reviewer accepts them.

## Scope

This policy controls source access for the AI Adoption Outlook project. It applies to original source documents held outside Git and to every repository derivative created from that evidence.

The approved local source root is:

`/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`

## Repository storage

Original source documents remain outside Git in the approved local source root or its subfolders. They must not be copied into Git, renamed, moved, or modified during inventory.

Git may store source metadata, hashes, source IDs, approved summaries,
normalized knowledge, and derived publications only when their classification
and approved handling route permit repository storage. Restricted or otherwise
non-trackable derivatives remain local-only.

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

- Use the approved source-processing authorization/run contracts and exact
  reconciliation matrix for every new body-processing operation.
- Record every approved route, tool, environment, and identified reviewer in an
  authorization record; preserve every execution in a hash-bound run record.
- Keep source-root verification and classification decisions paired in the same review checkpoint.

## Content-access history and current gate

Historical repository reports claim that approved local extraction and
source-linked synthesis occurred. The canonical catalogue, legacy register,
manifests, and those reports disagree about classification and processing
states, and the current tree has no historical processing-run record or
extracted corpus that makes the earlier process reproducible. Proposed run
contracts and a controlled text/HTML reader do not substantiate those earlier
claims. See the
[repository baseline](status/repository-baseline.md).

Before any new source body is opened, the source must have a stable source ID,
recorded metadata, approved classification, approved processing route, approved
extraction tool, and planned run. The 2026-08-02 reconciliation authorizes
fresh processing; it deliberately does not copy historical `extracted` claims
into the canonical catalogue. Prior reports do not authorize access or prove a
current run.

The approved authorization and execution controls are defined in
[source processing control policy](source-processing-control-policy.md). An
approved authorization still requires a recorded run before body access.

Extraction completion is not evidence or knowledge approval. Promotion of
extracted material into authoritative evidence, knowledge, assessment, or
publication requires the human review boundaries in
[information-handling rules](information-handling.md).
