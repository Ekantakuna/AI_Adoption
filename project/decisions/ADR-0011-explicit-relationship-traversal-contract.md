---
id: ADR-0011
title: Traverse explicit knowledge relationships without replacing canonical records
status: accepted
date: 2026-08-14
reviewed_by: MZ
reviewed_at: 2026-08-14
decision_owners:
  - repository maintainers
  - authorized human reviewers
supersedes:
superseded_by:
---

# ADR-0011 — Explicit relationship traversal contract

## Proposal status and approval boundary

This ADR is the accepted traversal contract required by the `stage-11` entry
gate in `ROADMAP-000001`. MZ reviewed and approved the complete contract on
2026-08-14. Contract approval permits Stage 11 implementation but does not by
itself make relationship traversal operational.

Approval of this contract would approve the traversal architecture and
integrity rules below. It would not approve any production relationship,
knowledge claim, impact conclusion, Stage 11 implementation, or later automated
invalidation.

## Context

Stage 9 established approved stable `REL-NNNNNN` identifiers, relationship
records between existing non-evidence knowledge objects, evidence references,
review states, and basic endpoint integrity. Stage 10 closed without creating a
relationship because its bounded pilot had only one justified knowledge
endpoint. The repository has no production relationship records and no
controlled traversal or impact implementation.

Stage 11 requires an approved traversal contract before implementation. The
contract must let maintainers find explicitly referenced downstream objects
without inferring semantic links, hiding conflicts, or creating a graph-specific
source of truth.

## Decision

If accepted, Stage 11 will implement traversal as a replaceable, read-only view
constructed from canonical repository records. Canonical evidence, knowledge,
and `REL` records remain authoritative. Traversal results, indexes, paths, and
impact reports are derivatives and must not contain the only copy of a claim,
review decision, conflict, or provenance fact.

The initial implementation will build its index in memory for each invocation.
It will not add a persistent graph store. It will use stable IDs and explicit
fields only; titles, similar wording, embeddings, and inferred semantic
proximity do not create edges.

## Canonical inputs and graph projection

The projection has two kinds of explicit input:

1. `evidence_ids` creates a dependency from an `EVID` record to each canonical
   knowledge or relationship record that cites it; and
2. each canonical `REL` record contributes its declared `from_id`, `to_id`, and
   `relationship_type` semantics.

Evidence records and non-relationship knowledge records are addressable nodes.
A `REL` record remains a canonical, evidence-backed knowledge record but acts as
an edge in traversal. The projection must retain its `REL` ID, evidence IDs,
classification, origin, and review status in traversal output.

An active reviewed view includes only records whose review state is `verified`
or `approved`. Draft, `needs_review`, and `under_review` records are available
only through an explicit audit option and must be labelled non-authoritative.
Rejected records are excluded from active traversal. Deprecated records remain
addressable for history under the rules below.

## Relationship direction and semantics

All endpoints must be existing non-evidence, non-relationship knowledge
objects. Unless narrowed below, configured knowledge-object types may appear at
either endpoint.

| Type | Stored direction | Meaning | Impact direction | Additional constraint |
| --- | --- | --- | --- | --- |
| `supports` | supporter → supported object | The source object provides explicit support for the target interpretation. | from → to | Evidence must support the asserted link. |
| `contradicts` | statement A ↔ statement B | The objects retain materially conflicting interpretations. | both directions | Traversal treats one record as symmetric and keeps the conflict unresolved. |
| `refines` | narrower → broader | The source makes the target more specific without silently replacing it. | both directions | Neither endpoint is deprecated automatically. |
| `depends_on` | dependent → dependency | The source requires the target for its stated meaning or use. | to → from | Directed dependency cycles are structurally invalid. |
| `influences` | influencing object → affected object | The source is explicitly stated to influence the target. | from → to | Influence is not treated as causation unless the canonical record says so. |
| `measures` | metric → measured object | A metric measures an aspect of the target. | to → from | The source must be a `METRIC` record. |
| `mitigates` | mitigating object → risk | The source is explicitly presented as reducing or controlling the target risk. | both directions | The target must be a `RISK` record. |
| `relates_to` | object A ↔ object B | A reviewed association exists without a stronger approved semantic type. | both directions | It must not be used as an evidence-free inferred similarity edge. |
| `supersedes` | replacement → replaced object | The source replaces the target for future use while preserving its identity and history. | to → from | Endpoints must have the same object type; the target must be `deprecated`; cycles are invalid. |

