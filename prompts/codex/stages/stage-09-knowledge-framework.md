# Stage 9 — Implement the Knowledge Extraction Framework

## Objective

Complete the controlled knowledge framework needed for future source-content
analysis, evidence extraction, knowledge management, knowledge relationships,
incremental updates, reporting, and presentation generation.

This task must extend the existing repository structure. It must not overwrite,
delete, or duplicate useful existing content.

## Existing repository context

The repository already contains:

- `knowledge/README.md`
- `knowledge/assumptions/`
- `knowledge/decisions/`
- `knowledge/evidence/`
- `knowledge/references/`
- `knowledge/current_state_search_20.md`
- `knowledge/public-source-analysis.md`
- `schemas/README.md`
- `schemas/sources.yaml`

Treat these as existing project assets.

Before editing, inspect them and determine:

- their current purpose;
- whether they match the target knowledge model;
- whether they should remain where they are;
- whether they require documentation or migration;
- whether they contain substantive knowledge that must be preserved.

Do not delete or move them without first reporting the reason.

## Mandatory inspection

Before making changes, read:

- `AGENTS.md`
- `README.md`
- `ARCHITECTURE.md` if present
- `CONTRIBUTING.md` if present
- `knowledge/README.md`
- every existing file directly under `knowledge/`
- README files under `knowledge/`
- `schemas/README.md`
- `schemas/sources.yaml`
- `config/project.yaml`
- `config/taxonomy.yaml`
- `config/source-types.yaml`
- `sources/catalogue.yaml`
- `project/source-management-policy.md`
- `project/status/source-access-report.md`
- relevant scripts, tests, prompts, and workflows
- current Git status and branch

## Restrictions

- Do not read external source-document contents.
- Do not perform new substantive knowledge extraction.
- Do not copy source documents into Git.
- Do not change source catalogue IDs.
- Do not delete existing knowledge files.
- Do not create duplicate authoritative structures.
- Do not mark AI-generated records as verified or approved.
- Do not commit or push.
- Do not change unrelated files.

## Required architecture

The knowledge layer must support this traceable flow:

Source catalogue
→ source processing run
→ atomic evidence statement
→ knowledge object
→ relationship
→ assessment or outlook
→ report
→ presentation

Distinguish clearly:

- source metadata;
- extracted evidence;
- interpreted knowledge;
- project decisions;
- assumptions;
- assessments;
- generated publications.

## Required directories

Create only missing directories and documentation:

- `knowledge/glossary/`
- `knowledge/concepts/`
- `knowledge/frameworks/`
- `knowledge/metrics/`
- `knowledge/risks/`
- `knowledge/trends/`
- `knowledge/use_cases/`
- `knowledge/relationships/`

Preserve existing directories:

- `knowledge/assumptions/`
- `knowledge/decisions/`
- `knowledge/evidence/`
- `knowledge/references/`

Every knowledge subdirectory must have a README explaining:

- purpose;
- accepted content;
- prohibited content;
- identifier prefix;
- template;
- evidence requirement;
- review requirement;
- upstream inputs;
- downstream consumers.

## Required configuration

Create:

- `config/knowledge-types.yaml`
- `config/evidence-confidence.yaml`
- `config/review-statuses.yaml`

Define at least these object types and prefixes:

- evidence statement: `EVID`
- glossary term: `TERM`
- concept: `CONCEPT`
- framework: `FRAME`
- metric: `METRIC`
- risk: `RISK`
- trend: `TREND`
- use case: `USECASE`
- relationship: `REL`
- assumption: `ASSUMPTION`
- decision: `DECISION`
- reference: `REF`

Review statuses must include:

- draft
- needs_review
- under_review
- verified
- approved
- rejected
- deprecated

AI-generated content may initially use only:

- draft
- needs_review

Verified and approved records require reviewer information.

## Required schemas

Create valid JSON Schema expressed as YAML:

- `schemas/evidence.schema.yaml`
- `schemas/glossary-entry.schema.yaml`
- `schemas/concept.schema.yaml`
- `schemas/framework.schema.yaml`
- `schemas/metric.schema.yaml`
- `schemas/risk.schema.yaml`
- `schemas/trend.schema.yaml`
- `schemas/use-case.schema.yaml`
- `schemas/relationship.schema.yaml`
- `schemas/assumption.schema.yaml`
- `schemas/decision.schema.yaml`

Preserve `schemas/sources.yaml`.

Do not replace it unless there is a documented incompatibility.

Identifier forms must use six digits, for example:

- `EVID-000001`
- `TERM-000001`
- `CONCEPT-000001`
- `REL-000001`

Evidence records must reference source IDs that exist in:

