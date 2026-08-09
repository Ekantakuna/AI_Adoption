# Codex task prompts

This directory contains version-controlled instructions used to operate Codex CLI
within the AI Adoption repository. The catalogue and metadata are validated by
`scripts/validate_prompts.py`; prompt text is not proof that a task ran.

## Purpose

Prompts are stored in Git so that agent-assisted work is:

- reproducible
- reviewable
- auditable
- consistent across stages
- understandable to future contributors

## Structure

- `bootstrap/` contains three prompts that establish repository-wide rules and
  documentation, review that documentation, and record evidenced decisions.
- `stages/` contains `STAGE-TASK-TEMPLATE.md`, the Stage 09 knowledge-framework
  implementation prompt, and the generated Stage 10 evidence-to-knowledge pilot
  prompt. The Stage 10 prompt is not execution evidence and retains human-review
  gates.
- `reviews/` and `validation/` contain reusable review and final-validation
  prompts. `maintenance/` contains health and source-change procedures; the
  latter is future-facing and does not claim operational incremental processing.
- `planning/` contains the Stage 9.5 roadmap prompt, its review prompt, and the
  generator that may create one later stage prompt from an approved roadmap.
- `templates/` contains metadata-bearing generic, stage, review, and
  maintenance templates and is never included as active execution prompts.

## Inputs, outputs, and lifecycle

A saved prompt consumes the repository state and the explicit scope supplied by
the operator. Its expected outputs are the files and report named in that
prompt, subject to `AGENTS.md`, applicable policies, and human-review gates.
Creating or editing a prompt does not execute it. A prompt becomes usable after
repository review, remains versioned for traceability, and should be revised or
superseded when its referenced paths, commands, statuses, or controls change.
Stable prompt IDs, versions, lifecycle statuses, and source-access values are
recorded in `prompt-catalogue.yaml`. Templates and deprecated prompts are not
active execution prompts. Run `python scripts/validate_prompts.py` to check the
catalogue and metadata.

## Operating rule

Saved prompts are the intended convention for significant, repeatable Codex
tasks. A processing-run report is a planned object: no processing-run schema,
identifier, lifecycle, storage location, or validator is currently implemented.
Until those controls exist, preserve a task prompt in this directory when the
task explicitly calls for it, or report that no durable run record exists.

Codex must inspect `AGENTS.md` before making repository changes.
