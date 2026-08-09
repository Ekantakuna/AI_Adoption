# Roadmap and stage lifecycle

## Roadmap lifecycle

`draft` is being assembled and is not ready for execution. `in_review` has been
submitted to an authorized human. `approved` permits controlled downstream stage
prompt generation. `superseded` retains an older roadmap for traceability after a
new approved roadmap replaces it. `retired` is retained but no longer active.

The roadmap owner may prepare or revise a draft. Only an authorized human may
record approval, reviewer identity, and review date. A revision that changes
stage scope, dependencies, identifiers, gates, or controlled values must update
the roadmap version and status and receive review again.

## Stage capability status

Each stage has both a roadmap lifecycle `status` and a capability status. The
capability values are `implemented`, `partial`, `planned`, `absent`, and
`unknown`. `implemented` means repository evidence demonstrates a usable
capability; `partial` means incomplete, manual, inconsistent, or unreproducible;
`planned` means intent or scaffolding without an operating implementation;
`absent` means no implementation evidence was found; and `unknown` means the
evidence is insufficient. These values must not be silently promoted because a
stage is listed in the roadmap.

## Stage progression

1. Inspect the current status, controls, schemas, tests, and Git state.
2. Confirm prerequisites and every entry criterion.
3. Execute only the approved stage scope under its source-access boundary.
4. Validate deliverables and record implemented, partial, planned, absent, and
   unknown capabilities with repository paths.
5. Obtain the required human review and record unresolved issues.
6. Close the stage only when every exit gate is evidenced; otherwise retain the
   stage as partial or in review.

Stages may depend on earlier stages only. A dependency cycle, missing reference,
or unapproved prompt-generation request is a release-blocking error. A stage
status document is required for each implemented stage and must distinguish
historical facts from planned work.
