# Knowledge identifiers

Knowledge IDs use `<PREFIX>-NNNNNN`, with exactly six decimal digits. Prefixes
are controlled by `config/knowledge-types.yaml`: `EVID`, `TERM`, `CONCEPT`,
`FRAME`, `METRIC`, `RISK`, `TREND`, `USECASE`, `REL`, `ASSUMPTION`, `DECISION`,
and `REF`. IDs are globally unique across production knowledge, permanent, and
never renumbered or reassigned. `000000` is reserved for templates and cannot
identify production content.

Source IDs retain their separate `SRC-<GROUP>-NNNNNN` model. Stage 9 evidence
also records `RUN-NNNNNN`. The approved processing-run registry and lifecycle
are defined in `schemas/processing-run.schema.yaml` and
`sources/processing-runs.yaml`; the knowledge validator resolves evidence run
references and requires a successful reviewed run. The register is currently
empty.
