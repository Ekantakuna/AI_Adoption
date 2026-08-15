---
id: ADR-0012
title: Control assessment scoring and audience use before Stage 12
status: accepted
date: 2026-08-14
reviewed_by: MZ
reviewed_at: 2026-08-15
decision_owners:
  - authorized human reviewers
  - roadmap maintainers
supersedes:
superseded_by:
---

# ADR-0012 — Control assessment scoring and audience use before Stage 12

## Context

The approved roadmap requires reviewed knowledge and relationship integrity plus
approved scoring and audience controls before Stage 12 begins. Stages 10 and 11
are implemented and closed. Before the decisions recorded below,
`config/scoring_models.yaml` and `config/audiences.yaml` were empty and no
approved concrete scoring model or audience record existed.

Accepted ADR-0007 reserves approval of current-state conclusions, target-state
commitments, organizational recommendations, executive claims, and audience
release to authorized humans. Accepted ADR-0008 keeps audience outputs
replaceable and subordinate to reviewed canonical inputs. Information-handling
rules require derivatives to inherit the highest input classification.

MZ accepted this AI-authored control framework and its stable identifier forms
on 2026-08-15. That acceptance does not approve a concrete scoring model,
audience, classification permission, ownership assignment, assessment,
publication, or configuration implementation.

## Decision

### Scoring controls

Every scoring model must be a versioned controlled record with:

- a stable, never-reused `SCORE-NNNNNN` identifier;
- name, purpose, owner, lifecycle status, version, and applicable assessment
  types;
- dimensions and an explicit scale type, ordered values, labels, definitions,
  and any numeric thresholds;
- required canonical evidence and knowledge inputs;
- explicit missing, not-applicable, disputed, and insufficient-evidence
  behavior;
- an explicit aggregation formula, weighting, rounding, and minimum coverage,
  or a declaration that aggregation is prohibited;
- confidence represented separately from the score;
- conflict visibility and a prohibition on silently selecting one conflicting
  input;
- reviewer identity and review date for an `approved` state; and
- version/supersession rules that preserve the model used by historical
  assessments.

No repository-wide default scale or aggregation is implied. Missing or
insufficient evidence must not become a zero. A higher score must not be
interpreted as higher confidence. AI-generated scores remain draft until an
authorized human approves the assessment conclusion and, separately, any
target-state commitment.

### Audience controls

Every audience definition must be a versioned controlled record with:

- a stable, never-reused `AUD-NNNNNN` identifier;
- name, purpose, owner, lifecycle status, version, and intended recipient role
  or group;
- an explicit set of allowed classifications and prohibited content;
- permitted claim types and required approvals;
- rules for unresolved conflicts, provisional material, and recommendations;
- release reviewer identity and review date for an `approved` state; and
- version/supersession rules preserving the audience definition used by a
  historical derivative.

`public`, `internal`, and `restricted` permissions must be granted explicitly;
no ordering alone grants access. `unclassified` source bodies and derivatives
are ineligible. Every derivative inherits the highest classification of its
inputs, and audience fit does not replace evidence, classification, assessment,
or release review.

The existing `executive`, `board`, `employees`, and `technical` publication
directories are scaffolding. They do not establish approved audience IDs,
membership, classification permissions, or release authority.

### Approved initial audience

On 2026-08-15, MZ approved `AUD-000001`, **Internal assessment reviewers**, as
the only initial Stage 12 audience. It may receive `public` and `internal`
review material through approved tools and accounts. Access remains limited to
separately authorized internal human reviewers.

The audience prohibits `restricted` or `unclassified` material, source bodies,
secrets, credentials, unapproved personal information, unreviewed content
represented as authoritative, silent conflict resolution, and public or
external release. The `executive`, `board`, `employees`, and `technical`
directories remain unapproved scaffolding. Record version and configuration
implementation remain separate decisions.

### Approved ownership and authority

