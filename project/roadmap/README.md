# Master roadmap

The master roadmap is the controlled planning boundary between the implemented
Stage 9 foundation and later repository work. The machine-readable authority is
[`../roadmap.yaml`](../roadmap.yaml); the explanatory form is
[`implementation-roadmap.md`](implementation-roadmap.md). They are cross-checked
by `scripts/validate_roadmap.py`.

## Purpose and boundaries

The roadmap defines stable stage IDs, prerequisites, entry criteria, deliverables,
validation, exit gates, success measures, dependencies, and downstream prompt
generation boundaries. It contains no dates, budgets, headcount, or effort
estimates. It is not evidence, authoritative knowledge, an approval record, or
an implementation claim.

Stage 09.5 is approved. Stage 10 is the next planned stage because
the repository has validated processing controls and a small draft evidence and
knowledge set, but it is not implemented by this roadmap task. No Stage 10 or
later implementation is included here.

## Inputs, outputs, and ownership

Inputs are the current repository state, approved architecture and policies,
controlled configuration, applicable schemas and validators, and stage status
records. Outputs are the two roadmap forms, lifecycle and stage templates, a
read-only validator, tests, and a status record. The roadmap maintainer owns the
approved roadmap; a stage prompt may be generated from it one stage at a time,
but each generated prompt and later stage execution retains its own review gates.

## Identifier and lifecycle rules

Stage IDs are stable lowercase values such as `stage-09`, `stage-09.5`, and
`stage-10`. An ID is never reused for another stage. A roadmap status follows
the controlled lifecycle in [`stage-lifecycle.md`](stage-lifecycle.md). A stage
capability status uses the repository-wide values in
[`../../docs/reference/statuses.md`](../../docs/reference/statuses.md), and does
not imply that a planned or scaffolded capability operates.

## Validation and limitations

The validator checks YAML syntax, required fields, controlled statuses, duplicate
IDs, missing stage references, dependency cycles, and consistency between the
machine-readable stages and human-readable stage headings. It does not approve
the roadmap, validate the substantive quality of requirements, inspect source
bodies, or execute any stage. Tests use synthetic temporary repositories.

Material architectural choices remain governed by existing ADRs. This roadmap
adds no new architectural decision; any later stage that changes an authority
boundary, identifier model, storage route, or canonical format must propose an
ADR and preserve human review.

## Downstream prompt generation

After human approval, [`generate-stage-prompt-from-roadmap.md`](../../prompts/codex/planning/generate-stage-prompt-from-roadmap.md)
may generate one matching stage prompt at a time. Generation copies the selected
stage's requirements and does not execute the stage or pre-generate Stages 10–16.
