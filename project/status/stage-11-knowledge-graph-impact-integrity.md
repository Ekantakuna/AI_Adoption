# Stage 11 knowledge graph and impact integrity status

## Objective and status

Establish controlled relationship traversal and impact references for reviewed
knowledge without replacing canonical evidence, knowledge, or relationship
records with graph derivatives.

- Stage ID: `stage-11`
- Implementation status: implemented and closed
- Capability status: partial
- Implementation date: 2026-08-14
- Closure date: 2026-08-14
- Stage prompt: `PRM-CODEX-STAGE-011` version `1.0.0`
- Source access: repository-only; no external source or private extraction body
  was opened
- Human exit-gate review: approved by MZ on 2026-08-14

The required implementation is present, validates, and has authorized human
exit-gate approval. MZ authorized the roadmap transition on 2026-08-14;
`ROADMAP-000001` now records Stage 11 as `implemented` with capability
`partial`.

## Entry-gate evidence

| Criterion | Result | Repository evidence |
| --- | --- | --- |
| Stage 10 pilot review is closed | satisfied | `project/status/stage-10-reviewed-evidence-knowledge-pilot.md`, `project/status/stage-10-pilot-review-packet.md` |
| Relationship identifier contract is approved | satisfied | `project/status/stage-09-approval.md`, `config/knowledge-types.yaml`, `schemas/relationship.schema.yaml`, accepted `ADR-0005` |
| Traversal contract is approved | satisfied | MZ accepted `project/decisions/ADR-0011-explicit-relationship-traversal-contract.md` on 2026-08-14 |

The working tree was clean before Stage 11 prompt generation. The branch,
`main`, and refreshed `origin/main` all resolved to commit `361d254` at the
readiness check. Existing schema, source-processing, knowledge, roadmap, prompt,
and test validation passed before implementation.

## Implementation

- `config/relationship-types.yaml` is the controlled executable mapping for
  relationship direction, impact direction, endpoint constraints, cycle
  policy, reviewed/audit views, and depth limits.
- `scripts/validate_relationship_impact.py` loads canonical knowledge records,
  validates relationships and evidence backlinks, and creates a read-only
  in-memory projection for bounded traversal.
- `tests/test_relationship_impact_validation.py` contains only temporary
  synthetic fixtures and does not add fake production records.
- `docs/operations/traversing-knowledge-relationships.md` documents validation,
  query operation, outputs, lifecycle, and limitations.
- Architecture, concept, directory, repository-map, schema, test, script,
  configuration, project, prompt-library, and changelog documentation was
  synchronized with the in-review implementation.

No production `REL` record, graph database, persistent graph export, assessment
contract, or automatic invalidation behavior was created.

## Relationship model

Canonical `REL-NNNNNN` records remain evidence-backed knowledge objects with
stable IDs and approved knowledge review states. The executable relationship
types remain `supports`, `contradicts`, `refines`, `depends_on`, `influences`,
`measures`, `mitigates`, `relates_to`, and `supersedes`.

ADR-0011 and `config/relationship-types.yaml` define stored direction, impact
direction, subject/object constraints, same-type supersession, deprecated target
requirements, and cycle policy. Every relationship requires evidence and two
existing non-evidence, non-relationship endpoints. Similar words never create
an edge.

AI-origin relationships start as `draft` or `needs_review`. Human reviewer
metadata remains mandatory for `verified` and `approved`. Rejected and
deprecated records retain stable IDs; they are not silently deleted or reused.

## Traversal and impact model

The projection is derived on every command invocation from:

1. canonical `evidence_ids` backlinks; and
2. canonical relationship endpoints and controlled semantics.

Queries support `upstream`, `downstream`, `both`, and relationship-specific
`impact` direction. Default depth is 1 and the approved hard limit is 25.
Nodes are emitted once at their shortest depth; alternate paths remain listed.
Depth truncation reports that further impact is unknown.

The default view includes reviewed records. `--include-unreviewed` enables an
explicit audit view. Deprecated nodes remain historically addressable and are
labelled; rejected records do not enter the active view. Traversal never edits
canonical objects or changes review state.

An actual repository query from `EVID-000002` in impact direction resolves
`USECASE-000001` at depth 1 through its explicit `evidence_ids` reference. This
demonstrates the success measure without inventing a relationship.

