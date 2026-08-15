# Tests

`test_prompt_validation.py` covers prompt metadata, catalogue membership,
template status, and deprecation replacement checks.

This directory contains `unittest` coverage for the Stage 9 schema and knowledge
validators and remains the home for future repository checks. Install
`requirements-validation.txt`, then run all tests from the repository root:

```text
python -m unittest discover -s tests -p "test_*.py"
```

`test_knowledge_validation.py` uses isolated temporary repositories and covers
the empty framework, catalogue `records` compatibility, valid evidence,
referential integrity, duplicate, malformed, and reserved IDs, statuses,
reviewer gates, unsupported types, template exclusion, malformed non-string
references and controlled values, and the boundary between root-level legacy
notes and unstructured object-directory content.
It also confirms that the command returns zero on success and non-zero on
validation failure.

`test_schema_validation.py` covers valid Draft 2020-12 schemas and records,
meta-schema failures, source-catalogue failures, production knowledge-record
failures, governed Stage 12 entry-control configuration success/failure and
missing-schema behavior, configured reference-schema enforcement, template
exclusion, and command exit codes. Its fixtures contain no project source data.

`test_source_processing_validation.py` covers the empty registers, catalogue
authorization gate, human reviewer identity, classification and tool matching,
restricted environment, run hash/provenance, local derivative hash
verification, and evidence-eligible review.
`test_extract_text.py` covers text normalization, HTML script/style exclusion,
raw source hashing, output-boundary enforcement, and rejection of an unsupported
format. These tests use synthetic temporary fixtures and do not open repository
or external source bodies.

`test_extract_pptx_text.py` uses synthetic ZIP/XML fixtures to verify numeric
slide ordering, text extraction, and rejection of packages without slide XML.
It contains no project source data.

`test_roadmap_validation.py` covers the machine/human roadmap cross-check and
rejects duplicate stage IDs, missing references, dependency cycles, and heading
mismatches using temporary synthetic repositories.

`test_relationship_impact_validation.py` uses isolated synthetic knowledge
records to cover one-hop and multi-hop traversal, dangling endpoints, unknown
types, duplicate IDs, missing evidence, structural and conceptual cycles,
deprecated supersession, impact direction, repeated nodes, self-relations,
invalid review states, reviewed-to-unreviewed endpoint rejection, the
relationship-edge boundary, missing reviewer metadata, prohibited type
pairings, rejected endpoints, duplicate/deprecated warnings, and preservation
of canonical files. It also checks conflict output, human-readable
alternate/cycle/conflict sections, reviewed/audit filtering, depth truncation
and limits, upstream/both traversal, and direct semantics for `refines`,
`influences`, `measures`, and `mitigates`. Its non-mutation test compares every
synthetic canonical path and byte before and after validation, all traversal
modes, and JSON rendering. It creates no production relationship records or
graph store.

Fixtures must not contain production or sensitive source data. Test
documentation must identify the command, covered contract, expected inputs and
outputs, and limitations.