- `sources/catalogue.yaml`

The actual catalogue uses the top-level key:

- `records`

The implementation must support that structure.

Knowledge objects must reference evidence IDs.

Relationships must reference existing knowledge-object IDs.

## Required templates

Create templates for each object type under the corresponding directory.

Templates must:

- use placeholder IDs ending in `000000`;
- be clearly marked as templates;
- not count as production records;
- contain no substantive extracted claims.

Use Markdown with YAML front matter where appropriate.

Use YAML-only templates for atomic evidence and relationships if that matches the
repository conventions.

## Existing knowledge-file treatment

Inspect:

- `knowledge/current_state_search_20.md`
- `knowledge/public-source-analysis.md`

Document what they currently represent.

Do not silently treat them as validated structured knowledge.

If they do not conform to the new model:

- preserve them;
- classify them as legacy, provisional, or analysis notes;
- document a later migration path;
- do not migrate their substantive content during this stage.

## Required policies and documentation

Create or update:

- `project/knowledge-management-policy.md`
- `project/knowledge-extraction-guidelines.md`
- `project/knowledge-review-workflow.md`
- `docs/concepts/source-evidence-knowledge.md`
- `docs/concepts/knowledge-object-model.md`
- `docs/architecture/knowledge-flow.md`
- `docs/operations/creating-knowledge-records.md`
- `docs/operations/reviewing-knowledge-records.md`
- `docs/reference/knowledge-identifiers.md`
- `docs/reference/knowledge-statuses.md`
- `project/status/stage-09-knowledge-framework.md`

Update relevant existing documentation, including:

- `knowledge/README.md`
- `schemas/README.md`
- root `README.md`
- `ARCHITECTURE.md`, if present
- `docs/repository-map.md`, if present
- `CHANGELOG.md`, if present

Document clearly what is:

- already implemented;
- introduced by Stage 9;
- still planned;
- legacy or provisional.

## Required validator

Create:

- `scripts/validate_knowledge.py`

The following command must work from repository root:

    python scripts/validate_knowledge.py

The validator must:

1. Parse `sources/catalogue.yaml`.
2. Read source IDs from the top-level `records` array.
3. Load controlled types, statuses, and confidence values.
4. Discover structured knowledge records.
5. Parse YAML and Markdown YAML front matter.
6. Ignore README and template files.
7. Validate ID format.
8. Check global ID uniqueness.
9. Validate source references against catalogue IDs.
10. Validate evidence references against evidence IDs.
11. Validate relationship endpoints.
12. Validate review statuses.
13. Require reviewer information for verified and approved records.
14. Identify unsupported object types.
15. Preserve compatibility with empty production directories.
16. Return exit code 0 when no errors exist.
17. Return a non-zero exit code when validation errors exist.
18. Print a concise summary.

Expected initial behavior may be similar to:

    Knowledge validation passed.
    Production knowledge records: 0
    Evidence records: 0
    Legacy or provisional files: 2
    Errors: 0

If existing files are counted differently, explain the decision.

## Required tests

Create:

- `tests/test_knowledge_validation.py`

Use temporary directories and fixtures.

Test at least:

- empty framework passes;
- valid evidence record passes;
- unknown source ID fails;
- duplicate ID fails;
- invalid review status fails;
- glossary entry without evidence fails;
- invalid identifier fails;
- templates are ignored;
- approved record without reviewer fails;
- catalogue `records` structure is supported;
- legacy Markdown notes do not silently become approved structured records.

Use the existing test framework. If none exists, use `unittest`.

## CI integration

Inspect the existing workflows.

Add:

    python scripts/validate_knowledge.py

to the existing validation workflow.

If none exists, create:

- `.github/workflows/validate.yml`

Do not remove unrelated checks.

## Stage status requirements

`project/status/stage-09-knowledge-framework.md` must include:

- objective;
- implementation status;
- pre-existing assets found;
- assets created;
- legacy or provisional knowledge files;
- schemas created;
- validators created;
- tests;
- CI integration;
- validation results;
- explicit exclusions;
- unresolved issues;
- next stage.

State explicitly that Stage 9 does not mean substantive content extraction is
complete.

## Validation commands

Run:

- YAML parsing for created YAML files
- `python scripts/validate_knowledge.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- existing repository validators
- `git diff --check`
- `git status --short`

## Final report

Report:

1. Existing assets inspected
2. Files preserved
3. Files created
4. Files modified
5. Legacy or provisional content treatment
6. Design decisions
7. Documentation updated
8. Validator behavior
9. Tests and validation results
10. Remaining gaps
11. Recommended next action

Do not commit or push.
