# Repository baseline

> Historical baseline: the capability table and validation baseline record the
> repository as inspected on 2026-07-30. Stage 9 subsequently added schema and
> knowledge validators, tests, and CI. See
> [stage-09-knowledge-framework.md](stage-09-knowledge-framework.md) for the
> current validation state. The source-state conflict recorded here was
> subsequently resolved by the separately approved reconciliation and source-
> processing controls on 2026-08-02; see
> [source-processing-approval.md](source-processing-approval.md). ADRs 0001 and
> 0003–0009 were also subsequently accepted; the table below remains the
> historical 2026-07-30 snapshot.

## Scope and method

This baseline records repository evidence inspected on 2026-07-30 for the
repository operating-model stage. It does not inspect or analyze external source
document bodies. Source metadata and repository-held documentation were
inspected.

Classification values are:

- **implemented**: a usable capability is evidenced in repository artifacts;
- **partial**: some elements exist, but are incomplete, inconsistent, manual, or
  not reproducible;
- **planned**: intent or scaffolding exists without an operating implementation;
- **absent**: no implementation evidence was found;
- **unknown**: repository evidence is insufficient.

This document reports evidence, not approval of source-derived knowledge.

## Repository findings before the operating-model changes

- The repository was on branch `setup/repository-operating-model`.
- `config/source-types.yaml` had a pre-existing uncommitted formatting and
  ignore-pattern change.
- `prompts/codex/` was pre-existing and untracked, including the saved prompt
  for this stage.
- Root guidance, contribution, information-handling, and source-management
  documents existed but did not fully define the requested layered operating
  model.
- `docs/` and its architecture/governance/operations/reference subdirectories
  existed but contained no tracked documentation.
- The source inventory, source schema, configuration, manifests, legacy source
  snapshot, and three source-stage status notes existed.
- Ten non-source registers were empty, audience and scoring configuration files
  were empty, and only a source schema existed.
- No executable scripts, automated tests, CI workflows, documentation build
  configuration, knowledge graph, report generator, or presentation generator
  was found.

## Capability baseline

| Component | Status | Repository evidence | Finding |
| --- | --- | --- | --- |
| Repository purpose and operating documentation | implemented | `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/` | The operating-model documentation now defines purpose, boundaries, flow, and operation; human review of proposed policy/ADR remains required. |
| Information handling | implemented | `project/information-handling.md`, `project/source-management-policy.md` | Classification and source-access gates are documented. Enforcement automation is absent. |
| Source type configuration | partial | `config/source-types.yaml`, `config/project.yaml`, `config/taxonomy.yaml`, `sources/catalogue.yaml` | Source groups, routes/states, classifications, root, taxonomy domains, and ID prefixes exist. The root path is machine-specific, source/general classification vocabularies differ, `glossary` is used by the catalogue but absent from the taxonomy, and no contract maps catalogue source type `image` to source group `images`. |
| Metadata source inventory | partial | `sources/catalogue.yaml`, `sources/manifests/*.yaml`, `registers/sources.yaml` | Fifty-eight stable source records exist, but authority and later state representations conflict. |
| Source schema | partial | `schemas/sources.yaml`, `project/decisions/0002-canonical-source-catalogue-schema.md` | Maksim Zakharenkau approved the Draft 2020-12 schema matching the canonical catalogue shape on 2026-07-30; an executable validator remains absent, and the schema does not constrain source types or domains to configuration. |
| Controlled extraction | partial | `project/status/source-access-report.md`, `knowledge/public-source-analysis.md`, `knowledge/current_state_search_20.md` | Repository notes report prior local extraction, but no tracked extractor, processing-run record, or extracted corpus demonstrates a reproducible current workflow. |
| Atomic evidence management | planned | `knowledge/evidence/`, `knowledge/README.md` | Directory intent exists; no evidence schema, records, or validator was found. Existing knowledge notes are synthesis documents, not atomic evidence records. |
| Structured knowledge management | partial | `knowledge/*.md`, `knowledge/README.md`, `registers/*.yaml` | Two source-linked synthesis notes exist. Ten domain/project registers are empty and lack object-specific schemas. |
| Knowledge graph construction/operation | absent | No graph schema, relationship store, builder, query, or test found | Register names alone do not implement a graph. |
| Relationship and impact analysis | absent | No dependency traversal or impact implementation found | `registers/dependencies.yaml` is empty and has no schema. |
| Current-state assessment | planned | `assessments/README.md`, `assessments/` subdirectories, `outlook/03-current-state/README.md` | Scaffolding and one current-state knowledge note exist, but no assessment contract or assessed baseline exists. |
| Target state, gaps, and maturity | planned | `assessments/target-state/`, `assessments/gaps/`, `outlook/14-maturity/`, `config/scoring_models.yaml` | Directories exist; scoring configuration is empty and no assessment records were found. |
| Outlook content | planned | `outlook/README.md`, domain README files | Section structure exists; no demonstrated modular report content or assembly exists. |
| Project and progress management | partial | `project/status/*.md`, policies, empty registers | Status and policies exist. Risks, initiatives, milestones, metrics, dependencies, controls, and decision registers contain no records. |
| Architecture decisions | partial | `project/decisions/`, `registers/decisions.yaml` | Nine ADRs now exist: ADR 0002 records human approval, ADR 0001 is a proposed target operating model, and ADRs 0003–0009 are proposed records of operative evidence-backed rules. The structured decision register remains empty and has no schema. |
| Audience configuration | absent | `config/audiences.yaml` | File is empty. |
| Audience-specific reporting | planned | `publications/README.md`, audience directories | Directory intent exists; no templates, report content, generator, or validation found. |
| Audience-specific presentations | planned | `presentations/README.md`, `presentations/source/`, `presentations/themes/`, `presentations/generated/.gitkeep` | Directory intent exists; no deck source, theme, generator, or tests found. |
| Website publication | planned | `website/README.md` | Intent only; no site configuration or implementation found. |
| Incremental source processing | absent | No detector, dependency graph, invalidation state, runner, or tests found | Hash metadata exists, but no automation uses it for incremental processing. |
| Repository validation | absent | `scripts/README.md`, `tests/README.md`, empty subdirectories | No executable validator or automated tests found. YAML can be parsed manually. |
| CI and documentation build | absent | `.github/README.md`; no workflow or MkDocs/configuration files | No automated CI, documentation build, or link checker is configured. |