## Cycle and conflict behavior

- Self-relations are errors.
- `depends_on`-only cycles and every cycle containing `supersedes` are errors.
- Reviewed conceptual and symmetric cycles are warnings and remain visible.
- Repeated paths do not expand a visited node again and are reported separately.
- `contradicts` edges remain unresolved conflicts in traversal output.
- Order, review date, or approval state never selects a winning claim.

## Integrity behavior

The validator returns a non-zero exit for duplicate IDs, unknown relationship
types, prohibited endpoint types/pairings, dangling endpoints, self-relations,
invalid review states, missing reviewer metadata, missing evidence, active
relationships to rejected objects, structural cycles, and unresolved canonical
impact references.

Allowed deprecated endpoints, permitted conceptual cycles, and semantic
duplicate edges are warnings. Warnings remain visible rather than being
automatically repaired.

## Synthetic tests

Twenty-nine isolated Stage 11 tests cover:

- valid one-hop and multi-hop traversal;
- dangling source and dangling target;
- unknown relationship type and duplicate relationship ID;
- missing evidence;
- invalid dependency and supersession cycles and permitted conceptual cycles;
- valid deprecated supersession;
- upstream-object impact direction;
- repeated-node and alternate-path behavior;
- prohibited self-relations, invalid review states, and reviewed relationships
  with non-reviewed endpoints;
- missing reviewer metadata, prohibited endpoint-type pairings, and active
  relationships to rejected endpoints;
- semantic-duplicate and deprecated-endpoint warning behavior;
- explicit conflict output and human-readable alternate/cycle/conflict sections;
- reviewed-versus-audit filtering, depth truncation and hard-limit behavior,
  and upstream/both directions;
- direct `refines`, `influences`, `measures`, and `mitigates` impact directions
  plus `measures`/`mitigates` endpoint constraints;
- the rule that `REL` records are edge records rather than traversal nodes; and
- a complete before/after snapshot of every synthetic canonical file and
  directory across validation, all traversal modes, and JSON CLI rendering,
  with no graph-store write.

## Canonical boundary and ADR impact

Canonical evidence, knowledge, and `REL` records remain authoritative. The
in-memory projection, traversal paths, warnings, cycle notices, and affected-ID
sets are replaceable derivatives. Stage 11 introduces no second source of
truth.

ADR-0011 is the material decision for Stage 11. MZ accepted its complete
direction, depth, lifecycle, cycle, conflict, warning/error, and canonical-data
contract before implementation. No additional ADR is proposed.

## Validation results

Post-implementation validation passed:

- YAML parsing: 70 files;
- Draft 2020-12 schema validation: 15 schemas, 61 sources, 60 processing
  authorizations, four runs, and 12 production knowledge records;
- source-processing validation: four evidence-eligible runs;
- knowledge validation: 12 records, nine evidence records, and two preserved
  provisional files;
- relationship/impact validation: 12 canonical records, zero production
  relationships, zero errors, and zero warnings;
- prompt validation: 21 prompt files and 14 catalogue entries;
- roadmap validation;
- automated tests: 87 passed, including 29 Stage 11 synthetic tests;
- actual impact query: `EVID-000002` resolved `USECASE-000001` at depth 1;
- offline Markdown links: 187 checked with zero errors; and
- `git diff --check`.

A documentation builder is not configured and is not reported as passing.
Relationship/impact validation is configured as a CI step and passes locally;
hosted CI was not run from this uncommitted worktree.

## Limitations and unresolved issues

- There are no production `REL` records, so relationship-edge behavior is
  demonstrated synthetically; direct evidence impact is demonstrable on current
  canonical records.
- The validator identifies potentially affected objects but does not establish
  that their content is stale or needs substantive revision.
- Classification is reported but the query does not implement a user-specific
  authorization engine.
- A depth limit can truncate a legitimate long chain and therefore reports
  unknown impact beyond the boundary.
- Stage 11 does not detect changes to source or canonical records, persist
  impact or invalidation records, automatically change stale or review states,
  enforce human re-review, perform controlled regeneration, or select between
  changed and unchanged processing paths. Those capabilities remain Stage 16
  work.
