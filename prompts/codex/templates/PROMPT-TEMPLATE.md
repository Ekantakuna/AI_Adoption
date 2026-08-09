---
id: PRM-TEMPLATE-GENERIC
title: Generic Codex prompt template
type: template
version: 1.0.0
status: draft
owner_role: repository-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: cross-stage
source_access: repository_only
allowed_paths: []
prohibited_actions: [commit, push, source_body_access]
required_inputs: []
expected_outputs: []
validation: []
human_review: required
supersedes: null
superseded_by: null
---

# Task: <title>

## Objective

<Outcome, without expanding scope.>

## Repository context and mandatory inspection

Read `AGENTS.md`, relevant implementation, documentation, configuration,
schemas, tests, validators, workflows, project status, branch, status, and
diff. Treat planned material as planned.

## Prerequisites and scope

<Entry conditions and exact allowed work.>

## Out of scope

<Explicit exclusions, including unrelated implementation.>

## Source-data boundary and allowed files

State `none`, `repository_only`, `metadata_only`, or an explicitly approved
source subset. List allowed paths and never open or modify original sources
unless explicitly authorized by the applicable policy and prompt metadata.

## Required implementation and documentation

Separate implementation from documentation. Name inputs, outputs, identifiers,
lifecycle, relationships, ownership, review responsibility, and limitations.

## Validation and human review

Run applicable parsers, schema validators, tests, documentation/link checks,
and `git diff --check`. Preserve draft/review state; do not self-approve.

## Final report and Git restrictions

Report files inspected, created, modified, deleted, decisions, documentation,
validation/test results, unresolved issues, and next action. Do not commit,
push, merge, rewrite history, or delete branches unless explicitly authorized.
