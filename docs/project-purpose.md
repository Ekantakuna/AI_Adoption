# Project purpose

## Problem addressed

AI adoption work draws on source assets, interpretations, organizational
evidence, decisions, delivery records, and audience communications. Without
explicit boundaries, a summary can lose its provenance, a generated report can
be mistaken for a source of truth, and a changed source can leave downstream
content stale.

This repository is intended to make that work traceable and maintainable.

## Intended outcomes

The repository should support:

- an inventory of evidence sources without storing original source binaries in
  Git;
- controlled extraction under classification and handling rules;
- atomic evidence linked to stable source IDs;
- structured knowledge and explicit relationships;
- current-state, target-state, gap, maturity, outlook, and impact views;
- project decisions and progress management;
- reports and presentations tailored to authorized audiences;
- incremental reprocessing when source information changes.

These are target outcomes. The current tree implements metadata inventory and
some governance foundations, with downstream layers mostly partial, scaffolded,
or absent. See the [baseline](../project/status/repository-baseline.md).

## Quality attributes

Repository work should be:

- **traceable**: claims link to stable evidence and source identifiers;
- **reviewable**: draft, review, and approval boundaries are visible;
- **safe**: classification determines storage and processing routes;
- **maintainable**: canonical definitions are linked rather than duplicated;
- **reproducible**: automation records inputs and outputs when implemented;
- **incremental**: changed inputs affect only known downstream dependencies;
- **honest about status**: plans and scaffolds are not described as operations.

## Non-goals of the current operating-model stage

This stage does not analyze external source bodies, approve knowledge or
organizational conclusions, implement a knowledge graph, build reports or
presentations, or deliver an incremental processing engine. It documents the
boundaries and evidence-based starting point for those later stages.
