# Architectural-decision review status

- Review date: 2026-07-30
- Review state: completed by AI agent; new ADR records require authorized human
  review
- Scope: existing architectural decisions demonstrated by repository
  implementation or policy
- Source-body access: none

## Method

The review inspected repository structure, current status, Git branch and
worktree state, root guidance, architecture documentation, policies, controlled
configuration, source metadata and schema structure, directory contracts, ADR
conventions, test and automation scaffolds, and relevant diffs. It did not open
or analyze external source-document contents.

An ADR was created only when a rule was already demonstrated by tracked
implementation, committed policy, or the authoritative operating contract.
Because the records are AI-authored, their status remains `proposed` until an
authorized human reviewer records approval. Each ADR distinguishes the
operative evidence-backed rule from capabilities that remain partial, planned,
or absent.

## ADRs created

| ADR | Existing decision evidence | Implementation boundary |
| --- | --- | --- |
| [ADR-0003](../decisions/ADR-0003-source-assets-outside-git.md) | `project/source-management-policy.md`, `config/source-types.yaml`, `sources/catalogue.yaml`, `schemas/sources.yaml` | External storage and metadata catalogue exist; controlled extraction and enforcement automation are incomplete |
| [ADR-0004](../decisions/ADR-0004-markdown-and-yaml-canonical-formats.md) | `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, tracked Markdown/YAML structure | Formats are in use; most structured object schemas and validators are absent |
| [ADR-0005](../decisions/ADR-0005-stable-identifiers.md) | `config/project.yaml`, `config/source-types.yaml`, `sources/catalogue.yaml`, `schemas/sources.yaml` | Project, source-root, and source IDs exist; downstream ID models do not |
| [ADR-0006](../decisions/ADR-0006-separate-evidence-and-knowledge.md) | `AGENTS.md`, `project/information-handling.md`, `project/source-management-policy.md`, `knowledge/README.md` | Boundary is operative; atomic evidence and promotion contracts are planned |
| [ADR-0007](../decisions/ADR-0007-human-review-for-authority.md) | `AGENTS.md`, `project/information-handling.md`, `project/source-management-policy.md` | Human authority gates are operative; workflow enforcement is mostly absent |
| [ADR-0008](../decisions/ADR-0008-publications-are-derivatives.md) | `README.md`, `CONTRIBUTING.md`, `publications/README.md`, `presentations/README.md` | Source-of-truth boundary exists; generator and release workflow do not |
| [ADR-0009](../decisions/ADR-0009-documentation-is-part-of-implementation.md) | `AGENTS.md`, `CONTRIBUTING.md`, `docs/governance/documentation-policy.md` | Documentation obligation is operative; automated completeness checking is absent |

## Decisions not documented

No separate ADR was created for:

- the complete eight-layer architecture, because it is already recorded as the
  proposed ADR 0001 and most downstream layers are planned or absent;
- an atomic-evidence schema or evidence identifier, because neither is
  approved or implemented;
- a knowledge graph, relationship schema, or automated impact model, because no
  implementation evidence exists;
- incremental source processing, because hashes exist but no detector,
  dependency traversal, invalidation engine, runner, or tests exist;
- a specific publication-generation technology or workflow, because audience
  configuration, templates, identifiers, generators, and validators are absent;
- stable identifiers for knowledge, assessments, most project records,
  publications, presentations, processing runs, or relationships, because the
  repository explicitly marks those models unapproved;
- a repository-wide automated approval workflow, because human-review policy
  exists but general workflow enforcement does not.

## Files changed by this review

Seven ADR files and this status record were created. ADR index links,
architecture links, the repository baseline, documentation index, and changelog
were updated. The ADR template was inspected and not modified. No capability,
schema, source record, original evidence, or automation was changed.

## Validation

- All 33 repository YAML files parsed with PyYAML 6.0.3.
- The YAML front matter in ADRs 0003–0009 parsed and each record uses the
  expected `ADR-NNNN` ID and `proposed` status.
- A local relative-link scan checked 124 links in 75 Markdown files and found no
  broken relative links.
- Lychee checked the same 124 links in offline mode: 124 passed and zero errors
  were reported.
- `git diff --check` passed.
- Final Git status and diff summary were inspected. The worktree contains broad
  pre-existing operating-model changes; this review did not overwrite or
  reconcile unrelated edits.
- No configured schema-validation command, repository validator, automated test
  suite, documentation builder, Markdown linter, YAML linter, Mermaid
  validator, or CI workflow was found. The `jsonschema` package is not
  installed in the repository virtual environment. No source or schema content
  changed in this task, and YAML parsing was not reported as schema validation.

## Remaining review items

1. An authorized human reviewer must accept, revise, reject, or retain the
   proposed status of ADRs 0003–0009.
2. ADR 0001 remains a proposed target architecture and must not be represented
   as implemented.
3. Existing catalogue/manifests/legacy-register state conflicts remain outside
   this documentation-only task and were not reconciled.

## Stage 9 follow-up — 2026-08-02

Stage 9 implements proposed knowledge identifiers, evidence/knowledge schemas,
reviewer gates, templates, and an integrity validator. These changes fit the
existing decisions in ADRs 0005, 0006, and 0007, so no duplicate ADR was
created. Those three proposed records and the ADR index were updated to
distinguish the implemented empty framework from still-absent production
knowledge, processing-run registration, source-catalogue integrity validation,
and repository-wide approval automation. Maksim Zakharenkau accepted ADRs 0005,
0006, and 0007 on 2026-08-02 as part of Stage 9 closure. ADRs 0001, 0003–0004,
and 0008–0009 remain proposed pending separate review.

## Source-processing follow-up — 2026-08-02

ADR 0010 records explicit source-processing authorization and run records.
The contracts, empty registers, validator, synthetic tests, and controlled
text/HTML reader were implemented as proposals. Maksim Zakharenkau accepted the
decision, policy, contracts, exact reconciliation, and 57 authorizations on
2026-08-02. No run or evidence exists and no source body was opened.

The later controlled pilot `RUN-000001` successfully created a private
derivative and awaits human verification. This operational follow-up does not
change ADR 0010 or make the run evidence-eligible.

## Final ADR acceptance follow-up — 2026-08-02

After source reconciliation and acceptance of ADR 0010, Maksim Zakharenkau
accepted ADR 0001 and ADRs 0003, 0004, 0008, and 0009 with the implementation
limitations recorded in
`project/status/adr-approval-review-0001-0003-0004-0008-0009.md`. This resolves
the earlier pending-review items without claiming that target or scaffolded
capabilities are operational.
