# Stage template

Use this structure for a future roadmap stage. Replace every placeholder with
repository-supported content and keep the stage ID stable after publication.

```yaml
- id: stage-N
  sequence: N
  title: <short title>
  status: planned
  capability_status: planned
  summary: <bounded objective>
  prerequisites: []
  entry_criteria: []
  deliverables: []
  validation: [yaml_parse, tests, git_diff_check]
  exit_gates: []
  success_measures: []
  dependencies: []
  downstream_prompt: null
```

Each stage must explain what it is and why it exists, inputs and outputs,
identifier/lifecycle behavior, relationships, validation, ownership/review,
operational procedure, and limitations in its human-readable section. Do not add
dates, budgets, headcount, or unsupported estimates. A stage prompt is generated
only after roadmap approval and must retain these fields and the source-access
boundary.
