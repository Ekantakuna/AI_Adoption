# Repository map

Status reflects repository evidence at this baseline:
**implemented**, **partial**, **planned**, **absent**, or **unknown**. A directory
scaffold is not an operational capability.

| Directory | Purpose and accepted content | Prohibited content | Upstream inputs | Downstream consumers | Main validation | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `.github/` | GitHub collaboration configuration, issue templates, and workflows | Evidence, canonical knowledge, secrets | Repository policies and scripts | Contributors and CI | Knowledge validator and tests | Partial; Stage 9 validation workflow implemented |
| `assessments/` | Traceable current/target state, gaps, and maturity assessments | Unsupported conclusions or unlabeled AI approval | Reviewed evidence, knowledge, scoring models | Outlook, project views, publications | Planned assessment schemas/tests | Planned scaffold |
| `config/` | Controlled project values, taxonomies, source types, audiences, and scoring models | Evidence records or generated outputs | Approved governance decisions | All layers and validators | YAML parsing; schema validation is mostly absent | Partial |
| `docs/` | Authoritative repository architecture, governance, operations, and reference documentation | Source bodies or duplicated canonical records | Policies, implementation, decisions, status | Humans and agents | Link/documentation checks; no configured builder yet | Implemented operating-model docs |
| `knowledge/` | Controlled draft/reviewed evidence, terms, concepts, frameworks, metrics, risks, trends, use cases, assumptions, decisions, references, and relationships | Original source binaries, unsupported claims, false approval labels | Approved processing/evidence and review | Assessments, outlook, publications | Stage 9 knowledge validator and object schemas | Partial; nine evidence and three use-case records, including one completed Stage 10 pilot, plus two provisional notes |
| `outlook/` | Modular canonical outlook content by domain | Rendered decks, unsupported organizational decisions | Reviewed knowledge and assessments | Publications and presentations | Planned content/provenance checks | Planned scaffold |
| `presentations/` | Deck sources, themes, and replaceable generated presentations | Canonical evidence or the only copy of a claim | Approved reports/content and themes | Audience delivery | Planned renderer and traceability checks | Planned scaffold |
| `project/` | Information controls, ADRs, reviews, meeting notes, and stage status | Original evidence, silent conflict resolution | Repository activity and human decisions | Contributors, governance, progress views | Markdown review and planned status/ADR checks | Partial |
| `project/roadmap.yaml`, `project/roadmap/` | Machine-readable and human-readable stage sequencing, gates, lifecycle, and prompt boundary | Dates, unsupported estimates, execution claims, or automatic approval | Architecture, policies, status, schemas, and validation evidence | Human stage planning and one-at-a-time prompt generation | `scripts/validate_roadmap.py` and tests | Implemented; Stage 9.5 roadmap approved |
| `prompts/` | Versioned task and workflow instructions | Credentials, source bodies, rules that silently override precedence | Operating contract and stage design | Human and AI task execution | Prompt metadata/catalogue validator plus review against `AGENTS.md` | Partial; Codex library implemented |
| `publications/` | Audience-specific report sources and generated outputs with provenance | Unreviewed executive claims or canonical evidence-only records | Approved outlook, assessments, knowledge, audiences | Executives, board, employees, technical audiences | Planned publication validator/renderer | Planned scaffold |
| `registers/` | Canonical structured records for defined entity types | Records without approved object schema; source inventory authority | Approved records, controlled configuration | Knowledge, project views, publications | YAML parsing; object schemas mostly absent | Partial; ten empty registers plus legacy source snapshot |
| `schemas/` | Machine-readable validation contracts | Business content or generated results | Object and governance decisions | Validators and contributors | YAML parsing and partial knowledge contract enforcement | Partial; source and Stage 9 knowledge schemas |
| `scripts/` | Reproducible ingestion, validation, reporting, and publication utilities | Ad hoc source bodies, credentials, undocumented destructive operations | Schemas, configuration, canonical content | All automated workflows | Schema, knowledge, and source-processing tests | Partial; validators and controlled text/HTML and PPTX readers implemented |
| `sources/` | Canonical metadata catalogue, metadata-only manifests, processing authorizations/runs, approved notes, and controlled derivatives | Original source binaries; derivatives not approved for Git | External source metadata and handling decisions | Evidence processing and provenance | YAML/schema and source-processing integrity validation | Partial; 60 authorizations and four technically verified runs |
| `tests/` | Fixtures and automated checks for structure, schema, workflows, and generation | Production or sensitive source data | Scripts, schemas, expected contracts | Contributors and CI | `unittest` discovery | Partial; schema, knowledge, processing, and text/HTML and PPTX-reader tests implemented |
| `website/` | Website source/configuration and generated-site integration | Canonical-only knowledge or unreviewed claims | Approved publications and site templates | Website audience | Planned site build and link checks | Planned scaffold |

## Important subdirectories

| Path | Contract |
| --- | --- |
| `assessments/gaps/`, `assessments/target-state/` | Empty scaffolds for future assessment objects; no schema or lifecycle is implemented. |
| `docs/concepts/` | Authoritative definitions for repository information objects and their lifecycle boundaries. |
| `outlook/00-executive-summary/`, `outlook/05-business-domains/` | Empty section scaffolds; unlike other outlook sections, they do not yet have local README files. |
| `project/decisions/` | ADRs for material architectural choices; proposals remain pending human review. |
| `project/meeting-notes/`, `project/reviews/` | Empty scaffolds for future project records; no object schema or naming convention exists. |
| `project/status/` | Evidence-backed stage and baseline status records. |
| `prompts/{ingestion,analysis,synthesis,reporting,publication,system}/` | Empty workflow-category scaffolds. |
| `prompts/codex/bootstrap/` | Three saved prompts establish the operating model, review its documentation, and record existing decisions. |
| `prompts/codex/stages/` | Contains the stage-task template and active Stage 09 and Stage 10 prompts. |
| `prompts/codex/` | Versioned Codex prompt library with metadata catalogue, lifecycle policy, templates, planning, review, validation, and maintenance prompts. |
| `publications/{executive,board,employees,technical}/` | Empty audience-output scaffolds; no audience records, templates, or generator exist. |
| `scripts/{ingest,validate,report,publish}/` | Empty specialized scaffolds; implemented root scripts provide schema, knowledge, source-processing validation, and controlled text/HTML and PPTX reading. |
| `sources/manifests/` | Generated or maintained metadata-only views; the catalogue wins on conflict by current policy. |
| `sources/extracted/` | Controlled derivatives only after classification and storage review; original files never belong here. |
| `knowledge/*/` | Each controlled object directory has a README and non-production template; evidence and use-case directories also contain governed production records. |
| `presentations/generated/` | Replaceable output, ignored except for `.gitkeep`; never canonical. |

## Root files

- `AGENTS.md` is the authoritative agent contract.
- `ARCHITECTURE.md` is the authoritative layered architecture.
- `README.md` is the repository entry point.
- `CONTRIBUTING.md` defines the human and agent contribution workflow.
- `CHANGELOG.md` records notable repository changes.
- `requirements-validation.txt` pins the direct Python dependencies used by
  local and CI validation.
- `GEMINI.md` points other assistants to `AGENTS.md`.
- `.gitignore` excludes common secrets, local environments, build output,
  generated presentations, private extraction output, and key files; ignore
  rules are not information-handling approval.
- `.gitattributes` applies repository text-normalization rules.

Directory scope changes must update this map, the directory README, applicable
validation, status, and an ADR when the change is architectural.