A self-relation is prohibited for every relationship type. One symmetric
relationship represents both traversal directions; a reverse `contradicts` or
`relates_to` record is a semantic duplicate requiring review, not a second
directional edge.

## Relationship lifecycle and review

Relationship records use the approved knowledge lifecycle:

`draft` → `needs_review` → `under_review` → `verified` or `approved`

A reviewer may instead record `rejected`; a retained relationship may later be
`deprecated`. IDs remain stable and are never reused. AI-origin relationships
start only as `draft` or `needs_review`, retain `origin: ai`, and cannot become
reviewed without identified human reviewer metadata.

Every relationship requires at least one existing `EVID` reference. Review
must check endpoint identity, type semantics, direction, evidence coverage,
classification, conflicts, and downstream impact. Validation establishes
integrity, not semantic truth or approval.

Deprecation keeps the relationship addressable for audit but removes it from
the active reviewed traversal. Rejection does not delete the record. A
replacement relationship receives a new stable ID; the prior ID is not edited
to represent a different relationship.

## Traversal rules

The Stage 11 operation will accept a stable start ID, traversal mode, and
maximum depth. Depth is the number of explicit edges from the start node.

- Default depth is `1`.
- The caller may request an integer depth from `0` through `25`.
- Unbounded traversal is prohibited.
- `upstream` follows references toward evidence or declared prerequisites.
- `downstream` follows explicit consumers and stored relationship direction.
- `both` returns both upstream and downstream neighborhoods.
- `impact` follows evidence backlinks and the impact direction in the semantics
  table.

Results contain each node once, with its shortest discovered depth, and retain
the explicit edge and `REL` IDs that reached it. Additional paths to a repeated
node are recorded as alternate paths rather than expanding that node again.
Results must identify review state, classification, deprecated state, and
unresolved `contradicts` edges.

The depth ceiling is an operational safety boundary, not a statement that
objects beyond it are unaffected. A result that reaches the requested ceiling
must report that traversal was truncated.

## Cycle policy

Cycles are classified rather than uniformly rejected:

- a directed cycle composed only of `depends_on` edges is structurally invalid;
- any cycle containing `supersedes` is structurally invalid;
- all self-relations are structurally invalid;
- cycles involving symmetric `contradicts` or `relates_to` semantics, or other
  reviewed conceptual links, are permitted and reported;
- revisiting a node through a second valid path is a repeated path, not by
  itself a cycle error.

Traversal uses a visited-node set and an active-path set. It emits a cycle
notice for permitted cycles, records the participating IDs, and does not expand
the repeated node again. A structural cycle is a validation error and causes a
non-zero validator exit.

## Missing, rejected, deprecated, and superseded objects

- An unknown or missing relationship endpoint is a dangling reference and a
  validation error.
- An unknown or missing evidence reference is a validation error.
- An active relationship whose endpoint is `rejected` is a validation error.
- A deprecated endpoint remains resolvable and is returned with a warning. The
  warning is suppressed for the target of a valid `supersedes` relationship,
  where deprecation is required.
- A deprecated relationship is excluded from active traversal but remains
  visible in audit traversal.
- Supersession is recognized only through an explicit canonical `supersedes`
  relationship. Filenames, dates, or similar wording do not imply it.
- A missing node ends that path and makes the impact chain unresolved; the
  validator must not claim that no downstream impact exists.

Traversal never edits an affected object, changes its review state, or follows
an inferred replacement. Automated stale-state changes, invalidation, and
regeneration remain Stage 16 work.

## Conflict visibility

`contradicts` records remain ordinary canonical relationship records with
evidence and review metadata. Traversal output must label them as unresolved
conflicts unless a separate approved decision explicitly resolves the conflict.
Neither path order, review date, approval state, nor `supersedes` silently
chooses a winning claim.

Conflicting paths may coexist in one result. The validator reports them but
does not collapse, rank, or rewrite them.

## Integrity behavior

The Stage 11 validator will fail with a non-zero exit for:

- duplicate stable IDs;
- unknown relationship types;
- prohibited endpoint types or type pairings;
- dangling source or target endpoints;
- prohibited self-relations;
- invalid review states or missing required reviewer metadata;
- missing evidence references;
- active relationships to rejected objects;
- structurally invalid cycles; and
- impact paths that reference an object that cannot resolve to a canonical
  record.

It will emit non-failing warnings for deprecated endpoints where allowed,
permitted conceptual cycles, and semantic duplicate edges requiring review.
Warnings remain visible in machine-readable and human-readable output.

## Operational interface

