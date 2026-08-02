# Source processing control policy

> Approved by Maksim Zakharenkau on 2026-08-02. Approval is recorded in
> `project/status/source-processing-approval.md`.

## Purpose

This policy controls the transition from canonical source metadata to an
authorized processing run. It does not authorize any source by itself and does
not make extraction output evidence.

## Authorization gate

Before a source body is opened, the canonical catalogue must contain a human-
approved classification and a non-blocked processing state. An approved record
in `sources/processing-authorizations.yaml` must bind that source ID and
classification to one controlled route, extraction tool, execution
environment, reviewer, review date, and evidence basis.

Each configured extraction tool also carries an approval state. An approved
authorization cannot reference a proposed or deprecated tool. Adding a tool or
expanding its source types, extensions, or routes requires human review before
body access.

Restricted sources require `local_only` and `approved_on_prem`. Public sources
may use `external_processing_approved`, but an authorization for a local tool
does not authorize substitution of an external service. Internal sources use a
local route unless a later reviewed policy adds another route.

## Run gate

Each processing execution receives a stable `RUN-NNNNNN` record in
`sources/processing-runs.yaml`. The run preserves the authorization ID, source
ID and hash, classification, route, tool and exact version, environment,
operator, timestamps, outcome, derivative reference and hash, and review state.

Only a `succeeded` run with `verified` or `approved` review status may support a
production `EVID` record. Extraction derivatives inherit source classification
and may be stored in Git only when the approved route permits it.

## Lifecycle and ownership

Authorization IDs and run IDs are never reused. Revocation preserves the
authorization record. Failed and blocked runs remain for audit. Repository
maintainers own the contracts and validators; Maksim Zakharenkau is the current
review owner for source classifications, routes, tools, and environments.

## Operation

Run `python scripts/validate_schemas.py`,
`python scripts/validate_source_processing.py`, and
`python scripts/validate_knowledge.py` after any authorization, run, or evidence
change. Validation does not inspect source bodies or establish semantic truth.

## Limitations

The initial contracts do not execute extraction, verify whether a machine is an
approved on-premises environment, validate external service accounts, or
reconcile historical extracted-file claims. The Pages source remains blocked.
