# Decision environment semantic layer

This area explains reusable relationships between decision-environment records. Canonical facts and lifecycle records remain in YAML registers.

```text
decision-intelligence target
  -> decision type
  -> decision context + business semantics
  -> choice architecture + authority rules + controls
  -> actual decision
       -> options
       -> evidence | prediction | forecast | scenario | simulation
       -> human authorization, override or escalation
       -> execution
  -> observed outcome + metrics + risks
  -> reviewed learning event
  -> controlled change to semantics, architecture, models, controls or measures
```

The domain references shared glossary terms, stakeholders, solutions, capabilities, risks, controls, metrics, dependencies and initiatives. It does not duplicate their canonical records.
