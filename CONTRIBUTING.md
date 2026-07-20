# Contributing

Contributions should keep the repository traceable, reviewable, and safe for the information it contains.

## Before making changes

- Work on a dedicated branch.
- Read `AGENTS.md` and `project/information-handling.md`.
- Confirm that any source material has an assigned classification and approved processing route.
- Do not add credentials, personal information, production datasets, or unreviewed restricted material.
- Treat `sources/extracted/private/` as non-versioned content. Do not assume that other extracted artifacts are safe to track merely because Git does not ignore them.

## Content rules

- Separate facts, assumptions, inferences, and recommendations explicitly.
- Cite source or evidence identifiers rather than making unsupported claims.
- Preserve existing stable record IDs; never reuse an ID for a different record.
- Use domain IDs from `config/taxonomy.yaml` and controlled values from `config/project.yaml`.
- Keep Markdown and YAML registers canonical; generated outputs should be reproducible from them.
- Do not create strategy conclusions as part of repository maintenance.

## YAML registers

Register files use this foundation shape:

```yaml
schema_version: 1
register: example
records: []
```

Every register must have an approved register-specific schema before its first record is added. Do not invent a register-specific field model before that approval. Keep an unused register's `records` value as an empty list.

## Review checklist

1. Parse all YAML files with an available safe YAML parser or project validator.
2. Run the available Markdown checks.
3. Confirm that links and referenced identifiers resolve where validation supports it.
4. Review `git status` and `git diff --stat`.
5. Summarize changed files and identify decisions still required.

Do not commit or push unless explicitly authorized.
