---
id: ADR-0007
title: Require human review before authoritative approval
status: proposed
date: 2026-07-30
decision_owners:
  - authorized human reviewers
supersedes:
superseded_by:
---

# ADR-0007 — Require human review before authoritative approval

## Context

The authoritative agent contract and information-handling policy prohibit an AI
agent from approving its own outputs. Human review gates source classification
and processing, authoritative evidence and knowledge, organizational
conclusions and commitments, recommendations presented as decisions, and
publication-ready executive claims.

The review boundary is proposed policy. Workflow enforcement remains
incomplete or absent.

## Decision

Only an authorized human reviewer may approve:

- source classification, processing routes, and extraction tools;
- promotion into authoritative evidence or knowledge;
- current-state conclusions and target-state commitments;
- conflict resolutions and organizational recommendations;
- publication-ready executive claims and audience release.

Agents may create clearly labelled drafts, proposals, inventories, and review
packets within an approved handling route. Tracking, schema validity,
confidence, generation, or agent authorship does not constitute approval.
Reviewer identity and review state must be preserved where the applicable
schema supports them.

## Rationale

These decisions carry evidentiary, organizational, and information-handling
authority that cannot be inferred from automated output.

## Alternatives considered

### Allow agents to self-approve high-confidence output

Not selected because confidence does not confer organizational authority or
resolve handling and evidence risks.

### Treat merge or Git tracking as approval

Not selected because repository state does not identify the review mandate,
scope, or decision.

### Require human review for every mechanical change

Not selected because agents may perform bounded inventory, drafting, and
validation work; the approval boundary applies to authoritative states and
specified governance decisions.

## Consequences

### Positive

- Authority and accountability remain with designated reviewers.
- Draft and approved content remain distinguishable.
- Sensitive processing and organizational claims receive explicit oversight.

### Negative

- Publication and knowledge promotion depend on reviewer availability.
- Object schemas must carry sufficient review metadata.

### Risks

- Inconsistent narrative labels may obscure status until structured contracts
  exist.
- A reviewer may approve a narrow item that is later represented too broadly.

## Implementation implications

`AGENTS.md`, `project/information-handling.md`, and
`project/source-management-policy.md` define mandatory gates. Approved ADRs and
schemas can record reviewer identity and date, as demonstrated by ADR-0002 and
the source schema.

Assessment, knowledge, and publication review workflows are not implemented.
This decision establishes the authority boundary, not an automated approval
system, and no repository-wide validator can determine whether a named
reviewer is authorized.

## Validation

Check that authoritative records identify an authorized reviewer and review
state where supported, that AI-authored material remains draft or proposed
until review, and that approval scope is not expanded by inference. No
repository-wide approval validator exists.

## References

- [Agent operating contract](../../AGENTS.md)
- [Information-handling rules](../information-handling.md)
- [Source management policy](../source-management-policy.md)
- [Contribution guide](../../CONTRIBUTING.md)
- [Approved source-schema decision](0002-canonical-source-catalogue-schema.md)
- [Repository architecture](../../ARCHITECTURE.md)
