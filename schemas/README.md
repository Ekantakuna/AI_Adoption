# Schemas

This directory is reserved for machine-readable contracts used to validate configuration, registers, and source metadata.

Each register requires its own approved schema before records may be added. Until a schema is approved, the corresponding register must retain an empty `records` list.

The current-state model separates use-case patterns, actual implementations, time-stamped implementation snapshots and reusable technical solutions. Business domains and AI techniques are controlled independently so records can be updated without rewriting historical evidence.

Approved current-state contracts are:

- `use-case.schema.yaml` for reusable or possible patterns;
- `implementation.schema.yaml` for actual pilots and deployments;
- `implementation-snapshot.schema.yaml` for append-only AS-IS observations;
- `solution.schema.yaml` for technical solutions and shared platforms;
- `initiative.schema.yaml` for project summaries;
- `business-domain.schema.yaml` and `ai-technique.schema.yaml` for controlled vocabularies.

`capability.schema.yaml` and `competency.schema.yaml` provide shared contracts for target-state capabilities and role-level competency requirements across organization, people, governance and technical domains.

The machine-readable register mapping is maintained in `config/record-types.yaml`.

`source.schema.yaml` controls the metadata-only source catalogue. It separates confirmed and proposed taxonomy relationships, requires custody history and handling gates, and permits unset hash and inspection fields while content access remains unapproved.

Governance contracts are:

- `governance-target.schema.yaml` for versioned TO-BE profiles;
- `governance-operating-model.schema.yaml` for roles, decisions, escalation and cadence;
- `governance-artifact.schema.yaml` for policy and guidance metadata;
- `governance-role.schema.yaml` for roles and cross-functional bodies;
- `governance-capability.schema.yaml` for organizational and technical capability design;
- `governance-tool-requirement.schema.yaml` for vendor-neutral software and automation needs;
- `governance-assessment.schema.yaml` and `governance-finding.schema.yaml` for evidence-backed evaluation;
- `governance-action.schema.yaml` for implementation-pathway measures;
- `risk.schema.yaml` and `control.schema.yaml` for shared lifecycle risk and treatment records.

Organization contracts are:

- `organization-target.schema.yaml` and `organization-operating-model.schema.yaml` for the organizational vision and value operating model;
- `organization-unit.schema.yaml` and `organization-role.schema.yaml` for structures, responsibilities, capacity and competencies;
- `organization-network.schema.yaml` for communities of practice and champion networks;
- `organization-practice.schema.yaml` for ways of working and value flow;
- `partnership-requirement.schema.yaml` and `organization-tool-requirement.schema.yaml` for vendor-neutral enablement needs;
- `organization-assessment.schema.yaml` and `organization-finding.schema.yaml` for evidence-backed AS-IS, TO-BE and gap evaluation;
- `organization-action.schema.yaml` for approved-gap-driven pathway measures.

People-and-culture contracts are:

- `ai-change-plan.schema.yaml` and `ai-change-action.schema.yaml` for scope, timeline, responsibilities and execution;
- `ai-awareness-campaign.schema.yaml` for audience communications and reach;
- `ai-literacy-program.schema.yaml` for role-based learning and competency outcomes;
- `workforce-impact-assessment.schema.yaml` and `workforce-impact.schema.yaml` for evidence-backed workforce change;
- `employee-readiness-assessment.schema.yaml` and `employee-readiness-finding.schema.yaml` for privacy-safe aggregate readiness;
- `people-change-snapshot.schema.yaml` for append-only progress and reporting history.

Strategic-intent contracts are:

- `ai-strategy.schema.yaml` for versioned vision, transformation thesis and target state;
- `strategic-objective.schema.yaml` for measurable outcome-oriented objectives;
- `strategic-choice.schema.yaml` and `strategic-hypothesis.schema.yaml` for alternatives, rationale and testable causal logic;
- `strategy-scenario.schema.yaml` and `strategy-simulation.schema.yaml` for structured uncertainty and non-factual challenge runs;
- `decision-intelligence-target.schema.yaml` for the five-property intelligent choice architecture;
- `critical-success-factor.schema.yaml` and `metric.schema.yaml` for success conditions and early indicators;
- `strategy-execution-plan.schema.yaml` for cross-domain execution and intervention controls;
- `strategy-assessment.schema.yaml` and `strategy-finding.schema.yaml` for outcome, assumption and execution evaluation;
- `strategy-change-event.schema.yaml` for immutable strategy-version history.

Decision-environment contracts are:

- `decision-type.schema.yaml` and `decision-context.schema.yaml` for recurring decisions and their semantic business context;
- `choice-architecture.schema.yaml` for controlled framing, option, evidence, evaluation, authority and observability design;
- `decision-authority-rule.schema.yaml` for human rights, delegation, override, escalation and automation boundaries;
- `decision.schema.yaml`, `decision-option.schema.yaml` and `decision-evidence.schema.yaml` for actual choices and their traceable inputs;
- `decision-outcome.schema.yaml` and `decision-learning-event.schema.yaml` for outcome-linked feedback and controlled evolution;
- `decision-environment-assessment.schema.yaml` for evidence-backed capability, quality, control and learning assessment.

