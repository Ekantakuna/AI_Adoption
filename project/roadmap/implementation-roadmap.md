# Master implementation roadmap

Status: `approved`
Roadmap ID: `ROADMAP-000001`
Source access: repository-only
Human review: approved by Maksim Zakharenkau on 2026-08-08

This document is the human-readable companion to
[`../roadmap.yaml`](../roadmap.yaml). The validator checks that every machine
stage has one matching heading. The roadmap is a plan, not proof that its future
stages operate.

## How to use this roadmap

Complete stages in dependency order. Before work begins, inspect the current
status and confirm the entry criteria. During work, preserve stable IDs and
review states, keep conflicts explicit, and do not access source bodies outside
an approved route. At closure, update the stage status, run the listed checks,
and obtain the required human review. A later stage may not silently repair or
reclassify an earlier stage.

## Stage-09 — Knowledge framework

- Status: `implemented`; capability: `partial`
- Prerequisites: `stage-08`
- Entry criteria: Stage 8 operating model and source handling existed.
- Deliverables: knowledge schemas/templates; source-processing authorization and
  run contracts; knowledge and processing validators; CI and tests.
- Validation: YAML, schema, knowledge, source-processing, tests, and diff checks.
- Exit gates: Stage 9 approval, review boundaries, and deferred limitations are
  recorded.
- Success measure: controlled records validate and provenance links resolve
  without copying original source bodies into Git.
- Dependencies: none.
- Limitation: the framework and small post-stage drafts do not establish
  authoritative knowledge.

## Stage-09.5 — Master implementation roadmap

- Status: `implemented`; capability: `implemented`
- Prerequisites: `stage-09`
- Entry criteria: current repository and Stage 9 status inspected; active prompt
  metadata verified; source-body boundary confirmed.
- Deliverables: machine/human roadmaps, lifecycle and stage templates, validator,
  tests, and status record.
- Validation: YAML parsing, roadmap validation, tests, and `git diff --check`.
- Exit gates: forms cross-check; validator passes; authorized human review is
  recorded.
- Success measure: stable IDs and gates exist, invalid references and cycles are
  rejected, and unsupported estimates are absent.
- Dependencies: `stage-09`.
- Limitation: this task creates planning controls only; it does not implement
  Stage 10.

## Stage-10 — Reviewed evidence-to-knowledge pilot

- Status: `planned`; capability: `partial`
- Prerequisites: `stage-09.5`
- Entry criteria: approved roadmap; validated authorizations/runs; stable
  provenance; assigned human reviewer.
- Deliverables: small reviewed evidence set, selected reviewed knowledge and
  relationships, pilot report, and stage status.
- Validation: YAML, schema, knowledge, source-processing, tests, and diff checks.
- Exit gates: eligible run provenance, recorded human review, retained conflicts
  and exclusions, and no wholesale provisional-note migration.
- Success measure: run-to-evidence-to-knowledge links validate and review states
  are accurate.
- Dependencies: `stage-09`, `stage-09.5`.
- Limitation: Stage 10 is next planned work only and is not implemented here.

## Stage-11 — Knowledge graph and impact integrity

- Status: `planned`; capability: `absent`
- Prerequisites: `stage-10`
- Entry criteria: pilot closed and relationship/traversal contract approved.
- Deliverables: relationship lifecycle, impact validator, synthetic tests, and
  stage status.
- Validation: YAML, schema, repository, tests, and diff checks.
- Exit gates: traversal behavior, canonical boundaries, and human review are
  documented.
- Success measure: explicit references identify affected downstream objects.
- Dependencies: `stage-10`.

## Stage-12 — Assessment and outlook contracts

- Status: `planned`; capability: `planned`
- Prerequisites: `stage-10`, `stage-11`
- Entry criteria: reviewed knowledge/relationships and approved scoring/audience
  controls.
- Deliverables: assessment schemas, outlook contract, validator/tests, status.
- Validation: YAML, schema, repository, tests, and diff checks.
- Exit gates: claim types and human approval gates are explicit.
- Success measure: assessments cite upstream objects and reproducibly describe
  scoring inputs and limitations.
- Dependencies: `stage-10`, `stage-11`.

## Stage-13 — Project progress and decision views

- Status: `planned`; capability: `partial`
- Prerequisites: `stage-12`
- Entry criteria: approved project-record schemas, ownership, and stable
  assessment inputs.
- Deliverables: project register contracts, progress validation, tests, status.
- Validation: YAML, schema, repository, tests, and diff checks.
- Exit gates: owners, lifecycle states, approval boundaries, and attribution.
- Success measure: progress views regenerate from canonical records.
- Dependencies: `stage-12`.

## Stage-14 — Audience publications

- Status: `planned`; capability: `planned`
- Prerequisites: `stage-12`, `stage-13`
- Entry criteria: approved audiences/publication contract and reviewed inputs.
- Deliverables: publication schema, provenance validator, assembly procedure,
  tests, status.
- Validation: YAML, schema, repository, links, tests, and diff checks.
- Exit gates: upstream resolution, classification, and release approval.
- Success measure: publications reproduce from declared inputs and generator
  metadata.
- Dependencies: `stage-12`, `stage-13`.

## Stage-15 — Presentations and website derivatives

- Status: `planned`; capability: `planned`
- Prerequisites: `stage-14`
- Entry criteria: approved publication and output contracts.
- Deliverables: presentation and website contracts, traceability checks, tests,
  status.
- Validation: YAML, schema, repository, links, tests, and diff checks.
- Exit gates: source references, replaceability, and release approval.
- Success measure: outputs identify inputs, generator version, review state, and
  limitations.
- Dependencies: `stage-14`.

## Stage-16 — Incremental change and operating automation

- Status: `planned`; capability: `absent`
- Prerequisites: `stage-11`, `stage-14`, `stage-15`
- Entry criteria: stable identifiers/dependencies and approved change/storage
  controls.
- Deliverables: change detector, impact/invalidation records, regeneration
  procedure, synthetic tests, status.
- Validation: YAML, schema, repository, tests, and diff checks.
- Exit gates: stale derivatives, immutable originals, and human re-review gates
  are controlled.
- Success measure: affected objects are reproducibly identified without
  needless reprocessing.
- Dependencies: `stage-11`, `stage-14`, `stage-15`.
