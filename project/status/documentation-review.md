# Documentation review status

- Review date: 2026-07-30
- Review state: completed by AI agent; policy amendments and proposed
  architecture/ADR records still require authorized human review; the source
  catalogue schema was separately approved in ADR 0002
- Scope: repository documentation accuracy and completeness
- Source-body access: none

## Inspected evidence

The review inspected root documentation, all files under `docs/`, applicable
project policies/decisions/status records, configuration, the proposed source
schema, register shapes, source metadata structure and manifest inventory,
directory READMEs, scripts/tests/GitHub scaffolds, workflow and build
configuration absence, directory structure, Git branch/status, and the relevant
diff. External source-document contents were not opened.

## Findings and corrections

| Finding | Correction | Resulting status |
| --- | --- | --- |
| Historical source reports appeared to state current authority and contradicted the catalogue | Added historical-snapshot notices and clarified that reconciliation requires authorized human review | Conflict remains unresolved and explicit |
| Source policy said document analysis had not started despite reports of prior local extraction and synthesis | Replaced the absolute claim with a history/current-gate section | Documentation now distinguishes reported history from current reproducibility and access authority |
| Source metadata, extraction, atomic evidence, knowledge, assessment, canonical data, derivatives, and local-only data lacked one shared definition | Added `docs/concepts/information-objects.md` and linked it from entry points | Terminology and lifecycle boundaries documented; downstream object schemas remain planned |
| Several README files described empty scaffolds as if utilities, tests, reports, presentations, or sites existed | Marked the directories partial, planned, or absent and listed missing contracts/automation | Planned capability is no longer presented as operational |
| Important empty subdirectories and root control files were omitted from the repository map | Expanded the subdirectory and root-file descriptions | Current structure is documented without claiming implementation |
| Local commands lacked output/limitation explanations | Added explanations for inventory and finish commands | Operational procedure distinguishes tracked diffs, untracked files, and ignored paths |
| Information-handling text did not fully state local/Git storage, evidence protection, or approval boundaries | Expanded the policy with those distinctions and marked AI amendments for human review | Controls are documented; enforcement automation remains absent |
| A saved-prompt README required a processing-run report even though no such object contract exists | Marked processing-run records as planned and documented the interim convention | Procedure now matches implementation |

## Required distinctions

The reviewed documentation now explicitly distinguishes:

- implemented, partial, planned, absent, and unknown capability status;
- target architecture, operational procedure, design principles, and future
  automation;
- source metadata from source content and extraction;
- extraction and evidence from interpreted knowledge;
- drafts/proposals from human-approved records;
- canonical structured/Markdown records from generated derivatives;
- local-only source assets and restricted derivatives from content eligible for
  Git.

## Documentation-impact rule

`AGENTS.md` requires documentation updates whenever a concept, object type,
schema, taxonomy, metadata field, status, workflow, script, command, directory,
automation, publication type, or presentation type changes. It also requires
the purpose, inputs/outputs, identifiers/lifecycle, relationships, validation,
review ownership, operation, and limitations to be documented.

## Validation

- All 33 repository YAML files parsed with PyYAML 6.0.3.
- A local relative-link scan checked 62 Markdown files and found no broken
  relative links.
- `git diff --check` passed.
- No executable scripts, automated tests, CI workflows, package/test
  configuration, documentation builder, Markdown linter, link checker, YAML
  linter, or configured Draft 2020-12 validator was found.
- Schema validation, repository integrity validation, automated tests,
  documentation build, Mermaid validation, and CI therefore remain unavailable;
  YAML parsing is not schema validation.

## Remaining review items

1. An authorized human must review the policy amendments and proposed ADRs;
   ADR 0002 already records approval of the source schema.
2. The catalogue, legacy source register, manifests, and historical source
   reports still require controlled reconciliation.
3. Downstream object identifiers, lifecycles, schemas, and validators remain
   unimplemented; this review documented but did not create those capabilities.
4. A configured documentation/link/Mermaid validation toolchain is still
   absent.

## Documentation-impact follow-up — 2026-08-02

