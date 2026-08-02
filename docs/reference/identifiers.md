# Identifier rules

## Purpose

Stable identifiers connect source metadata, evidence, knowledge, assessment,
project records, and outputs without depending on filenames or display titles.
An identifier is never reused for a different object.

## Implemented identifiers

| Object | Format or value | Authority | Status |
| --- | --- | --- | --- |
| Project | `AI-ADOPTION` | `config/project.yaml` | Implemented |
| Source root | `SROOT-0001` | `config/source-types.yaml` and source catalogue | Implemented, but the absolute path is machine-specific |
| Source | Prefix plus six-digit sequence, for example `SRC-AGT-000001` | Existing catalogue and `config/source-types.yaml` prefixes | Implemented |

Configured source prefixes are:

| Key | Prefix |
| --- | --- |
| glossary | `SRC-GLO` |
| scope | `SRC-SCO` |
| vision | `SRC-VIS` |
| organization | `SRC-ORG` |
| agentic AI | `SRC-AGT` |
| governance | `SRC-GOV` |
| maturity | `SRC-MAT` |
| security | `SRC-SEC` |
| risk and trust | `SRC-RSK` |
| use cases | `SRC-UC` |
| telecom | `SRC-TEL` |
| prompt context | `SRC-PRM` |
| presentation drafts | `SRC-PRE` |
| miscellaneous | `SRC-MIS` |

The prefix expresses the allocation group, not permanent semantic ownership.
Moving a source or changing its domain does not by itself change its ID.

## Source identity lifecycle

- Allocate an ID once a source candidate enters the approved catalogue
  workflow.
- Preserve it across filename and path changes; record history.
- Keep duplicates as separate candidates until their relationship is reviewed.
- Use `duplicate_of` or its approved equivalent rather than deleting identity.
- Mark replacement through a supersession relationship/state; do not recycle the
  old ID.
- Cite the ID in downstream evidence and knowledge.

The approved canonical catalogue schema retains the catalogue's `id` field.
The legacy register's `source_id` field remains a compatibility difference and
must be mapped explicitly during a reviewed migration; it is not permission to
rename or reallocate identifiers. See
`project/decisions/0002-canonical-source-catalogue-schema.md`.

## Planned identifiers

No approved formats exist for atomic evidence, knowledge claims, assessments,
risks, controls, decisions, initiatives, milestones, metrics, publications,
presentations, processing runs, or graph relationships. Their registers being
present does not define an ID model.

Before adding records, approve an object-specific schema defining uniqueness,
allocation, immutability, references, supersession, validation, and ownership.
Do not invent prefixes in task-specific content.

ADR filenames use a zero-padded sequence such as
`project/decisions/0001-repository-operating-model.md` for ordering. This is a
documentation filename convention, not yet a structured decision-register ID.

## Validation

The approved catalogue schema checks identifier format. Repository-level
validation must additionally check uniqueness, referential integrity, configured
prefixes, non-reuse, and supersession relationships. No such automated
repository validator currently exists.
