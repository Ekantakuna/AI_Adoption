# Contributing

Contributions must keep the repository traceable, reviewable, and safe for its
information classification. Read [AGENTS.md](AGENTS.md), even when contributing
without an AI agent.

## Before making changes

1. Work on a dedicated branch and inspect `git status`.
2. Read the relevant implementation, documentation, schemas, controlled
   configuration, tests, and project status.
3. Confirm that source material has a stable ID, classification, approved
   processing route, and approved tool before opening its body.
4. Identify whether a material design choice requires an Architecture Decision
   Record in `project/decisions/`.
5. Preserve unrelated and pre-existing worktree changes.

Do not add credentials, personal information, production datasets, original
source binaries, or unreviewed restricted material. The fact that a path is not
ignored by Git does not make its contents safe to track.

## Content and record rules

- Separate facts, assumptions, inferences, and recommendations.
- Cite stable source or evidence IDs for source-derived claims.
- Preserve existing record IDs; never reuse an ID for another object.
- Use controlled values from `config/`.
- Add structured records only under an approved object-specific schema.
- Treat reviewed Markdown and YAML registers as canonical. Mark generated
  derivatives and keep them reproducible when automation exists.
- Represent terminology, evidence, and status conflicts explicitly.
- Do not present AI-generated content as human-approved.

Identifier rules are documented in
[docs/reference/identifiers.md](docs/reference/identifiers.md), and lifecycle
values in [docs/reference/statuses.md](docs/reference/statuses.md).

## Keep documentation and status synchronized

Any implementation change must update its authoritative documentation in the
same branch. Cover its purpose, inputs, outputs, identifiers, lifecycle,
relationships, validation, review ownership, operation, and limitations.

Also:

- update a stage record under `project/status/`;
- update `CHANGELOG.md` for notable changes;
- add or update an ADR for material architectural decisions;
- update the repository map when a directory's contract changes.

## Source changes and incremental work

The automated incremental-processing model is planned, not implemented. Until
it exists, a source metadata or hash change requires a controlled review:

1. preserve the source ID and previous path or hash history;
2. update the authoritative catalogue only through an approved inventory step;
3. identify affected evidence, knowledge, assessments, and outputs from explicit
   references;
4. reprocess only under the approved handling route;
5. mark impacted content for review rather than silently republishing it.

See [change management](docs/governance/change-management.md).

## Validation and review

Run all checks that exist and apply:

1. parse all YAML safely;
2. run schema and repository validators;
3. run automated tests;
4. build documentation and check links if configured;
5. run `git diff --check`;
6. inspect `git status --short` and `git diff --stat`.

Stage 9 provides Draft 2020-12 schema validation, a cross-record knowledge
validator, automated unit tests, and CI integration. Install
`requirements-validation.txt` and run all commands documented in
`docs/operations/local-development.md`. A documentation build remains
unconfigured. Do not substitute YAML parsing for schema validation.

Do not commit or push unless explicitly authorized.
