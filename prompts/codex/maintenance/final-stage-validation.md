# Task: Perform final stage validation

Inspect all current uncommitted changes.

Read `AGENTS.md` and the current stage status document.

Validate:

- YAML syntax
- schemas
- controlled values
- identifier uniqueness
- cross-file references
- source-catalogue references
- evidence references
- tests
- documentation links
- documentation alignment with implementation
- stage status completeness
- changelog impact
- ADR impact
- Git whitespace errors

Run all existing repository validators and tests.

Run:

- `git diff --check`
- `git status --short`
- `git diff --stat`

Do not make unrelated improvements.

Correct defects that are directly caused by the current stage.

Do not commit or push.

Report:

1. Commands executed
2. Passed checks
3. Failed checks corrected
4. Remaining failures
5. Files changed during validation
6. Whether the stage is ready for human review and commit