Data-domain contracts are:

- `data-readiness-target.schema.yaml` and `data-requirement.schema.yaml` for target readiness and contextual AI data needs;
- `data-product.schema.yaml` and `data-capability-profile.schema.yaml` for reusable data products and capability design;
- `data-governance-requirement.schema.yaml` for AI-specific governance extension requirements;
- `data-quality-framework.schema.yaml` and `data-quality-rule.schema.yaml` for contextual quality dimensions, thresholds and rules;
- `data-practice.schema.yaml` and `data-observability-check.schema.yaml` for lifecycle, metadata, analytics and reliability practices;
- `data-assessment.schema.yaml`, `data-finding.schema.yaml` and `data-action.schema.yaml` for evidence-backed evaluation and improvement.

Agentic-AI contracts are:

- `agentic-concept.schema.yaml` and `agentic-technology-signal.schema.yaml` for definitions, evolution and emerging change;
- `agent-profile.schema.yaml`, `agentic-platform-requirement.schema.yaml`, `agentic-architecture.schema.yaml` and `agentic-pattern.schema.yaml` for controlled agent design;
- `agentic-workflow.schema.yaml` and `agentic-workflow-run.schema.yaml` for human-accountable workflow design and append-only execution;
- `agent-evaluation.schema.yaml` for reproducible capability, safety, control and operational evidence;
- `agentic-operating-model.schema.yaml` for the human-agent operating-company model;
- `agentic-assessment.schema.yaml`, `agentic-finding.schema.yaml` and `agentic-action.schema.yaml` for evidence-backed transition.

Security-and-trust contracts are:

- `security-trust-target.schema.yaml` and `security-trust-requirement.schema.yaml` for intended trust outcomes and measurable requirements;
- `threat-model.schema.yaml` for assets, actors, threats, attack paths, failure modes and exposure;
- `security-trust-architecture.schema.yaml` and `security-trust-practice.schema.yaml` for protection design and secure-lifecycle practices;
- `security-test.schema.yaml` for reproducible test scope, method, results, limitations and findings;
- `assurance-case.schema.yaml` for bounded claims supported by explicit arguments and evidence;
- `security-trust-event.schema.yaml` for detection, response, recovery and lessons;
- `security-trust-assessment.schema.yaml`, `security-trust-finding.schema.yaml` and `security-trust-action.schema.yaml` for evidence-backed evaluation and improvement.

Engineering-platform contracts are:

- `engineering-requirement.schema.yaml`, `engineering-option.schema.yaml` and `technology-evaluation.schema.yaml` for vendor-neutral needs, alternatives and evidence-backed technical comparison;
- `reference-architecture.schema.yaml` and `engineering-design-pattern.schema.yaml` for versioned architecture and reusable pattern design;
- `engineering-practice.schema.yaml` for engineering, observability, operation, catalogue and documentation practices;
- `ai-ux-pattern.schema.yaml` for human-AI interaction, control, feedback, recovery and accessibility;
- `ai-catalogue-entry.schema.yaml` for governed entity inventory and documentation;
- `catalogue-assurance-check.schema.yaml` for security, risk, control and compliance evidence checks;
- `engineering-assessment.schema.yaml`, `engineering-finding.schema.yaml` and `engineering-action.schema.yaml` for evidence-backed evaluation, granular findings and improvement.

Ecosystem-sourcing contracts are:

- `ecosystem-provider.schema.yaml` and `ecosystem-offering.schema.yaml` for evidence-backed provider and service metadata;
- `sourcing-case.schema.yaml` for partnership-requirement and strategic-choice-driven sourcing workflows;
- `provider-evaluation.schema.yaml` for approved criteria and evidenced scorecards;
- `provider-due-diligence.schema.yaml` for independent multi-domain review outcomes;
- `sourcing-agreement.schema.yaml` for repository-safe agreement and obligation metadata;
- `provider-performance.schema.yaml` for metric-backed service, value, risk and renewal reviews;
- `sourcing-exit-plan.schema.yaml` for portability, continuity, transition and termination controls.

Maturity contracts are:

- `maturity-framework.schema.yaml` for a versioned combination of models and aggregation rules;
- `maturity-model.schema.yaml` for dimensions, levels, characteristics and criteria;
- `maturity-assessment.schema.yaml` for assessment scope, comparison and overall conclusion;
- `maturity-finding.schema.yaml` for granular qualitative and quantitative evidence-backed judgements;
- `maturity-action.schema.yaml` for improvement actions linked to findings and gaps.
