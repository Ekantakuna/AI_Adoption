# Registers

This directory contains canonical structured YAML records for project entities, controls, evidence links, and delivery tracking.

`sources.yaml` is the canonical source inventory. It contains metadata-only records for original evidence retained outside Git; source records must not be maintained separately in `sources/catalogue.yaml`.

`terms.yaml` is the canonical glossary and vocabulary inventory. It remains empty until term records comply with `schemas/term.schema.yaml` and the applicable source-processing controls.

Current-state records are separated by responsibility:

- `use-cases.yaml` stores reusable or possible use-case patterns;
- `implementations.yaml` stores actual pilots, deployments and in-house or externally sourced implementations;
- `implementation-snapshots.yaml` stores append-only AS-IS observations over time;
- `solutions.yaml` stores reusable technical-solution metadata;
- `initiatives.yaml` stores delivery projects and links them to implementations.

Value metrics, risks, controls, dependencies, capabilities and stakeholders remain in their dedicated registers and are referenced by stable IDs.

`capabilities.yaml` stores reusable organizational or technical capabilities. `competencies.yaml` stores reusable role-level knowledge, skill, behavior, experience and certification requirements; organization and people records reference them by stable ID.

Governance records form a separate but linked evidence chain:

- `governance-targets.yaml` stores versioned TO-BE scope, characteristics and intended outcomes;
- `governance-operating-models.yaml` stores current, transitional or target accountability structures;
- `governance-artifacts.yaml` inventories policies, standards, procedures, How-Tos, playbooks and charters;
- `governance-roles.yaml` stores roles, boards, committees and forums;
- `governance-capabilities.yaml` connects organizational, process, control, information, skill and technology dimensions;
- `governance-tool-requirements.yaml` stores vendor-neutral tooling and automation requirements;
- `governance-assessments.yaml` and `governance-findings.yaml` store dated evidence-backed evaluations and granular findings;
- `governance-actions.yaml` stores organizational and technical pathway actions linked to approved gaps;
- shared `risks.yaml` and `controls.yaml` provide many-to-many risk-treatment and lifecycle-control records.

Governance registers remain empty until source access is approved or manually proposed records are reviewed. Empty registers are intentional and contain no statement about the organization.

Organization records form an AS-IS to TO-BE value-operating-model chain:

- `organization-targets.yaml` stores versioned organizational vision, principles and target characteristics;
- `organization-operating-models.yaml` stores current, transitional or target structures, value flow and interfaces;
- `organization-units.yaml` stores units, teams, CoE options and enabling functions;
- `organization-roles.yaml` stores role definitions such as AI leader, team and champion roles without naming appointees and links them to shared competencies;
- `organization-networks.yaml` stores communities of practice and cross-functional champion networks;
- `organization-practices.yaml` stores ways of working and AI value-flow processes;
- `partnership-requirements.yaml` stores capability-based partnership needs without selecting providers;
- `organization-tool-requirements.yaml` stores vendor-neutral work, knowledge, portfolio and collaboration requirements;
- `organization-assessments.yaml` and `organization-findings.yaml` store dated evidence-backed evaluations;
- `organization-actions.yaml` stores structure, role, practice, network, partnership, tooling and change actions linked to approved gaps.

Organization registers remain empty until records meet their evidence and review requirements.

People-and-culture records support planning and repeatable reporting:

- `ai-change-plans.yaml` stores versioned scope, phases, timelines and responsibility assignments;
- `ai-change-actions.yaml` stores owned change, communication, literacy, readiness and reinforcement actions;
- `ai-awareness-campaigns.yaml` stores audience, message, channel, schedule and reach metadata;
- `ai-literacy-programs.yaml` stores role-based learning pathways, outcomes, delivery and evaluation;
- `workforce-impact-assessments.yaml` and `workforce-impacts.yaml` store assessment headers and granular role, task, competency and capacity impacts;
- `employee-readiness-assessments.yaml` and `employee-readiness-findings.yaml` store privacy-safe aggregate readiness evidence;
- `people-change-snapshots.yaml` stores append-only status, metric, risk, blocker and decision snapshots for reporting.

