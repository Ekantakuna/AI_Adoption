# Scripts

`validate_prompts.py` validates Codex prompt front matter, controlled types and
statuses, stable IDs, catalogue membership, paths, and template/lifecycle
rules. It does not execute prompts or authorize source access.

This directory contains the Stage 9 schema and knowledge-integrity validators,
approved source-processing validation, and a controlled reader for authorized
text/HTML runs. Reporting and publication tools remain scaffolded.

Install the pinned validation dependencies and run standards-based schema
validation from the repository root:

```text
python -m pip install -r requirements-validation.txt
python scripts/validate_schemas.py
```

`validate_schemas.py` checks every `*.schema.yaml` contract against the JSON
Schema Draft 2020-12 meta-schema, enables declared format checks, validates the
canonical source catalogue against `schemas/sources.yaml`, and validates future
production knowledge records against their configured object schemas. It
ignores READMEs, templates, and root-level provisional notes. It reports errors
without modifying any record.

Run the implemented validator from the repository root:

```text
python scripts/validate_knowledge.py
```

It reads the source catalogue and controlled knowledge configuration, discovers
YAML records and Markdown front matter, ignores templates and READMEs, and
checks identifiers, global uniqueness, references, statuses, confidence, and
reviewer gates. Reserved placeholder IDs cannot pass as production records, and
unstructured Markdown is accepted as provisional only at the knowledge root.
Malformed non-string reference and controlled-value fields are reported as
validation errors rather than terminating the validator.
It does not open source bodies, perform extraction, or replace authorized human
review. It resolves evidence processing-run references and requires a
successful reviewed run.

`validate_knowledge.py` performs cross-record integrity checks that JSON Schema
does not cover. Run both validators; neither grants content approval or source
access.

Run the roadmap validator with:

```text
python scripts/validate_roadmap.py
```

It checks `project/roadmap.yaml` and its human-readable companion for required
stage fields, controlled statuses, duplicate IDs, missing references,
dependency cycles, and stage-heading consistency. It does not approve the
roadmap, execute a stage, or inspect source bodies.

Run the authorization/run integrity check with:

```text
python scripts/validate_source_processing.py
```

It checks catalogue processability gates, identified human approval,
classification/route/tool/environment compatibility, source hashes, stable
authorization and run IDs, and evidence-eligible run review. Catalogue
reconciliation is approved, all 57 processable sources have authorizations, and
the command is a CI gate.

For local review of ignored extraction derivatives, also run
`python scripts/validate_source_processing.py --verify-local-outputs`. This
mode requires every successful run output under `sources/extracted/`, verifies
that it exists locally, and recomputes its SHA-256. It is intentionally not a CI
gate because private derivatives are excluded from Git.

After an approved `repository_text_reader` run record has been created, execute
that specific run with:

```text
python scripts/extract_text.py --run-id RUN-NNNNNN --output sources/extracted/<approved-name>.txt
```

The command first runs source-processing validation, resolves the source only
under the configured source root, verifies its current hash against the run,
supports controlled text and HTML extensions, confines outputs to
`sources/extracted/`, requires internal/restricted output under the ignored
`sources/extracted/private/` path, refuses overwrite, and reports the derivative
hash. The operator must update and submit the run record for human review. It
does not create evidence or support PDF, office-document, image, or Pages
extraction.

`extract_pptx_text.py` is a proposed local reader for authorized PPTX runs. It
verifies the source hash and output boundary using the same controls, reads
slide XML in numeric slide order, and emits slide-labelled text for precise
locators. It does not extract speaker notes, chart workbooks, alt text, or text
embedded only in images. The tool must not process a source until its proposed
configuration/schema addition and the per-source authorization are approved.

Any future script must document inputs, outputs, side effects, approved
information route, exact command, failure behavior, generated-file boundary,
and relevant tests. A validator must state whether it checks YAML syntax, JSON
Schema, repository integrity, links, or another distinct contract.
