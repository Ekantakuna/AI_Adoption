# AI Adoption repository

This repository is the controlled working environment for an evidence-based AI
adoption outlook. It is intended to connect source inventory, evidence,
structured knowledge, assessment, project tracking, and audience-specific
publication while preserving provenance and human review.

The repository is not yet an end-to-end operating system. Metadata inventory
and repository operating documentation exist, while controlled extraction is
partial. Atomic evidence, structured knowledge contracts, most downstream
automation, reports, presentations, and incremental processing remain planned
or absent. See the [repository baseline](project/status/repository-baseline.md) for the
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
Definitions and lifecycle boundaries for source assets, metadata, extraction,
evidence, knowledge, assessments, and outputs are in
[information objects](docs/concepts/information-objects.md).

## Repository areas

| Area | Intended role | Current status |
| --- | --- | --- |
| `sources/`, `config/`, `schemas/` | Source inventory and controlled processing foundations | Partial; metadata catalogue and approved source schema exist, while source states conflict |
| `knowledge/`, `registers/` | Evidence and structured knowledge | Partial; two provisional synthesis notes and empty scaffolding |
| `assessments/`, `outlook/` | Assessment and outlook content | Planned/scaffolded |
| `project/` | Policies, decisions, reviews, and progress | Partial |
| `publications/`, `presentations/`, `website/` | Audience outputs | Planned/scaffolded |
| `scripts/`, `tests/`, `.github/` | Automation and validation | Absent; directories are scaffolds and no executable validators, tests, or CI workflow exist |
| `docs/` | Repository operating documentation | Implemented by the operating-model baseline |

The detailed accepted and prohibited contents for every area are in the
[repository map](docs/repository-map.md).

## Current source-of-truth boundaries

- Original source assets (original evidence): approved storage outside Git.
- Source inventory: `sources/catalogue.yaml`, by repository policy.
- Controlled values: `config/*.yaml`.
- Source schema: `schemas/sources.yaml`, approved in ADR 0002.
- Evidence and knowledge: two source-linked synthesis notes under `knowledge/`
  remain provisional. Atomic-evidence and structured-knowledge contracts are
  planned; extraction output is not automatically evidence or approved knowledge.
  Assessments remain planned/scaffolded.
- Project state: `project/status/`, relevant registers, and recorded decisions.
- Generated publications and presentations: derivatives, never the canonical
  evidence or knowledge record.

The canonical catalogue conflicts with the legacy source register, manifests,
and historical source-status reports. That conflict remains explicit and blocks
trustworthy new source processing pending authorized reconciliation.

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