This follow-up reviewed the current implementation diff without opening
external source-document contents. The implementation surface was
`AGENTS.md`, `config/source-types.yaml`, `schemas/sources.yaml`, the new
`prompts/codex/` prompt library, and the changed directory structure represented
by those prompt files. No scripts, tests, GitHub workflows, knowledge object
types, publication templates, or presentation templates changed.

The review corrected the source-schema approval description, documented the
schema's top-level and record fields and non-JSON-Schema integrity limitations,
made the prompt inventory and prompt lifecycle match the files present, and
recorded that the two overlapping source ignore-list keys have no defined
consumer or precedence. The source catalogue schema conversion and prompt
library are now represented in the changelog. The ignore-list ambiguity remains
an implementation issue rather than being assigned invented behavior in
documentation.

Validation for this follow-up parsed all 33 YAML files with PyYAML 6.0.3,
checked the seven `ADR-NNNN` front-matter records, and checked 124 relative
links across 75 Markdown files with both a local path scan and Lychee offline;
all checks passed. `git diff --check` also passed. The repository still has no
configured schema-validation command, test suite, documentation builder,
Markdown linter, Mermaid validator, or CI workflow; the available Python
environment does not provide `jsonschema`.

## Final-stage validation follow-up — 2026-08-02

Final validation inspected the complete uncommitted operating-model change set
without opening external source bodies. It corrected the prompt inventories in
`prompts/codex/README.md` and `docs/repository-map.md`, which had omitted the
tracked final-stage validation prompt. It also documented two pre-existing
catalogue-to-configuration gaps in `config/README.md`, `schemas/README.md`, and
`project/status/repository-baseline.md`: `glossary` is absent from the taxonomy,
and no contract maps catalogue source type `image` to source group `images`.
No controlled value, source record, evidence claim, schema approval, or ADR
decision was changed.

Validation parsed all 33 YAML files, including the two intentional empty
configuration placeholders, with PyYAML 6.0.3 and duplicate-key detection. A
direct integrity audit checked the approved source-schema field rules, all 58
unique catalogue IDs, configured source-ID prefixes, record counts, controlled
classification and processing values, duplicate references, all 15 manifest
catalogue pointers, the 58-record legacy source-ID set, 37 Markdown source-ID
mentions, empty unschematized registers, and all nine ADR IDs; no dangling or
duplicate references were found. A local path scan and Lychee 0.24.2 checked
124 relative links across 76 Markdown files; all passed. `git diff --check`
passed, and final Git status and diff statistics were inspected.

The audit retained three explicit gaps rather than silently reconciling them:
the two undefined catalogue-to-configuration mappings above and 40 copied-field
differences between the authoritative catalogue and historical manifests. The
manifest conflict was already documented. Standards-based Draft 2020-12 schema
validation remains unavailable because no compatible validator is configured
or installed. No repository validator, automated test suite, documentation
builder, Markdown linter, Mermaid validator, or CI workflow exists. The stage is
ready for authorized human review, but commit readiness depends on that review
and acceptance of the unavailable validation and retained data conflicts.

## Stage 9 schema-validation follow-up — 2026-08-02

Stage 9 supersedes the earlier current-state claims that no schema validator,
repository validator, automated tests, or CI workflow exist. The repository
adds pinned direct validation dependencies, `scripts/validate_schemas.py`,
`scripts/validate_knowledge.py`, 29 unit tests, and
`.github/workflows/validate.yml`. Standards-based Draft 2020-12 meta-schema,
format, source-catalogue, and production knowledge-record validation passes for
13 schemas, 58 catalogue records, and zero production knowledge records. The
knowledge validator also passes with zero errors.

The earlier sections remain historical evidence of their dated reviews. A
documentation build and CI link check remain unconfigured. The follow-up does
not approve Stage 9 policy/schema proposals, authenticate the recorded ADR 0002
reviewer claim, or resolve retained source-state conflicts.

## Stage 9 approval follow-up — 2026-08-02

Maksim Zakharenkau subsequently confirmed full review authority, authenticated
his ADR 0002 approval, and approved the Stage 9 policy, contracts, and ADRs
0005–0007. The approval scope and exclusions are recorded in
[stage-09-approval.md](stage-09-approval.md). The source-state conflict and
processing-run contract remained deferred and continued to block new source
processing at Stage 9 closure.
