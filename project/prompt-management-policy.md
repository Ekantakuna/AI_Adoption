# Prompt management policy

Prompts under `prompts/codex/` are version-controlled instruction assets for
repeatable repository work. They are not evidence, knowledge records, policy
approval, or proof that a task has run.

Every prompt, including templates, has YAML front matter with a stable `id`,
version, lifecycle `status`, owner, stage, source-access boundary, allowed
paths, prohibited actions, inputs, outputs, validation, human-review
requirement, and supersession fields. Active production prompts are listed in
`prompts/codex/prompt-catalogue.yaml`; templates are identifiable but are not
execution prompts.

Stable IDs are never reused. Material revisions increment the version and
update `updated_at` and the catalogue. Obsolete prompts are deprecated,
superseded, or retired, with a replacement recorded when applicable. Prompt
changes are reviewed like implementation changes. Prompts must contain no
secrets, credentials, personal information, or source-document bodies.

The validator checks metadata, catalogue integrity, and controlled values. It
does not execute prompts, prove outputs were produced, assess prompt quality, or
grant source access. Human review remains required for policies, authoritative
knowledge, organizational conclusions, commitments, and publication claims.
