# AI Adoption Outlook

This repository is the working foundation for a traceable AI adoption outlook. It stores project configuration, structured registers, project knowledge, assessment material, report content, and publication assets as Markdown and YAML.

The repository currently contains foundation scaffolding only. It does not contain approved strategy conclusions, and source documents must not be processed until their classification and handling requirements have been reviewed.

## Working principles

- Never invent company facts.
- Distinguish facts, assumptions, inferences, and recommendations.
- Preserve provenance from sources through analysis and publication.
- Preserve stable record identifiers.
- Treat Markdown and YAML registers as canonical content.
- Follow [the information-handling rules](project/information-handling.md).

## Repository structure

| Directory | Purpose |
| --- | --- |
| `.github/` | GitHub-specific workflows and collaboration templates. |
| `assessments/` | Current-state, target-state, gap, and maturity assessments. |
| `config/` | Project-wide controlled values and taxonomy. |
| `knowledge/` | Traceable assumptions, decisions, evidence, glossary terms, and references. |
| `outlook/` | Modular source content for the AI adoption outlook. |
| `presentations/` | Presentation sources, themes, and generated output. |
| `project/` | Project controls, reviews, meeting notes, and status material. |
| `prompts/` | Reusable prompts grouped by workflow stage. |
| `publications/` | Audience-specific publication outputs. |
| `registers/` | Structured YAML records used across the repository. |
| `schemas/` | Machine-readable validation contracts. |
| `scripts/` | Ingestion, validation, reporting, and publication utilities. |
| `sources/` | Source metadata, manifests, notes, and controlled extraction areas. |
| `tests/` | Fixtures and automated repository checks. |
| `website/` | Website source and configuration. |

Each top-level directory contains its own short `README.md` describing its intended scope.

## Configuration and records

- [Project configuration](config/project.yaml) defines project metadata and allowed status, confidence, and classification values.
- [Taxonomy](config/taxonomy.yaml) defines the controlled domain identifiers and cross-cutting knowledge layers.
- `registers/sources.yaml` is the canonical source inventory; `sources/catalogue.yaml` is only a pointer to that register and must not contain independently maintained source records.
- `registers/terms.yaml` is the canonical glossary and vocabulary inventory; glossary terms are cross-cutting and are not owned by the `people_and_culture` domain.
- Each file in `registers/` has a common foundation structure consisting of `schema_version`, `register`, and an initially empty `records` list.
- Record schemas and workflow automation remain foundation work; do not add incompatible ad hoc fields before those contracts are agreed.

## Contribution workflow

1. Work on a branch.
2. Classify information before adding or processing it.
3. Add provenance and stable identifiers to structured records.
4. Run available Markdown and YAML checks.
5. Review `git status` and the diff before requesting approval to commit.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules. Do not commit or push through an automated agent without explicit permission.
