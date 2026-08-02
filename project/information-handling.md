# AI Adoption information-handling rules

These rules govern source assets and every derivative. Amendments made by an AI
agent remain review proposals until an authorized human reviewer accepts them.

## Public

May be processed by approved local and cloud tools.

## Internal

May be processed only by company-approved tools and accounts.

## Restricted

Must remain in approved on-premises environments.

## Unclassified

May be inventoried as metadata but its body must not be opened or processed.
Classification and a handling route require human review.

## Storage boundary

Original source assets remain in the approved source root outside Git. Source
metadata is distinct from source content: filenames, paths, sizes, hashes, and
administrative states may be inventoried without reading the body, but metadata
access does not authorize content access.

Git may contain metadata and derivatives only when their classification and
approved route permit repository storage. Restricted or otherwise non-trackable
derivatives remain local-only. Generated content inherits the highest
classification of its inputs. `.gitignore` is an accidental-disclosure control,
not permission to store or process information.

## Evidence protection

- Do not modify, rename, move, delete, or overwrite original source assets
  during repository processing.
- Do not silently replace evidence, provenance, source locators, stable IDs, or
  conflicting source statements.
- Extraction output remains a derivative; it is not authoritative evidence or
  approved knowledge merely because it exists.
- Keep each derived claim traceable to stable source and evidence identifiers
  where the applicable object model exists.

## Human review boundary

Only an authorized human reviewer may approve classifications, processing
routes, extraction tools, authoritative evidence or knowledge, current-state
conclusions, target commitments, organizational recommendations, and
publication-ready executive claims. AI agents may prepare clearly labelled
drafts and review proposals within an approved route; they cannot approve their
own outputs.

## Repository rules

- No credentials or API keys in Git.
- No personal information unless explicitly approved.
- No production datasets in the strategy repository.
- No source document is uploaded to an external model without classification review.

Operational source states and the content-access gate are defined in
[source management policy](source-management-policy.md). Approved per-source
authorization and run provenance controls are defined in
[source processing control policy](source-processing-control-policy.md).
Repository object
definitions are in
[information objects](../docs/concepts/information-objects.md).
