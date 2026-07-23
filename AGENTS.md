# Repository agent guidance

These rules apply throughout the repository:

- never invent company facts;
- distinguish facts, assumptions, inferences and recommendations;
- preserve source provenance;
- work on branches;
- do not commit or push without explicit permission;
- run validation before finishing;
- show changed files and diff summary;
- preserve stable record IDs;
- treat Markdown and registers as the canonical source.

Do not process source documents until their classification and handling requirements have been recorded and reviewed.

## Agentic-native project operation

- humans remain accountable for scope, source access, classifications, decisions, material changes, publication, commit and push;
- agents may plan, analyze permitted information, propose changes, execute authorized repository work, validate outputs and report evidence;
- agents must not approve their own outputs or represent proposals as approved facts;
- every material agent-operated workflow must expose its inputs, outputs, assumptions, tools, validation and required human gates;
- human override, rejection, escalation and rollback paths must remain available;
- agentic workflow definitions and runs use the canonical records controlled in `config/agentic-ai.yaml`.