On 2026-08-15, MZ approved these assignments:

- the roadmap maintainer may mechanically maintain the accepted unscored
  control but cannot change its approved semantics;
- the repository maintainer may mechanically maintain `AUD-000001` but cannot
  add recipients, classifications, or release permissions;
- MZ authorizes audience membership, approves Stage 12 assessments, and
  approves internal distribution to `AUD-000001`;
- AI agents and stage implementers may draft and validate only; and
- no scoring-model owner exists while Stage 12 remains unscored. A future model
  requires separate ownership and approval.

Public or external release remains prohibited. Mechanical maintenance does not
confer approval authority.

### Canonical and lifecycle boundaries

Scoring models and audience records are controlled inputs. Assessments and
outlook modules cite the exact model and audience versions they use; rendered
reports and presentations remain replaceable derivatives. A model or audience
record may move through `proposed`, `draft`, `in_review`, `approved`,
`superseded`, and `retired`. Supersession does not rewrite historical scores or
release decisions.

Stage 12 must validate identifiers, versions, controlled lifecycle states,
scale completeness, missing-value rules, evidence references, conflict
visibility, classification compatibility, and reviewer metadata. Validation
cannot determine whether a score, organizational target, recipient membership,
or release decision is substantively correct.

## Alternatives considered

### Infer controls from empty configuration and directory names

Rejected because empty files and scaffolding are not approved policy or
organizational authorization.

### Use one implicit maturity scale for every assessment

Rejected because different dimensions may require different semantics and an
implicit scale would hide interpretation and weighting choices.

### Treat audience fit as publication approval

Rejected because classification, evidence, claim authority, and release review
are independent controls.

## Consequences and limitations

Acceptance of this contract establishes guardrails but does not approve any
concrete model or audience record. An authorized human may instead require the
first assessment to remain explicitly unscored. Stage 12 remains blocked until
either an applicable scoring model or that unscored approach and every audience
used by its outputs are explicitly approved.
Assessment schemas, records, scoring execution, outlook modules, publication
generation, and automatic invalidation remain unimplemented.

## Review record and remaining human decisions

On 2026-08-15, MZ accepted the scoring and audience control rules and approved
the `SCORE-NNNNNN` and `AUD-NNNNNN` stable identifier forms. MZ explicitly did
not approve any concrete model, audience, permission, owner, assessment,
publication, or configuration implementation.

On 2026-08-15, MZ approved an unscored first Stage 12 assessment. It must not
use numeric or ordinal scores, weights, aggregation, ranking, or implied
maturity levels. It must distinguish claim types, cite reviewed upstream
records, expose missing or disputed evidence, and preserve human approval
boundaries. This decision does not approve assessment content, conclusions,
recommendations, or target-state commitments.

On 2026-08-15, MZ approved `AUD-000001` and its permissions, followed by the
ownership and authority assignments recorded above.

No Stage 12 entry-control governance decision remains pending. On 2026-08-15,
MZ authorized implementation of the approved unscored mode and `AUD-000001`
version `1.0.0`, including narrow schemas, validation, tests, and documentation.
That authorization did not approve a scoring model, another audience,
assessment content, outlook content, or Stage 12 execution.

The controls are implemented in `config/scoring_models.yaml` and
`config/audiences.yaml` and validated by their Draft 2020-12 schemas. Stage 12
remains blocked by repository/Git readiness until the existing Stage 11 change
set is preserved and a clean Stage 12 branch is established.

## References

- [Approved roadmap](../roadmap.yaml)
- [Stage 11 status](../status/stage-11-knowledge-graph-impact-integrity.md)
- [Information-handling rules](../information-handling.md)
- [Human authority decision](ADR-0007-human-review-for-authority.md)
- [Publication derivative decision](ADR-0008-publications-are-derivatives.md)
- [Publication pipeline](../../docs/architecture/publication-pipeline.md)
- [Configuration contract](../../config/README.md)
