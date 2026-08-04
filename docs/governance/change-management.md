# Change management

## Purpose

Repository changes must preserve provenance, stable identities, review state,
and the difference between canonical and generated data. This applies to source
updates, schema changes, operating changes, and generated outputs.

## Standard change lifecycle

1. **Scope**: state the requested outcome, affected objects, and information
   boundary.
2. **Inspect**: read relevant implementation, documentation, schemas,
   configuration, tests, status, branch, and diff.
3. **Classify**: separate observed facts, assumptions, inferences,
   recommendations, and unresolved conflicts.
4. **Decide**: record a material architectural choice as an ADR. An AI-authored
   ADR remains proposed until human review.
5. **Implement**: change only in-scope canonical content and automation.
6. **Document**: update authoritative documentation and `CHANGELOG.md`.
7. **Record status**: update the applicable file under `project/status/`.
8. **Validate**: run all available relevant checks.
9. **Review**: inspect the diff, obtain required human approvals, then merge
   through the authorized Git workflow.

## Source and evidence changes

Original evidence is immutable during repository processing. A moved or changed
asset does not receive a new ID automatically. First establish whether it is the
same source, a new version, a duplicate, or a distinct source; preserve path and
hash history and represent uncertainty explicitly.

Before body access, classification, stable source ID, processing route, and
extraction tool must be approved. A changed source can invalidate downstream
evidence even when its filename is unchanged.

## Planned incremental impact procedure

Automated incremental processing is absent. Until dependency relationships and
an invalidation engine exist, use a manual review:

1. compare authoritative source metadata and hashes;
2. list direct downstream references from evidence or knowledge records;
3. list assessments, reports, and presentations that cite those records;
4. mark affected objects for review without deleting prior states;
5. reprocess through the approved route;
6. record supersession or conflict relationships;
7. regenerate only replaceable derivatives after approval;
8. validate the complete provenance chain.

Where downstream references are unavailable, record impact as **unknown**. Do
not infer that no reference means no impact.

## Schema and controlled-value changes

A schema or controlled-value change must document migration and compatibility,
update producers and consumers, add validation and tests, preserve stable IDs,
and state how existing records are handled. Do not silently rewrite records to
fit a new vocabulary. Term conflicts require an explicit mapping or decision.

## Generated outputs

Generated files must be reproducible from identified canonical inputs when
automation is implemented. Rebuilding a derivative must not alter canonical
evidence, approvals, or IDs. Do not manually patch a generated file as the sole
fix; change its canonical input or generator.

## Git and rollback

Work on a branch, preserve unrelated changes, and do not commit or push without
explicit instruction. Prefer additive history and explicit supersession over
destructive rewrites. Rollback must restore canonical records and preserve the
audit trail; deleting evidence or rewriting Git history is not an acceptable
normal rollback.
