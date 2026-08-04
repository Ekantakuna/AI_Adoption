# Status values

Several status vocabularies serve different purposes. They must not be silently
mapped to one another.

## Capability implementation status

Used by repository architecture and status baselines:

| Value | Meaning |
| --- | --- |
| `implemented` | Repository artifacts demonstrate a usable capability. |
| `partial` | Some elements exist, but the capability is incomplete, inconsistent, manual, or not reproducible. |
| `planned` | Intent or scaffolding exists without operating implementation. |
| `absent` | No implementation evidence was found. |
| `unknown` | Repository evidence is insufficient for a conclusion. |

Narrative architecture may say “partially implemented” for `partial` and “not
yet implemented” for `planned` or `absent`, provided the precise baseline value
is clear.

## General content lifecycle

`config/project.yaml` defines:

| Value | Meaning |
| --- | --- |
| `proposed` | Suggested but not accepted for review as a working draft. |
| `draft` | Work in progress; not approved. |
| `in_review` | Submitted to an authorized reviewer. |
| `approved` | Explicitly accepted by an authorized human within their mandate. |
| `superseded` | Retained for traceability but replaced by a linked newer item. |
| `retired` | No longer active; retained according to governance rules. |

Only the value list is currently machine-controlled. Object-specific transition
rules and reviewer fields are not yet defined.

## Source processing status

`config/source-types.yaml` and `project/source-management-policy.md` define:

| Value | Meaning |
| --- | --- |
| `discovered` | Candidate identified; metadata may be incomplete. |
| `metadata_catalogued` | Metadata recorded; body access is not authorized by this state. |
| `classification_pending` | Handling classification awaits review. |
| `approved_for_processing` | Recorded classification and route permit the next approved processing step. |
| `extraction_in_progress` | Approved extraction has begun but is incomplete. |
| `extracted` | The approved extraction step reports completion; this does not mean knowledge approval. |
| `reviewed` | Processing output has received its required review. |
| `rejected` | Candidate or output was rejected with retained rationale. |
| `superseded` | Replaced by a linked source/version and retained for traceability. |
| `unreadable` | The selected tool cannot read the source. |
| `blocked` | A recorded control or tool limitation prevents progress. |

The catalogue and approved schema use the record field `processing_status`; the
configuration and policy describe the vocabulary as processing states. The
values align. ADR 0002 retains this distinction rather than renaming records
during the unresolved source-state reconciliation.

## Other source statuses

The catalogue defines readability values `readable`, `unreadable`, `blocked`,
and `unknown`, plus duplicate values `unique`, `possible_duplicate`,
`exact_duplicate`, and `unknown`. These describe distinct concerns and must not
be substituted for processing status.

Classification values are `public`, `internal`, `restricted`, and
`unclassified` for source inventory. `config/project.yaml` omits
`unclassified`, while source-specific configuration includes it. Use the
source-specific vocabulary for source inventory and do not silently reconcile
the difference.

## Approval boundary

AI-created content cannot move itself to `approved`. Extraction completion,
high confidence, Git tracking, or publication rendering also does not imply
human approval.

## Known status conflict

At this baseline, `sources/catalogue.yaml` records 57 sources as `unclassified`
and most as `metadata_catalogued`; the legacy source register, manifests, and
status documents claim later classification and processing states. The
catalogue is authoritative by policy, but the discrepancy requires human-led
reconciliation. Do not select the most advanced status automatically.
