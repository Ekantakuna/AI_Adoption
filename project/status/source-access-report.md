# Source access report

## Status

- Verification date: 2026-07-21
- Repository branch: `setup/source-access`
- Source root: `/Users/maksimzakharenkau/Documents/AI/Outlook/2026/Inputs`
- Access method: filenames and basic filesystem metadata only
- Document-content analysis: not started

No document bodies were opened during source-access verification. No original source document was copied into the repository.

## Folder-access findings

The source root was accessible. It now contains 14 taxonomy-domain folders plus the standalone `glossary_vocabulary` knowledge-layer folder:

| Folder | Files observed recursively |
| --- | ---: |
| `strategic_intent` | 9 |
| `decision_environment` | 1 |
| `current_state` | 9 |
| `value_management` | 1 |
| `use_cases` | 4 |
| `organization` | 2 |
| `people_and_culture` | 1 |
| `governance` | 7 |
| `data` | 1 |
| `engineering_platform` | 3 |
| `security_trust` | 5 |
| `agentic_ai` | 3 |
| `ecosystem_sourcing` | 0 |
| `maturity_execution` | 2 |
| `glossary_vocabulary` | 1 |

The current scan observed 50 filesystem files: 41 source candidates and nine `.DS_Store` files. Observed source extensions were `.pdf`, `.docx`, `.pages`, `.html`, and `.mmd`. All scanned files reported readable filesystem permissions; no symbolic links, metadata-access errors, or files larger than 100 MB were observed.

The legacy folder names checked during the second verification no longer existed because their material had been relocated into taxonomy folders. Catalogue records must preserve the originally observed paths as path history rather than treating the taxonomy paths as the original evidence paths.

## Source-path custody decision

The current taxonomy-aligned paths are frozen as the source custody baseline effective 2026-07-21. The explicitly authorized reorganization completed before the source-management policy is retained as a historical exception. Sources will not be moved back because restoration would create another custody event. No further source rename or relocation is permitted without separate approval and a recorded path-history event.

### Approved glossary separation event

- Approval date: 2026-07-21
- Status: completed and metadata-verified
- From: `people_and_culture/glossary_vocabulary`
- To: `glossary_vocabulary`
- Scope: folder relocation only; original document filenames and contents remain unchanged
- Reason: establish glossary and vocabulary as a standalone cross-cutting knowledge layer and avoid conflating it with workforce and organizational readiness
- Required history: catalogue records retain `AI_Gloassary_Vocabluary` as the originally observed folder, `people_and_culture/glossary_vocabulary` as an intermediate path, and `glossary_vocabulary` as the current custody path
- Verification: the contained source filename, size, modification time, and permissions were unchanged by the folder move

### Approved value and use-case separation event

- Approval date: 2026-07-21
- Status: completed and metadata-verified
- From: `value_and_use_cases`
- To: `value_management` and `use_cases`
- Scope: folder and file relocation only; original document filenames and contents remain unchanged
- Reason: separate AI portfolio value definition, prioritization and monitoring from the catalogue of possible and implemented AI use cases
- Planned paths:
  - `value_and_use_cases/value_creation.mmd` to `value_management/value_creation.mmd`
  - `value_and_use_cases/general_use` to `use_cases/general_use`
  - `value_and_use_cases/telecom` to `use_cases/telecom`
  - `value_and_use_cases/use_cases` to `use_cases/catalogue`
- Required history: catalogue records retain originally observed, intermediate `value_and_use_cases`, and final split paths
- Verification: all five source candidates retained their filenames, sizes, modification times and permissions

The following metadata map preserves the folder-level history. `[trailing space]` identifies a literal trailing space in the originally observed folder name.

