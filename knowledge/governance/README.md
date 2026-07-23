# Governance semantic layer

This area documents reusable governance concepts and relationships. Canonical facts live in YAML registers; this README explains how they form an analyzable knowledge model.

```text
governance target
  -> composed of capabilities
  -> realized through operating model, artifacts, roles, controls and tools

risk -> treated by controls and pathway actions
control -> implemented by roles, processes and tools -> produces evidence
assessment -> evaluates current or target state -> produces findings
finding -> compares current evidence with target characteristics
approved gap -> drives pathway action -> changes capability or control state
```

Terms and aliases belong in `registers/terms.yaml`. Governance records link to source IDs and evidence references rather than embedding unsupported source-derived claims. The model is provisional and may be refined after approved source analysis and collaboration on assumptions and direction.
