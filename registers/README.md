# Registers

This directory is the target location for canonical structured records for
project entities, controls, relationships, and delivery tracking.

Ten non-source registers currently contain only the common
`schema_version`/`register`/empty-`records` scaffold. They do not implement their
named object types, identifiers, lifecycles, relationships, or validation.
Records must not be added until an authorized object-specific schema defines
those contracts.

Source inventories are maintained canonically in `sources/catalogue.yaml`.
`registers/sources.yaml` is a non-authoritative legacy compatibility snapshot
whose fields and state values conflict with the catalogue. Preserve it for
review; do not update downstream work from its later states without an approved
reconciliation.

When a register becomes operational, its schema must define stable identifiers,
allowed transitions, provenance, relationships, review ownership,
supersession/retention, and validation. See
`docs/concepts/information-objects.md` and
`docs/reference/identifiers.md`.