| Originally observed folder | Current relative folder |
| --- | --- |
| `AI_Adoption_General_Presentation_Draft` | `strategic_intent/general_presentation_draft` |
| `AI_Adoption_Vision ` `[trailing space]` | `strategic_intent/vision` |
| `AI_Adoption_Organization` | `organization/research` |
| `AI_Agency` | `agentic_ai/research` |
| `AI_Gloassary_Vocabluary` | `glossary_vocabulary` |
| `AI_Governance ` `[trailing space]` | `governance/research` |
| `AI_Maturity_Models_Adoption ` `[trailing space]` | `maturity_execution/models` |
| `AI_Prompt_and_Context_Engineering` | `engineering_platform/prompt_and_context_engineering` |
| `AI_Risks_Trust_SecurityManagement` | `security_trust/risks_trust_security_management` |
| `AI_Security` | `security_trust/security` |
| `AI_Telecom` | `use_cases/telecom` |
| `AI_Types_Traditional_and_Generative` | `engineering_platform/ai_types` |
| `AI_USE` | `use_cases/general_use` |
| `AI_Use_Cases ` `[trailing space]` | `use_cases/catalogue` |
| `Muscellaneous ` `[trailing space]` | `current_state/unclassified_research` |

The legacy `AI_adoption_MindMap` folder was split by filename as follows:

| Originally observed file | Current relative file |
| --- | --- |
| `AI_adoption_MindMap/AI_DATA.mmd` | `data/overview.mmd` |
| `AI_adoption_MindMap/AI_ENGINEERING.mmd` | `engineering_platform/overview.mmd` |
| `AI_adoption_MindMap/AI_ORGANIZATION.mmd` | `organization/overview.mmd` |
| `AI_adoption_MindMap/AI_PEOPLE_and_CULTURE.mmd` | `people_and_culture/overview.mmd` |
| `AI_adoption_MindMap/AI_STRATEGY.mmd` | `strategic_intent/strategy.mmd` |
| `AI_adoption_MindMap/AI_VALUE_CREATION.mmd` | `value_management/value_creation.mmd` |
| `AI_adoption_MindMap/AI_VISION.mmd` | `strategic_intent/vision.mmd` |
| `AI_adoption_MindMap/GOVERNANCE.mmd` | `governance/overview.mmd` |

Additional renamed paths are preserved here:

| Originally observed path | Current relative path |
| --- | --- |
| `technologys-generational-moment-with-generative-ai-a-cio-and-cto-guide.pdf` | `decision_environment/technology-generational-moment-generative-ai-cio-cto-guide.pdf` |
| `AI_Governance /Adaptive_Governance` | `governance/research/adaptive_governance` |
| `AI_Governance /Governance_Policies_and_Howto` | `governance/research/governance_policies_and_how_to` |

## Ignored items

The nine `.DS_Store` files are operating-system metadata and must be excluded from inventory and extraction. Other ignored names and patterns are controlled by `config/source-types.yaml`. Ignored status does not authorize deletion from the local source root.

## Unresolved security and classification decisions

Content access remains blocked pending these decisions:

- approve a classification and processing route for every source candidate;
- determine whether strategy, vision, general-presentation, organization, governance-policy, use-case, telecom, and mind-map material is internal or restricted;
- determine whether security and risk material requires on-premises-only processing;
- confirm whether the governance policy document contains restricted operational information;
- review Gartner-labelled material and other vendor publications for license and redistribution limits;
- confirm that no source contains credentials, personal data, or restricted operational data;
- approve local extraction tools for PDF, DOCX, Pages, HTML, and MMD files;
- determine whether any PDF is encrypted, damaged, image-only, or requires OCR;
- approve local hashing before suspected duplicates are compared;

Filename-based domain placement and public-source impressions are unverified inferences, not classification decisions.

### Deferred decision log

Decision owner status on 2026-07-22: all items below are explicitly deferred and remain pending until the owner returns to them. Deferral is not approval and does not change any source classification, processing route, taxonomy relationship, tool authorization, rights status or content-access gate.

