# Changelog

All notable repository-foundation changes are documented in this file.

## Unreleased

### Added

- Draft Stage 9.5 master roadmap, stage lifecycle/template documentation,
  roadmap validator, tests, and human-review status record.
- Approved-roadmap-derived Stage 10 evidence-to-knowledge pilot prompt with
  metadata-only source access and explicit human-review gates.

- Stage 9 controlled knowledge types, evidence confidence, and review statuses.
- Atomic evidence and knowledge-object schemas, directory contracts, and
  non-production templates.
- An object-specific schema for contextual `REF` knowledge records.
- Knowledge management/extraction/review policies and operating documentation.
- Knowledge integrity validator, temporary-fixture `unittest` suite, and GitHub
  validation workflow.
- Pinned validation dependencies and executable Draft 2020-12 meta-schema,
  source-catalogue, and production knowledge-record validation.
- Stage 9 implementation status and explicit provisional-note migration path.
- Repository operating model and target layered architecture.
- Documentation index, repository map, information-flow, agent-operation,
  publication-pipeline, governance, local-development, identifier, and status
  references.
- Evidence-backed repository baseline under `project/status/`.
- Proposed Architecture Decision Record for the repository operating model.
- Approved Draft 2020-12 schema and decision record for the canonical source
  catalogue shape.
- Proposed ADRs recording seven existing evidence-backed decisions: external
  source storage and metadata-only cataloguing, Markdown/YAML canonical formats,
  stable identifiers, evidence/knowledge separation, human approval boundaries,
  derivative publications, and agent documentation obligations.
- Architectural-decision review status with evidence and explicitly excluded
  future decisions.
- Version-controlled Codex bootstrap, maintenance, and stage-template prompts.
- Source-processing authorization and run schemas/registers,
  controlled route/tool configuration, integrity validator, templates, and a
  gated repository text/HTML reader.
- Approved source-state reconciliation preserving historical conflicts, with
  57 identified route/tool/environment authorizations and one blocked source.
- Controlled pilot `RUN-000001` for `SRC-ORG-000005`, with verified input hash,
  private ignored derivative, recorded output hash, and human verification of
  technical provenance.
- First atomic evidence draft, `EVID-000001`, with a precise run/line locator,
  inherited internal classification, and subsequent human verification limited
  to the evidence statement.
- Metadata-only inventory records `SRC-UC-000012`–`000014` for three new
  implemented-use-case PPTX files, plus an approved, synthetic-tested local
  PPTX slide-text reader and enforceable per-tool approval states.
- Verified private runs `RUN-000002`–`000004`, eight source-attributed atomic
  evidence drafts, and three evidence-backed semantic use-case drafts for Smart
  Chat Bot, AI Speech Analytics Assistant, and Life Registration.
- Repository purpose, contribution guidance, and information-handling rules.
- Project configuration and controlled taxonomy.
- Empty structured YAML registers.
- Directory-level purpose documentation and repository placeholders.

### Changed

- `ROADMAP-000001` was approved by Maksim Zakharenkau on 2026-08-08; future
  stage prompt generation remains separate from stage execution.

- Stage 9 policies, controlled contracts, and ADRs 0005–0007 were approved by
  Maksim Zakharenkau; the stage is closed with explicit deferred limitations.
- Source-processing policy, configuration, schemas, and ADR 0010 were approved;
  the canonical catalogue is reconciled and processing validation is in CI.
- ADRs 0001, 0003–0004, and 0008–0009 were accepted by Maksim Zakharenkau with
  their documented implementation limitations.
- Knowledge documentation now distinguishes the empty structured framework from
  the two preserved legacy/provisional synthesis notes.
- Architecture and repository maps now report knowledge contracts and integrity
  validation as partial implementations rather than absent capabilities.
- `AGENTS.md` is now the authoritative, detailed repository agent contract.
- The source catalogue schema now validates the canonical catalogue shape as
  approved in ADR 0002 instead of describing the incompatible legacy register.
- Source-type configuration includes an additional, currently unenforced
  `ignore_patterns` list; its overlap with `ignored_files` remains unresolved.
- Root documentation distinguishes operational, partial, planned, absent, and
  unknown capabilities.
- Documentation review clarified information-object definitions and lifecycles,
  local-only versus Git-tracked data, evidence/knowledge boundaries, historical
  source-status conflicts, and scaffold-only directory status.
- Documentation-review evidence and remaining approval items are recorded in
  `project/status/documentation-review.md`.
- Directory READMEs now state whether their capabilities are partial, planned,
  or absent and identify missing schemas, identifiers, review gates, commands,
  and automation.
- Source inventory ownership is assigned to `sources/catalogue.yaml`.
- Repository paths use a portable repository-relative value.
- Historical status records now point to the Stage 9 validation follow-up
  instead of presenting their earlier validator/test/CI absence as current.

### Unreleased

- Established the version-controlled Codex prompt library, metadata catalogue,
  prompt policy, validator, and operating documentation.

### Fixed

- Stage 9 knowledge validation now reports malformed non-string references and
  controlled values as validation errors instead of terminating with a type
  error.
- Direct execution of the controlled repository text reader now resolves its
  source-processing validator import correctly.

### Known issues

- Historical legacy source states remain preserved and differ from the approved
  fresh-processing states; they are non-canonical and not silently superseded.
- The Pages source has no approved tool, and no successful reviewed processing
  run or production evidence exists.
- Documentation builds, knowledge-graph traversal, incremental processing,
  reporting, and presentation generation are not implemented.

No strategy conclusions or new source-derived findings are included in this
operating-model change.
