# Source processing templates

This directory contains non-production templates for source-processing
authorizations and runs. `AUTH-000000` and `RUN-000000` are reserved
placeholders and must never be used as production IDs.

An authorization records the human-approved source classification, route,
tool, and environment. A run records one execution against the source hash and
authorization. Templates contain no source content and are ignored by
production record counts.
