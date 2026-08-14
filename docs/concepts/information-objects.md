# Information objects and lifecycle boundaries

## Purpose

This page is the authoritative terminology reference for the repository's main
information objects. It distinguishes original source material from metadata,
evidence from interpretation, canonical records from generated publications,
and local-only data from Git-tracked content.

## Object definitions

| Object | Definition | Canonical location or target | Current implementation |
| --- | --- | --- | --- |
| Source asset | An original file or other external item used as input. It is evidence in its original form and is not modified by repository processing. | Approved storage outside Git | External dependency recorded by policy and metadata; source bodies were not verified in this documentation review |
| Source metadata | Administrative facts about a source asset, such as stable ID, path, filename, size, hash, classification, and processing state. Metadata is not the source body and is not interpreted knowledge. | `sources/catalogue.yaml` | Implemented metadata inventory; classifications and fresh-processing states explicitly reconciled, while legacy historical views remain preserved |
| Manifest | A replaceable, metadata-only view of source records for a domain or processing purpose. | `sources/manifests/` | Partial; historical views exist but are not canonical current state |
| Extraction | A derivative representation of source content created by an approved tool and route. Extraction is not automatically reviewed evidence or approved knowledge. | Controlled local storage or an approved Git path, depending on classification | Partial; authorization/run contracts, validators, text/HTML and PPTX readers, and four technically verified private runs exist |
| Atomic evidence | One attributable observation or statement with a stable ID, precise source locator, provenance, classification, and review state. | `knowledge/evidence/` and `schemas/evidence.schema.yaml` | Partial; nine records validate, three are verified, and six await review |
| Knowledge record | An interpreted term, concept, framework, metric, risk, trend, use case, assumption, decision, reference, or relationship carrying an explicit review state. | Object-specific `knowledge/` subdirectory | Partial; three use cases validate, one is approved for its stated use, two remain drafts, and two root notes remain provisional |
| Assessment | A method-based evaluation such as current state, target state, gap, maturity, or impact. It is an interpretation, not original evidence. | Target: `assessments/` and applicable structured records | Planned/scaffolded |
| Project record | A status, risk, control, decision, initiative, dependency, milestone, metric, review, or meeting record used to govern the work. | `project/` and approved registers | Partial; policies and status notes exist, while most registers are empty |
| Publication | Audience-specific report content assembled from approved canonical inputs. | Target: `publications/` | Planned/scaffolded |
| Presentation | A slide-oriented derivative of an approved publication or the same approved canonical inputs. | Target: `presentations/` | Planned/scaffolded |
| Website output | A site derivative assembled from approved publication inputs. | Target: `website/` | Planned/scaffolded |

## Canonical and generated

A **canonical record** is the designated maintained record for an information
type. Git tracking alone does not make a record canonical or approved. A
canonical knowledge or assessment record must also have the required provenance,
classification, schema, and human review.

A **generated derivative** is a replaceable view or output created from
identified canonical inputs. Manifests, indexes, graph projections, rendered
reports, decks, and sites are generated derivatives when their generators are
implemented. They must not become the only copy of evidence, approvals, or
decisions.

## Local-only and Git-tracked

**Local-only** means stored outside version control in an approved location.
Original source assets are local/external to Git. Restricted derivatives and
other material whose handling route forbids repository storage are also
local-only.

**Git-tracked** means the information may be committed only after its
classification and handling route permit repository storage. Typical eligible
content includes approved metadata, hashes, summaries, normalized knowledge,
project records, and publication source. Ignore rules prevent accidental
tracking; they do not grant handling approval.

## Lifecycle and approval

| Object family | Identity | Lifecycle authority | Human-review boundary |
| --- | --- | --- | --- |
| Source metadata | Implemented `SRC-<group>-<six digits>` IDs | Source processing values in `config/source-types.yaml` and `project/source-management-policy.md` | Classification, processing route, tool approval, conflict resolution, and destructive identity changes |
| Evidence | Approved `EVID-<six digits>` Stage 9 contract | `config/review-statuses.yaml` and evidence schema | Promotion of extraction into verified/approved evidence |
| Knowledge and assessments | Approved Stage 9 knowledge prefixes; assessment IDs remain unapproved | Knowledge review statuses are implemented; assessment transitions remain planned | Approval of authoritative knowledge, current-state conclusions, target commitments, and conflict resolutions |
| Project records | ADR filename convention exists; other ID models are unapproved | General values plus future object-specific schemas | Approval according to the record owner's mandate; AI-authored policies and ADRs remain proposals |
| Publications, presentations, and sites | No approved ID models | Planned publication contracts | Publication-ready executive claims and audience release |

The general project lifecycle remains separate from Stage 9 knowledge review
statuses. See [knowledge statuses](../reference/knowledge-statuses.md) and
[knowledge identifiers](../reference/knowledge-identifiers.md). For object
families without a schema, do not add structured records or infer approval from
filenames, Git history, confidence, extraction state, or generated output.
