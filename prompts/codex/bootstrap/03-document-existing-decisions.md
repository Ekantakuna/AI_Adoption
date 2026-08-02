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
