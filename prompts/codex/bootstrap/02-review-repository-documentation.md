# Task: Review repository documentation for accuracy and completeness

Review the documentation created for the AI Adoption repository.

## Mandatory inspection

Read:

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `ARCHITECTURE.md`
- `CHANGELOG.md`
- all files under `docs/`
- relevant files under `project/`
- repository schemas and configuration
- relevant scripts, tests, and workflows
- the current directory structure
- Git diff

## Review objectives

Identify and correct:

- statements that claim planned capabilities are already implemented
- contradictory terminology
- duplicated authoritative explanations
- broken relative links
- missing directory descriptions
- missing explanation of local-only source data
- missing evidence-protection rules
- missing human review boundaries
- missing status or lifecycle explanations
- commands without explanations
- concepts without definitions
- object types without lifecycle or identifier descriptions
- documentation that does not match implementation
- files mentioned in documentation that do not exist
- important implemented files that are not documented

## Required distinctions

The documentation must distinguish:

- current implementation
- planned architecture
- operational procedure
- design principle
- future automation

It must distinguish:

- source metadata from source content
- evidence from interpreted knowledge
- drafts from approved knowledge
- canonical structured data from generated publications
- local source files from Git-tracked repository content

## Documentation impact rule

Confirm that `AGENTS.md` requires documentation updates whenever implementation,
schemas, workflows, concepts, statuses, or commands change.

## Final actions

- Correct documentation problems directly.
- Do not implement new project capabilities during this task.
- Do not inspect external source-document contents.
- Run relevant validation and `git diff --check`.
- Do not commit or push.

Report:

1. Problems found
2. Corrections made
3. Remaining uncertainties
4. Validation results
