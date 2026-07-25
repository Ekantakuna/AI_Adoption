# Sources

This directory contains source metadata, manifests, source notes, and controlled extraction areas; classification review is required before processing source documents.

The canonical source inventory is `sources/catalogue.yaml`. `../registers/sources.yaml` is retained only as a legacy compatibility snapshot.

The `extracted/private/` path is excluded from Git. Other extracted artifacts are not automatically excluded; they may be tracked only after classification and information-handling review confirms that repository storage is permitted.

## Source-access boundary

The original evidence remains outside Git under the approved local source root recorded in `config/source-types.yaml`. This directory may contain only approved metadata, manifests, notes, hashes, summaries, and normalized derivatives that comply with `project/source-management-policy.md`.

Manifest conventions are documented in `manifests/README.md`, while controlled source-root values, states, ignored patterns, and file-type controls are defined in `config/source-types.yaml`.