Stage 11 should provide one repository validator/traversal command with:

- whole-repository integrity validation when no start ID is supplied;
- `--start-id` for a canonical object;
- `--direction upstream|downstream|both|impact`;
- `--max-depth` within the controlled range;
- an explicit option to include non-authoritative records for audit; and
- deterministic human-readable output, with optional structured output for
  later consumers.

The command is read-only. It must not generate or update canonical records.
Synthetic fixtures belong under `tests/` or temporary test directories and
must not be added to production knowledge directories.

## Rationale

An explicit-reference projection preserves repository authority and makes
impact queries reproducible. Separate stored and impact directions prevent a
`depends_on` edge from producing the wrong downstream result. Bounded traversal
and explicit cycle handling prevent runaway expansion without treating all
conceptual cycles as corruption. Keeping deprecated and conflicting records
visible preserves auditability.

## Alternatives considered

### Persist a separate graph database as the source of truth

Not selected because it would duplicate canonical claims, review states, and
provenance and create a synchronization problem.

### Infer links from titles, keywords, or embeddings

Not selected because similarity is not evidence of a governed relationship and
could introduce unsupported organizational claims.

### Treat every cycle as invalid

Not selected because symmetric conflicts and conceptual associations can
legitimately form cycles. Dependency and supersession cycles remain invalid.

### Traverse without a depth bound

Not selected because an accidental dense or cyclic graph could produce
uncontrolled work and ambiguous impact output.

## Consequences

### Positive

- Impact results remain reproducible from explicit canonical references.
- Relationship direction and cycle behavior are reviewable before code exists.
- Conflicts and deprecated history remain visible.
- Stage 16 can later consume the same explicit impact boundary without Stage 11
  mutating records.

### Negative

- Unrecorded real-world relationships remain unknown.
- Reviewers must choose precise relationship types and directions.
- The conservative impact policy can identify records that ultimately need no
  substantive revision.
- The depth ceiling can truncate a valid long chain and therefore must be
  reported.

### Risks

- A broadly used `relates_to` edge could reduce semantic precision.
- Incorrect relationship direction could produce incomplete impact results.
- Users may mistake derived traversal output for an approved conclusion.
- Current schemas do not yet enforce all type-pair, self-edge, lifecycle, cycle,
  and warning rules in this proposal.

## Implementation implications

After approval, Stage 11 may update the relationship schema and controlled
configuration where necessary, implement a relationship/impact validator,
add synthetic tests and CI execution, update architecture and operations
documentation, and create the Stage 11 status and human-review package.

No production relationship is required merely to test traversal. Stage 11 must
use synthetic fixtures and must not alter Stage 10 reviewed records. The
roadmap remains `planned` and Stage 11 remains blocked until approval is
recorded on this ADR.

## Validation of the proposal

Before review, validate prompt metadata, roadmap consistency, repository YAML,
schemas, knowledge, source processing, tests, links, and the Git diff. These
checks can establish that the proposal integrates cleanly; they cannot approve
its semantics.

## Approval requested

The authorized reviewer must explicitly accept, revise, or reject:

1. the canonical-versus-derived boundary and in-memory projection;
2. relationship directions, type constraints, and impact directions;
3. reviewed/audit traversal eligibility;
4. the default depth of 1 and maximum depth of 25;
5. structural versus permitted cycle behavior;
6. repeated-node and alternate-path handling;
7. missing, rejected, deprecated, and superseded-object behavior;
8. conflict visibility and non-resolution rules;
9. validator error versus warning behavior; and
10. the read-only operational interface and Stage 16 boundary.

MZ accepted all ten decisions above on 2026-08-14. Stage 11 implementation and
its exit-gate review remain separate human-review decisions.

## References

- [Approved roadmap](../roadmap.yaml)
- [Human-readable roadmap](../roadmap/implementation-roadmap.md)
- [Stage 10 status](../status/stage-10-reviewed-evidence-knowledge-pilot.md)
- [Knowledge management policy](../knowledge-management-policy.md)
- [Knowledge review workflow](../knowledge-review-workflow.md)
- [Relationship schema](../../schemas/relationship.schema.yaml)
- [Relationship directory contract](../../knowledge/relationships/README.md)
- [Knowledge type configuration](../../config/knowledge-types.yaml)
- [Stable identifier decision](ADR-0005-stable-identifiers.md)
- [Evidence/knowledge boundary](ADR-0006-separate-evidence-and-knowledge.md)
- [Human-review boundary](ADR-0007-human-review-for-authority.md)
