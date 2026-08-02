# Configuration

This directory contains project-wide controlled values and planned
configuration surfaces.

- `project.yaml` defines project metadata and general status, confidence, and
  classification value lists.
- `taxonomy.yaml` defines implemented domain IDs.
- `source-types.yaml` defines source-root metadata, source-specific
  classifications and processing states, file groups, ignored patterns, and
  source-ID prefixes.
- `knowledge-types.yaml` maps controlled knowledge types to prefixes,
  directories, formats, schemas, and evidence requirements.
- `evidence-confidence.yaml` defines evidence-support confidence values.
- `review-statuses.yaml` defines the knowledge review lifecycle, AI initial
  states, and reviewer-required states.
- `source-processing.yaml` defines the approved authorization and run
  statuses, execution environments, routes, and extraction tools used by the
  source-processing contracts. Per-source access still requires an approved
  authorization and planned run.
  Individual tools carry an approval state; proposed tools cannot support an
  approved authorization. `pptx_xml_reader` is currently proposed pending
  human review.
- `audiences.yaml` and `scoring_models.yaml` are empty placeholders; no audience
  or scoring configuration is implemented.

Configuration is canonical only for the values explicitly present. Empty files
do not define an object type or capability. The source-specific classification
list includes `unclassified`, while the general project list does not; this is
an explicit scope difference, not an automatic mapping.

Two catalogue-to-configuration mappings are undefined. The catalogue uses the
domain `glossary`, which is absent from `taxonomy.yaml`, and the source type
`image`, while `source-types.yaml` names the corresponding source group
`images`. Do not infer a mapping or change either controlled value without a
reviewed contract.

`source-types.yaml` currently contains both `ignored_files` and
`ignore_patterns`. The latter adds Aider history files and repeats the common
temporary-file patterns in the former. No tracked inventory script, schema, or
other consumer defines precedence or whether the lists are merged. Until that
contract exists, treat both as configuration data requiring manual review; do
not claim that either list is automatically enforced.

Changes require documentation, migration/compatibility analysis, and human
review where they affect policy or approved records. YAML syntax parsing is
available; schemas do not yet cover the configuration files themselves. The
knowledge and source-processing validators check the expected controlled
structures they consume.
