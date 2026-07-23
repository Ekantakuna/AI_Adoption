# Scripts

This directory contains utilities for controlled ingestion, validation, reporting, and publication workflows.

## Metadata inventory

`inventory/build_source_inventory.rb` emits the canonical source-register YAML from names, relative paths, extensions, sizes, modification timestamps and symbolic-link metadata only. It does not open source files or calculate hashes. It preserves existing source IDs, refuses to follow symbolic links and stops when an existing catalogue path disappears or a custody mapping is missing.

The generated output must be reviewed before it replaces `registers/sources.yaml`. Running the utility does not authorize content extraction.