## Source-state conflict

The repository states that `sources/catalogue.yaml` is authoritative. Direct
inspection found:

- `sources/catalogue.yaml`: 58 records; 57 `unclassified` and one `internal`;
  56 `metadata_catalogued`, one `blocked`, and one
  `approved_for_processing`.
- `registers/sources.yaml`: 58 legacy records; 32 `public`, 21 `internal`, and
  five `restricted`; 32 `extracted`, 25 `approved_for_processing`, and one
  `blocked`.
- `sources/manifests/*.yaml` and
  `project/status/source-access-report.md`: later classifications and extraction
  claims.

These records cannot all be current under the declared authority rule. No values
were reconciled in this stage. The conflict blocks reliable downstream
incremental processing and should be resolved through an approved catalogue
migration or correction.

## Source-of-truth findings

- Original evidence is designated outside Git by
  `project/source-management-policy.md` and `config/source-types.yaml`.
- `sources/catalogue.yaml` is declared the canonical inventory by `README.md`,
  `sources/README.md`, and `registers/README.md`.
- Markdown and YAML registers are declared canonical repository content, but a
  register is not usable until its specific schema and records exist.
- Generated outputs are intended as derivatives; no generation pipeline exists.

## Validation baseline

PyYAML is available in the local virtual environment and the inspected YAML
files parse. Parsing is not schema validation. There is no configured schema
validator, test runner, repository validator, documentation builder, link
checker, or CI workflow.

## Unresolved issues

1. Reconcile the canonical catalogue with the legacy source register, manifests,
   and status claims under human review.
2. Define and review the missing catalogue-to-configuration contracts for the
   `glossary` domain and `image` source type without changing controlled values
   implicitly.
3. Configure executable validation for the approved canonical source schema.
4. Record approval or requested changes for the proposed operating-model ADR
   and policy documents.
5. Define atomic evidence and relationship schemas before adding evidence or
   graph records.
6. Add minimal repository and documentation validation before implementing
   downstream processing.

## Stage 9 validation follow-up — 2026-08-02

Stage 9 supersedes the historical `absent` findings for repository validation
and CI. `scripts/validate_schemas.py` now performs Draft 2020-12 meta-schema,
format, source-catalogue, and production knowledge-record validation;
`scripts/validate_knowledge.py` performs knowledge-layer integrity checks; 29
unit tests cover both validators; and `.github/workflows/validate.yml` runs the
implemented checks. The source schema and 58 current catalogue records pass the
configured standards-based validator.

Repository validation and CI are therefore partial rather than absent. A
documentation build and CI link check remain absent, and the source-state,
taxonomy, source-type mapping, manifest-consistency, and processing-run gaps in
this baseline remain unresolved. This follow-up does not change any approval
state or reconcile source metadata.
