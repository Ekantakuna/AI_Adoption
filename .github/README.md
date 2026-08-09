# GitHub configuration

This directory contains the Stage 9 validation workflow and remains scaffolded
for issue templates and pull-request support. `.github/workflows/validate.yml`
runs Draft 2020-12 schema/source-catalogue validation, the cross-record
source-processing, knowledge, and Codex prompt-library validators, and the
`unittest` suite on pushes and pull requests. It does not build documentation
or validate Markdown links.
