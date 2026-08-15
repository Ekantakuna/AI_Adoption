# Local development

## Prerequisites

The repository has no application package manifest, lockfile, task runner, or
MkDocs configuration. Stage 9 requires Python and the pinned packages in
`requirements-validation.txt` for its validators, tests, and CI workflow. Do
not assume the existing `.venv/` is portable.

```sh
python -m pip install -r requirements-validation.txt
```

## Start a task

```sh
git branch --show-current
git status --short
rg --files
```

These commands show the active branch, tracked/untracked worktree changes, and
the non-ignored file inventory. `rg --files` does not list empty directories or
ignored local-only files, so inspect relevant directory structure separately
when those distinctions matter.

Read `AGENTS.md`, the relevant policy and directory documentation, controlled
configuration, schemas, tests, and `project/status/` before editing. Work on a
dedicated branch. Preserve existing worktree changes.

Do not enumerate or open external source bodies unless the task requires it and
the source-access gate is satisfied. Metadata inspection alone does not grant
content access.

## YAML parsing

If PyYAML is available, a repository-wide syntax check can be run with:

```sh
python - <<'PY'
from pathlib import Path
import yaml

for path in sorted(Path(".").rglob("*.yaml")):
    if ".git" in path.parts or ".venv" in path.parts:
        continue
    with path.open(encoding="utf-8") as stream:
        yaml.safe_load(stream)
    print(path)
PY
```

This checks YAML syntax only. Run the configured standards-based validator
separately:

```sh
python scripts/validate_schemas.py
```

That command meta-validates repository schemas, enables JSON Schema format
checks, validates `sources/catalogue.yaml` against `schemas/sources.yaml`, and
validates production knowledge records against configured object schemas.

## Tests and repository validation

Run the implemented repository checks from the repository root:

```sh
python scripts/validate_schemas.py
python scripts/validate_source_processing.py
python scripts/validate_knowledge.py
python scripts/validate_relationship_impact.py
python scripts/validate_prompts.py
python scripts/validate_roadmap.py
python -m unittest discover -s tests -p "test_*.py"
```

The source-processing validator is an active CI gate after approved catalogue
reconciliation. The CI workflow runs schema, source-processing, knowledge,
relationship/impact, prompt, and unit-test validation. Roadmap validation is
available locally but is not currently a CI step.
Documentation builds and publication validation remain unconfigured; the
repository text reader operates only against an approved run.

## Documentation checks

No MkDocs or other documentation build is configured. Review relative Markdown
links and Mermaid source manually or with an explicitly selected tool. Record
which method was used; do not state that a docs build passed when none exists.

## Finish a task

```sh
git diff --check
git diff --stat
git status --short
```

`git diff --check` detects whitespace errors in tracked-file diffs.
`git diff --stat` summarizes tracked changes but omits untracked file contents.
`git status --short` supplies that missing untracked-file view. Inspect the full
tracked diff and read each relevant untracked file before handoff.

Also run all newly applicable validators and tests. Review the full diff for
unsupported claims, accidental source material, changed stable IDs, and
unrelated edits. Report unavailable checks and unresolved conflicts.

Do not commit or push unless explicitly authorized.
