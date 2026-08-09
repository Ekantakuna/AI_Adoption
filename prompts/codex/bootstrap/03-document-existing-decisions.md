---
id: PRM-CODEX-BOOT-003
title: Record existing architectural decisions
type: bootstrap
version: 1.1.0
status: active
owner_role: repository-maintainer
created_at: 2026-08-01
updated_at: 2026-08-05
roadmap_stage: bootstrap
source_access: repository_only
allowed_paths: [project/decisions, project/status, ARCHITECTURE.md, docs]
prohibited_actions: [commit, push, source_body_access, unsupported_claims]
required_inputs: [repository_evidence]
expected_outputs: [ADR_proposals, architecture_links, review_report]
validation: [repository_validators, tests, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Task: Record existing architectural decisions

Inspect the AI Adoption repository and identify architectural decisions that are
already demonstrated by implementation or existing policy.

Create ADRs only for decisions supported by repository evidence.

Likely areas to evaluate include:

- separation of evidence and knowledge
- Markdown and YAML as canonical tracked formats
- external source documents remaining outside Git
- stable identifiers
- metadata-only source catalogue
- human review before authoritative approval
- generated publications derived from structured knowledge
- agent documentation obligations

Do not assume every likely decision has already been made.

For every ADR:

- provide repository paths demonstrating the decision
- distinguish accepted implementation from proposed future architecture
- document alternatives and consequences
- use the next available ADR number
- do not modify the ADR template
- update architecture and index links where appropriate

Do not inspect external source-document contents.
Do not implement new capabilities.
Do not commit or push.

Run relevant validation and report:

- ADRs created
- evidence paths used
- decisions not documented because evidence was insufficient
- validation results
