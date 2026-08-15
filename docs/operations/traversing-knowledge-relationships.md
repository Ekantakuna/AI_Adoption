# Traversing knowledge relationships

## Purpose and boundary

`scripts/validate_relationship_impact.py` validates explicit relationship and
impact references and builds a read-only in-memory projection for queries. It
does not infer semantic relationships, approve records, write a graph store,
alter review states, or invalidate downstream content.

Canonical `EVID`, knowledge, and `REL` records remain authoritative. Traversal
output is a replaceable derivative. The governing directions, lifecycle,
cycles, depth, deprecated-object behavior, and conflict rules are in
[ADR-0011](../../project/decisions/ADR-0011-explicit-relationship-traversal-contract.md).

## Validation

From the repository root, run:

```text
python scripts/validate_relationship_impact.py
```

The command validates the controlled relationship-type configuration against
the relationship schema, stable IDs, review states, reviewer metadata,
evidence references, endpoints, type pairings, self-relations, semantic
duplicates, deprecated/rejected endpoints, and structural cycles. Errors return
a non-zero exit. Permitted conceptual cycles and allowed deprecated references
remain visible as warnings.

This check supplements rather than replaces schema and knowledge validation.

## Traversal

Supply one canonical start ID:

```text
python scripts/validate_relationship_impact.py --start-id EVID-000002 --direction impact --max-depth 2
```

Directions are:

- `upstream`: evidence and reverse explicit-reference paths;
- `downstream`: explicit consumers and stored relationship direction;
- `both`: the union of upstream and downstream;
- `impact`: evidence backlinks and ADR-0011's relationship-specific impact
  direction.

The default depth is 1. The approved maximum is 25; traversal is never
unbounded. A depth-limited result reports truncation rather than claiming no
further impact.

The default view includes `verified`, `approved`, and historically addressable
deprecated objects. Add `--include-unreviewed` only for an explicitly labelled
audit view containing draft/review/rejected records. Use `--format json` for
deterministic structured output.

Each node is emitted once at its shortest depth. Alternate paths, permitted
cycles, deprecated objects, unresolved conflicts, and truncation remain visible.
Missing canonical nodes are validation errors; traversal does not interpret a
broken path as proof that no impact exists.

Human-readable output labels these sections as `ALTERNATE`, `CYCLE`,
`CONFLICT`, and `WARNING`. JSON output exposes the corresponding
`alternate_paths`, `cycles`, `conflicts`, and `warnings` arrays.

## Lifecycle and limitations

Relationship creation and review continue through the approved knowledge
workflow. AI-origin `REL` records start as `draft` or `needs_review`, require
evidence, and need identified human review for `verified` or `approved` states.
Rejected and deprecated records remain addressable for audit and keep their
stable IDs.

The repository currently has no production `REL` records, so Stage 11 behavior
is demonstrated with temporary synthetic fixtures and existing direct
`evidence_ids` references. Stage 11 identifies potentially affected records
only. It does not implement:

- source or canonical-record change detection;
- persistent impact or invalidation records;
- automatic stale-state or review-state transitions;
- enforcement of human re-review for affected records;
- controlled regeneration of reviewed derivatives; or
- selection between changed and unchanged processing paths.

Those operating-automation capabilities remain Stage 16 work.

Stage 11 alone does not make Stage 16 ready: the approved roadmap also requires
Stages 14 and 15, plus approved change-policy and storage-route controls, before
Stage 16 can begin.
