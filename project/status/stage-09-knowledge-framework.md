# Stage 09 knowledge framework status

## Objective

Implement the controlled, empty knowledge framework required for future
source-processing provenance, atomic evidence, interpreted knowledge,
relationships, assessments/outlooks, reports, and presentations without
performing substantive extraction or changing source records.

## Implementation status

**Complete and closed on 2026-08-02.** The resulting
knowledge capability remains partial because it intentionally contains no
production evidence or knowledge and has no processing-run implementation.
Stage 9 implements the knowledge-layer contracts, templates, validators, tests,
approved review workflow, and CI integration. Maksim Zakharenkau approved the
Stage 9 scope in [stage-09-approval.md](stage-09-approval.md).

## Pre-existing assets found and preserved

- `knowledge/README.md` documented a partial target area and was extended.
- Empty `knowledge/assumptions/`, `knowledge/decisions/`,
  `knowledge/evidence/`, and `knowledge/references/` directories were retained
  and received local contracts/templates.
- `knowledge/current_state_search_20.md` and
  `knowledge/public-source-analysis.md` contain substantive synthesis and were
  preserved unchanged.
- `schemas/README.md` and the approved `schemas/sources.yaml` source contract
  were retained; the source schema and every catalogue ID are unchanged.
- The canonical `sources/catalogue.yaml` has a top-level `records` array with 58
  unique source IDs. Only repository metadata was inspected.
- Existing source policies and historical status notes were preserved; their
  documented source-state conflict was not reconciled.

## Assets created

- Controlled configuration: `config/knowledge-types.yaml`,
  `config/evidence-confidence.yaml`, and `config/review-statuses.yaml`.
- Missing object directories: glossary, concepts, frameworks, metrics, risks,
  trends, use cases, and relationships.
- A README and placeholder-only template in all twelve knowledge object
  directories, including the four pre-existing directories.
- Knowledge policy, extraction guidelines, review workflow, conceptual model,
  architecture flow, creation/review operations, and identifier/status
  references.
- ADRs 0005, 0006, and 0007 were synchronized with the implemented empty
  framework and accepted by Maksim Zakharenkau; no duplicate architectural
  decision was added.

## Legacy or provisional knowledge files

The two root-level Markdown notes have no structured YAML front matter, stable
knowledge ID, atomic statement boundary, processing-run record, or reviewer
metadata. The validator reports them as two `legacy or provisional files` and
does not treat their headings named “Facts,” “Inferences,” or “Recommendations”
as verified structured records. A later migration must preserve their original
text, atomize only reviewed claims into new `EVID` and knowledge IDs, add exact
locators and run provenance, preserve fact/inference boundaries and conflicts,
and obtain authorized human review. No substantive migration occurred here.

## Schemas created

Draft 2020-12 JSON Schemas expressed as YAML were created for evidence,
glossary entries, concepts, frameworks, metrics, risks, trends, use cases,
relationships, assumptions, knowledge decisions, and contextual references.
Stage 9 includes executable Draft 2020-12 meta-schema and instance validation
with declared format checking.

## Validator created

`scripts/validate_knowledge.py` reads catalogue IDs from `records`, loads all
three controlled knowledge files, parses YAML and Markdown front matter,
ignores READMEs/templates, accepts empty directories, checks configured types
and ID prefixes, enforces global ID uniqueness, resolves source/evidence and
relationship references, validates status/confidence, enforces required fields
and reviewer gates, returns a non-zero code on errors, and prints a
concise summary. It does not open source bodies or validate processing-run
existence.

`scripts/validate_schemas.py` checks all 13 repository schemas against the
Draft 2020-12 meta-schema, validates `sources/catalogue.yaml` against the
approved source schema, and validates production knowledge records against
their configured object schemas. It ignores templates, READMEs, the two
root-level provisional notes. Cross-record rules remain in
`validate_knowledge.py`.

## Tests and CI integration

`tests/test_knowledge_validation.py` contains 22 isolated temporary-directory
tests covering the empty framework, valid evidence, unknown sources, duplicate
IDs, invalid statuses, evidence-required glossary entries, malformed IDs,
reserved production IDs, template exclusion, reviewer gates, catalogue
`records`, evidence and relationship references, malformed non-string
references and controlled values, unsupported types, and the legacy/unstructured
Markdown boundary, plus success/failure exit codes.
`tests/test_schema_validation.py` adds six isolated tests for schema and record
success, meta-schema failure, invalid source and knowledge records, template
exclusion, and command exit codes. `.github/workflows/validate.yml` installs the
pinned direct validation dependencies and runs both validators and the complete
test suite; no prior workflow existed.

## Validation results

Final local results after the validator correction on 2026-08-02:

```text
Knowledge validation passed.
Production knowledge records: 0
Evidence records: 0
Legacy or provisional files: 2
Errors: 0
```

```text
Schema validation passed.
Draft 2020-12 schemas checked: 13
Source catalogue records: 58
Production knowledge records: 0
Errors: 0
```

The 29 Stage 9 unit tests pass. All 18 Stage 9 YAML files and all 51 repository
YAML files parse with PyYAML without duplicate keys. Draft 2020-12 meta-schema,
format, source-catalogue, and production knowledge-record validation pass. The
knowledge validator passes, and both a local relative-target scan and Lychee
offline validate 140 Markdown links without errors. The text whitespace scan
and `git diff --check` pass. A configured documentation build remains
unavailable and is not reported as passing.

## Explicit exclusions and unresolved issues

- No external source body was opened; no source was extracted or copied to Git.
- No source catalogue ID or original evidence was changed.
- Stage 9 does **not** mean substantive content extraction is complete.
- There is no processing-run schema/register, extractor, production evidence,
  production structured knowledge, graph traversal, impact invalidation,
  assessment schema, report generator, or presentation generator.
- The source-state conflict documented in the repository baseline remains open
  and blocks trustworthy new source processing until authorized reconciliation.
- Stage 9 policies, workflows, controlled values, and schemas were approved by
  Maksim Zakharenkau. Framework approval is not content approval.
- A documentation build remains unconfigured. Link checking is available
  locally through Lychee but is not part of the repository CI workflow.

## Closure review

Maksim Zakharenkau identified himself as the repository owner and developer,
confirmed full review authority, and approved the concrete post-validation
scope on 2026-08-02. The complete scope and exclusions are recorded in
[stage-09-approval.md](stage-09-approval.md).

The reviewer accepted the source-state conflict and missing processing-run
contract as explicit, deferred limitations rather than silently resolving them
inside Stage 9. New source-body processing remains blocked until authorized
reconciliation and a reviewed processing-run contract exist.

## Next stage

After final Stage 9 approval, define the controlled source-processing-run object
and reconcile the canonical catalogue state before any pilot extraction. After
those gates, create a small reviewed pilot that tests run → evidence → knowledge
→ relationship traceability without migrating the two provisional notes
wholesale.

## Post-stage follow-up — 2026-08-02

The separately reviewed source-processing policy, authorization/run contracts,
ADR 0010, exact catalogue reconciliation, and 57 authorizations were approved
and implemented after Stage 9 closure. This does not change the historical
Stage 9 approval snapshot above. No source body, processing run, production
evidence, or production knowledge was created in that follow-up.
