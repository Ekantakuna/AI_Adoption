# Codex task prompts

This directory contains version-controlled instructions used to operate Codex CLI
within the AI Adoption repository.

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
- `stages/` contains `STAGE-TASK-TEMPLATE.md` and the Stage 09 knowledge-framework
  implementation prompt.
- `maintenance/` contains the recurring documentation-impact review and final
  stage-validation prompts; change-processing and status-generation prompts
  are planned.

## Inputs, outputs, and lifecycle

A saved prompt consumes the repository state and the explicit scope supplied by
the operator. Its expected outputs are the files and report named in that
prompt, subject to `AGENTS.md`, applicable policies, and human-review gates.
Creating or editing a prompt does not execute it. A prompt becomes usable after
repository review, remains versioned for traceability, and should be revised or
superseded when its referenced paths, commands, statuses, or controls change.
There is no prompt schema, prompt identifier, execution registry, or automated
prompt validator.

## Operating rule

Saved prompts are the intended convention for significant, repeatable Codex
tasks. A processing-run report is a planned object: no processing-run schema,
identifier, lifecycle, storage location, or validator is currently implemented.
Until those controls exist, preserve a task prompt in this directory when the
task explicitly calls for it, or report that no durable run record exists.

Codex must inspect `AGENTS.md` before making repository changes.