Named employees and person-level readiness records are prohibited by default. Champion structures reference shared organization roles and networks; capabilities, competencies, stakeholders, initiatives, milestones, risks and metrics remain shared registers.

Strategic-intent records form a versioned strategy, challenge and execution system:

- `ai-strategies.yaml` stores vision, transformation thesis, target state and version lineage;
- `strategic-objectives.yaml` stores outcome-oriented objectives linked to required metrics;
- `strategic-choices.yaml` stores alternatives, trade-offs, criteria and rationale;
- `strategic-hypotheses.yaml` stores causal hypotheses, tests and falsification criteria;
- `strategy-scenarios.yaml` and `strategy-simulations.yaml` store possible futures and reproducible non-factual challenge runs;
- `decision-intelligence-targets.yaml` stores the target intelligent choice architecture and its five mandatory properties;
- `critical-success-factors.yaml` stores required success conditions and leading indicators;
- `strategy-execution-plans.yaml` links objectives to initiatives, capabilities, milestones, dependencies and intervention rules;
- `strategy-assessments.yaml` and `strategy-findings.yaml` store dated progress, outcome, assumption and adaptation evidence;
- `strategy-change-events.yaml` preserves immutable strategy and execution-plan evolution;
- shared `metrics.yaml` stores outcome measures, leading and lagging indicators, operational measures and guardrails.

Strategy and execution registers remain empty until collaborative strategy development and approved evidence analysis begin.

Decision-environment records form a traceable decision and learning lifecycle:

- `decision-types.yaml` stores reusable decision classes, triggers, cadence and materiality;
- `decision-contexts.yaml` stores versioned business problems, semantics, assumptions and constraints;
- `choice-architectures.yaml` stores option-generation, evaluation, authority, orchestration and observability design;
- `decision-authority-rules.yaml` stores human decision rights, delegation, override, escalation and prohibited actions;
- `decisions.yaml` stores actual decision instances and preserves options, evidence, authorization and rationale;
- `decision-options.yaml` and `decision-evidence.yaml` distinguish alternatives from facts, predictions, forecasts, scenarios, simulations and judgement;
- `decision-outcomes.yaml` stores time-stamped expected, actual and unintended results;
- `decision-learning-events.yaml` stores reviewed changes derived from outcomes and feedback;
- `decision-environment-assessments.yaml` stores evidence-backed current-state, target-state, gap, quality and learning assessments.

These records reference shared terms, stakeholders, solutions, initiatives, risks, controls, metrics, capabilities and dependencies. Empty registers make no claim about current decision practices.

Ecosystem-sourcing records cover the complete external-provider lifecycle:

- `ecosystem-providers.yaml` stores provider identity, capabilities, jurisdictions and relationship metadata;
- `ecosystem-offerings.yaml` stores model, service, platform, data, software, advisory or delivery offerings;
- `sourcing-cases.yaml` links partnership requirements and strategic choices to candidates, evaluations and decisions;
- `provider-evaluations.yaml` stores approved criteria, scorecards, evidence, limitations and recommendations;
- `provider-due-diligence.yaml` stores independent domain outcomes, conditions, risks, controls and remediation;
- `sourcing-agreements.yaml` stores repository-safe agreement, obligation and service-level metadata;
- `provider-performance.yaml` stores dated service, value, risk, relationship and renewal reviews;
- `sourcing-exit-plans.yaml` stores portability, continuity, replacement, data disposition and transition plans.

These records reference shared partnership requirements, strategic choices, solutions, risks, controls, metrics and dependencies by stable ID. Original agreements and restricted commercial terms remain outside Git.

Maturity records form an evidence chain:

- `maturity-frameworks.yaml` combines the approved models and aggregation approach;
- `maturity-models.yaml` stores versioned dimensions, levels, characteristics and criteria;
- `maturity-assessments.yaml` stores time-stamped assessment scope and overall conclusions;
- `maturity-findings.yaml` stores granular qualitative and quantitative arguments with evidence;
- `maturity-actions.yaml` stores improvement-pathway actions linked to gaps and findings.

Historical approved assessments and findings are retained rather than overwritten so progress can be compared over time.