- Stage 11 alone does not satisfy the Stage 16 entry gate. Stage 16 also
  requires completed prerequisites from Stages 14 and 15 and approved
  change-policy and storage-route controls.
- Assessments and outlook contracts remain Stage 12 work.
- A Stage 11 synchronization is proposed for the approved Stage 9 knowledge
  review workflow. The revised governance text requires authorized human review
  before it inherits approved status.
- A documentation builder is not configured.

No unresolved relationship conflict exists in production because no production
relationship record exists. This is not evidence that the wider knowledge
corpus has no semantic conflicts.

## Exit-gate assessment

| Exit gate | State | Evidence |
| --- | --- | --- |
| Dangling-reference behavior documented and validated | satisfied and approved | ADR-0011, operations documentation, validator, dangling source/target tests; approved by MZ on 2026-08-14 |
| Cyclic behavior documented and validated | satisfied and approved | ADR-0011 cycle policy, validator, structural/conceptual cycle tests; approved by MZ on 2026-08-14 |
| Canonical knowledge boundaries remain intact | satisfied and approved | in-memory implementation and non-mutation synthetic test; approved by MZ on 2026-08-14 |
| Human review is recorded | satisfied | MZ approved the Stage 11 exit-gate assessment on 2026-08-14 |

Success measure: affected downstream objects can be identified from explicit
references while unresolved conflicts remain visible. This is demonstrated by
the repository `EVID-000002` → `USECASE-000001` query and synthetic relationship
and conflict tests. Human acceptance of that implementation claim was recorded
through MZ's 2026-08-14 exit-gate approval.

## Stage 12 readiness

Stage 11's prerequisite contribution to Stage 12 is satisfied. Stage 12 is not
otherwise ready because it independently requires approved scoring and audience
controls, which Stage 11 did not create or approve.

## Human review

### Decisions recorded

- On 2026-08-14, MZ reviewed `config/relationship-types.yaml` against accepted
  ADR-0011 and approved the executable mapping as faithful to the relationship
  directions, impact directions, endpoint constraints, depth limits,
  reviewed/audit states, and cycle policies.
- On 2026-08-14, MZ reviewed and approved the validator error and warning
  behavior, including errors for reviewed relationships with non-reviewed or
  rejected endpoints and visible warnings for semantic duplicates, permitted
  conceptual cycles, and allowed deprecated endpoints.
- On 2026-08-14, MZ reviewed and approved traversal output behavior, including
  direction handling, bounded depth and truncation, reviewed/audit filtering,
  repeated-node handling, cycle reporting, deprecated-object warnings, and
  explicit unresolved-conflict output.
- On 2026-08-14, MZ reviewed and approved the synthetic-test coverage and
  canonical non-mutation boundary, including complete synthetic repository
  snapshot comparison, all traversal modes, JSON rendering, all relationship
  semantics, and confirmation that traversal writes no graph store or canonical
  record.
- On 2026-08-14, MZ reviewed and approved the documented Stage 11 limitations
  and Stage 16 boundary, including the absence of change detection, persistent
  impact or invalidation records, automatic state transitions, human re-review
  enforcement, controlled regeneration, and changed-path selection. MZ also
  accepted that Stage 11 alone does not make Stage 16 ready because Stages 14
  and 15 and approved change-policy and storage-route controls remain required.
- On 2026-08-14, MZ reviewed and approved the Stage 11 exit-gate assessment,
  including dangling-reference behavior, cyclic behavior, preservation of
  canonical knowledge boundaries, the recorded human-review gate, and the
  demonstrated success measure for explicit-reference impact with visible
  unresolved conflicts.
- On 2026-08-14, MZ authorized the roadmap transition to `status: implemented`
  with capability `partial`.
- On 2026-08-14, MZ authorized preparation of the separate Stage 9 knowledge
  review workflow synchronization and addition of relationship/impact
  validation to CI. The CI step is implemented.
- On 2026-08-15, MZ reviewed and approved the Stage 11 synchronization of the
  Stage 9 knowledge review workflow, including bounded explicit-reference
  impact traversal and its manual-review and non-automation boundaries.

### Remaining Stage 11 decisions

No Stage 11 implementation, exit-gate, roadmap-transition, workflow, or CI
decision remains pending. Hosted CI has not yet run against the uncommitted
change set; that operational fact does not reopen Stage 11.
