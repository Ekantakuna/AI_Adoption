# Sources

This directory contains source metadata, manifests, source notes, and controlled extraction areas; classification review is required before processing source documents.

The canonical source inventory is `../registers/sources.yaml`. `catalogue.yaml` points to that register and is not an independent source-record store.

The `extracted/private/` path is excluded from Git. Other extracted artifacts are not automatically excluded; they may be tracked only after classification and information-handling review confirms that repository storage is permitted.

## Source-access boundary

The original evidence remains under the local source root recorded in `config/source-types.yaml`. Original source documents must not be copied into this repository. This directory may contain only approved metadata, hashes, manifests, extraction records, summaries, and normalized derivatives that comply with `project/source-management-policy.md`.

Original evidence and repository derivatives are different custody layers:

- original evidence remains in its existing local folder with its filename and path preserved in the catalogue;
- repository derivatives contain traceable information produced through an approved processing route and link back to stable source IDs.

Document-content analysis has not started. A source may not be opened for analysis until its classification, processing route, stable ID, and extraction tool are approved.

## Source inventory

`registers/sources.yaml` remains the canonical source inventory. Manifest conventions are documented in `manifests/README.md`, while controlled formats, states, ignored patterns, and domain prefixes are defined in `config/source-types.yaml`.
