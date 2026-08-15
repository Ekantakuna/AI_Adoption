# AI Adoption repository

This repository is the controlled working environment for an evidence-based AI
adoption outlook. It is intended to connect source inventory, evidence,
structured knowledge, assessment, project tracking, and audience-specific
publication while preserving provenance and human review.

The repository is not yet an end-to-end operating system. Metadata inventory,
controlled processing, and knowledge validation exist. Stage 9 established the
knowledge contracts; a bounded Stage 10 evidence-to-knowledge pilot is closed
with human-reviewed records. Stage 11 bounded relationship/impact traversal is
implemented and closed with human-approved exit gates; its capability remains
partial. Reports, presentations, assessments, and incremental invalidation
remain planned. See the
[repository baseline](project/status/repository-baseline.md) for the
evidence-backed status of each capability.

## Target information flow

The target flow is:

**Source assets → metadata catalogue → content processing → atomic evidence →
structured knowledge → relationships and impact analysis → assessments and
progress views → reports → presentations**

This is a target architecture, not a claim that each step operates today.
[ARCHITECTURE.md](ARCHITECTURE.md) defines the layers, boundaries, review
points, and current implementation status.

## Operating principles

- Never invent company facts or unsupported evidence.
- Label facts, assumptions, inferences, and recommendations.
- Preserve provenance and stable identifiers.
- Keep original source assets outside Git and follow
  [information-handling rules](project/information-handling.md).
- Treat reviewed Markdown and YAML registers as canonical repository content;
  treat generated outputs as reproducible derivatives.
- Require authorized human review for authoritative knowledge, organizational
  conclusions, commitments, and publication-ready executive claims.
- Represent conflicts explicitly; do not silently normalize them.

Repository agents must follow [AGENTS.md](AGENTS.md). Contributors should start
with [CONTRIBUTING.md](CONTRIBUTING.md) and the
[documentation index](docs/index.md).
Material Codex work uses the version-controlled [Codex prompt library](prompts/codex/README.md),
whose lifecycle and execution procedure are documented in
[Using the Codex prompt library](docs/operations/using-codex-prompt-library.md).
The approved [master implementation roadmap](project/roadmap/implementation-roadmap.md)
defines the controlled sequence for later work; it does not make planned stages
operational.
Definitions and lifecycle boundaries for source assets, metadata, extraction,
evidence, knowledge, assessments, and outputs are in
[information objects](docs/concepts/information-objects.md).

## Repository areas

| Area | Intended role | Current status |
| --- | --- | --- |
| `sources/`, `config/`, `schemas/` | Source inventory and controlled processing contracts | Partial |
| `knowledge/`, `registers/` | Evidence and structured knowledge | Partial; validated records and completed bounded Stage 10 pilot plus two provisional notes |
| `assessments/`, `outlook/` | Assessment and outlook content | Planned/scaffolded |
| `project/` | Policies, decisions, reviews, and progress | Partial |
| `publications/`, `presentations/`, `website/` | Audience outputs | Planned/scaffolded |
| `scripts/`, `tests/`, `.github/` | Automation and validation | Partial; schema/knowledge and relationship/impact validation, tests, and CI are implemented |
| `docs/` | Repository operating documentation | Implemented by the operating-model baseline |

The detailed accepted and prohibited contents for every area are in the
[repository map](docs/repository-map.md).

## Current source-of-truth boundaries

- Original source assets (original evidence): approved storage outside Git.
- Source inventory: `sources/catalogue.yaml`, by repository policy.
- Controlled values: `config/*.yaml`.
- Source schema: `schemas/sources.yaml`, approved in ADR 0002.
- Evidence and knowledge: schema-conforming records under `knowledge/`, subject
  to classification and human review. The directories initially contain no
  production records; extraction output is not automatically evidence or
  approved knowledge. Nine evidence and three use-case records exist;
  `EVID-000001`–`000003` are verified and `USECASE-000001` is approved for its
  stated semantic use. Assessments remain planned/scaffolded.
- Project state: `project/status/`, relevant registers, and recorded decisions.
- Generated publications and presentations: derivatives, never the canonical
  evidence or knowledge record.

The source-state conflict was explicitly reconciled on 2026-08-02. Historical
legacy states remain preserved but do not override the canonical catalogue.
Sixty sources have approved processing authorizations; the Pages source remains
blocked. Four controlled runs succeeded and are technically verified. Three
AI-origin atomic evidence statements are human-verified; six evidence and two
use-case records remain `needs_review`.

## Contributing

1. Work on a dedicated branch.
2. Inspect relevant implementation, documentation, configuration, schemas,
   tests, status, and Git state.
3. Confirm information classification and the approved processing route.
4. Update implementation, documentation, status, and decisions together.
5. Run applicable validation and review the complete diff.
6. Do not commit or push through an agent without explicit permission.

Local commands and current validation limitations are documented in
[local development](docs/operations/local-development.md).
