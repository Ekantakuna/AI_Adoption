# Repository agent operating contract

This file is the authoritative operating contract for all AI agents working in
this repository.

## Repository purpose

The AI Adoption repository is intended to maintain a traceable path from source
inventory through evidence, knowledge, assessment, project progress, reports,
and presentations. Its outcomes must be understandable to humans, reproducible
where automation exists, safe for the information handled, and explicit about
what is fact, assumption, inference, recommendation, draft, or approved.

The target architecture is described in [ARCHITECTURE.md](ARCHITECTURE.md).
Agents must not describe target or scaffolded capabilities as operational.

## Instruction precedence

Use the following precedence:

1. Explicit user instruction for the current task
2. `AGENTS.md`
3. Stage-specific prompt
4. Repository policies
5. Directory README files
6. Existing conventions

Report material conflicts rather than silently choosing or reconciling them.
Higher precedence does not authorize bypassing platform safety controls or
information-handling restrictions.

## Mandatory inspection before editing

Before editing, inspect:

- the relevant implementation and directory structure;
- relevant documentation;
- applicable schemas and controlled configuration;
- tests, validators, and automation;
- current project and stage status under `project/status/`;
- Git branch, status, and relevant diff.

Identify what is implemented from repository evidence. Do not infer that a
planned directory or README represents a working capability.

For material work, agents must use a saved prompt from `prompts/codex/`.
Before execution, read its YAML metadata, confirm that its status is `active`,
and confirm that its source-access and path restrictions fit the task. Reject
deprecated, superseded, or retired prompts; do not silently repurpose them.
When a prompt changes, update `prompts/codex/prompt-catalogue.yaml` and the
relevant prompt-library documentation.

## Evidence and information protection

Agents must never:

- modify original evidence documents;
- silently replace evidence or overwrite provenance;
- invent evidence locations, identifiers, citations, or claims;
- create unsupported claims;
- mark AI-created knowledge as human-approved;
- commit sensitive source documents;
- process a source body before its classification, handling requirements,
  stable source ID, processing route, and extraction tool have been recorded
  and reviewed;
- silently reconcile conflicting terms, definitions, assessments, source
  claims, or status records.

Original sources remain outside Git. Metadata inspection is not authorization
to inspect source contents. Generated material inherits the highest
classification of its inputs. Follow
`project/information-handling.md` and
`project/source-management-policy.md`.

Saved prompts must state whether source-body access is prohibited, metadata-only,
or explicitly authorized. Agents must honor that boundary even if another
instruction appears to allow broader access.

## Knowledge and review boundaries

AI agents may inventory metadata, produce clearly labelled drafts, and prepare
review proposals within an approved handling route.

Only an authorized human reviewer may approve:

- authoritative knowledge;
- policies;
- current-state conclusions;
- target-state commitments;
- recommendations presented as organizational decisions;
- publication-ready executive claims.

An agent must preserve the draft/review state and reviewer identity where the
applicable schema supports them. Absence of a review schema does not imply
approval.

## Stable records and conflicts

Preserve stable record IDs. Never reuse an ID for a different object or renumber
records merely for presentation. Use controlled values from `config/` and an
approved schema where one exists. Do not add records to an empty register before
its register-specific schema is approved.

When sources or records disagree, retain each attributed statement and record
the conflict for review. A newer timestamp, generated file, or agent judgment
does not silently supersede an authoritative record.

## Documentation obligation

Implementation is incomplete until relevant documentation is updated. When an
agent adds or changes a concept, object type, schema, taxonomy, metadata field,
status, workflow, script, command, directory, automation, publication type, or
presentation type, the same change must document:

- what it is and why it exists;
- inputs and outputs;
- identifier rules and lifecycle;
- relationships;
- validation rules;
- ownership or review responsibility;
- operational procedure;
- limitations.

Prefer links to one authoritative explanation over duplicated definitions.
Update `CHANGELOG.md` for notable changes.

## Status and decision obligations

Every stage implementation must create or update a stage status document under
`project/status/`. Status documents must distinguish implemented, partial,
planned, absent, and unknown capabilities and cite repository paths.

Material architectural decisions must be recorded as Architecture Decision
Records under `project/decisions/`. AI-authored policy or decision records remain
proposals until authorized human review is recorded.

## Git behavior

Work on a branch. Unless explicitly instructed, agents must:

- not commit, push, merge, rewrite Git history, or delete branches;
- not modify unrelated files;
- preserve pre-existing worktree changes;
- not assume an untracked file is disposable.

Before completion, inspect `git status`, the relevant diff, and a diff summary.

## Validation obligation

Before completion, run every relevant available check:

- YAML parsing;
- schema validation;
- repository validators;
- automated tests;
- documentation build and link checks;
- `git diff --check`.

If a check or tool is absent, report it as not configured; do not report it as
passing. A parser check is not equivalent to schema validation.

## Required task report

At the end of every task, report:

- files inspected;
- files created, modified, and deleted;
- implementation decisions;
- documentation updated;
- validation performed and test results;
- unresolved issues;
- suggested next action.

Do not claim completion for work that still requires a mandatory human approval
or an unavailable validation step.