| Decision ID | Pending decision | Current effect |
| --- | --- | --- |
| `SRC-DEC-001` | Final classification and local or external processing route for each source | All 42 sources remain blocked from content access. |
| `SRC-DEC-002` | Approved extraction tools for PDF, DOCX, Pages, HTML and MMD | No extraction tool may open a source document. |
| `SRC-DEC-003` | Approval or rejection of folder-derived domain relationships | `domain_ids` remain empty; `proposed_domain_ids` are non-canonical. |
| `SRC-DEC-004` | Authorization for local hashing and duplicate confirmation | Hash fields remain unset and the duplicate candidate remains suspected. |
| `SRC-DEC-005` | Licensing and permitted-use review for Gartner and other vendor material | Rights status remains pending and repository derivatives are prohibited. |
| `SRC-DEC-006` | Security review for governance, security, risk, strategy and operational material | No security-sensitive source may advance to a content-access state. |

## Metadata-only inventory

Status: completed on 2026-07-22 without opening document bodies or calculating hashes.

- 42 source candidates are catalogued in `registers/sources.yaml` with stable source IDs. The additional `governance/research/GOVERNANCE.mmd` candidate was detected during the 2026-07-22 governance-foundation work; it was not created or modified by the repository workflow.
- Current file-type totals are 30 PDF, 9 MMD mind-map, 1 DOCX, 1 Pages and 1 HTML record.
- Nine `.DS_Store` files are excluded under the configured ignore rules.
- All records remain `metadata_catalogued`, `classification: pending` and `processing_route: pending`.
- Confirmed `domain_ids` remain empty; folder-derived taxonomy mappings are retained only as `proposed_domain_ids`.
- Two metadata-matched items are recorded as suspected duplicates, not confirmed duplicates; local hashing remains deferred pending approval.
- No symbolic link was followed, no extraction tool was invoked and no source-derived conclusion was created.

## Access gate

Document-content analysis has not yet started. No source content may be opened for analysis or sent to an external model until its classification and approved processing route are recorded. Generated derivatives must inherit the highest classification of all contributing sources.

## Approved current-state source structure

Status: created and metadata-verified on 2026-07-22. All listed directories are empty. Their creation did not move existing evidence and does not authorize content access.

The approved metadata-only collection paths are:

- `current_state/implemented_use_cases/marketing_product_management`
- `current_state/implemented_use_cases/customer_care`
- `current_state/implemented_use_cases/ict/software_engineering`
- `current_state/implemented_use_cases/ict/cyber_defence`
- `current_state/implemented_use_cases/ict/cyber_defence_centre`
- `current_state/implemented_use_cases/ict/service_monitoring`
- `current_state/implemented_use_cases/cross_cutting/shadow_ai`
- `current_state/shared_platforms/data`
- `current_state/shared_platforms/models`
- `current_state/shared_platforms/cloud`
- `current_state/shared_platforms/governance`
- `current_state/shared_platforms/security`
- `current_state/shared_platforms/monitoring`
- `current_state/project_summaries`

All folders begin with classification and processing route pending. Shadow AI, cyber-defence, production architecture and data-governance evidence require an explicit security decision before extraction.

## Approved maturity source structure

The following local structure is approved for creation. The existing `maturity_execution/maturity_models` folder is approved for relocation to `maturity_execution/models`; its contained filename and content must remain unchanged.

- `maturity_execution/framework`
- `maturity_execution/models`
- `maturity_execution/assessment_inputs/qualitative`
- `maturity_execution/assessment_inputs/quantitative`
- `maturity_execution/assessment_reports`
- `maturity_execution/action_plans`

Custody event:

- Approval date: 2026-07-22
- Status: completed and metadata-verified
- From: `maturity_execution/maturity_models`
- To: `maturity_execution/models`
- Scope: folder relocation only; original document filenames and contents remain unchanged
- Reason: separate maturity framework, reference models, assessment evidence, reports and action plans for understandable future ingestion
- Verification: the existing PDF retained its filename, size, modification time and permissions; all new collection folders are empty

All maturity sources begin with classification and processing route pending. No model characteristic, level or assessment conclusion has been extracted.
