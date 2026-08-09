---
id: PRM-CODEX-PLAN-GEN
title: Generate one stage prompt from the approved roadmap
type: planning
version: 1.0.0
status: active
owner_role: roadmap-maintainer
created_at: 2026-08-05
updated_at: 2026-08-05
roadmap_stage: post-09.5
source_access: repository_only
allowed_paths: [AGENTS.md, project/roadmap.yaml, project/roadmap/implementation-roadmap.md, project/status, prompts/codex/stages]
prohibited_actions: [commit, push, source_body_access, execute_generated_prompt, invent_requirements]
required_inputs: [requested_stage_id, approved_roadmap]
expected_outputs: [one_matching_stage_prompt]
validation: [roadmap_id_check, prompt_metadata_validation, git_diff_check]
human_review: required
supersedes: null
superseded_by: null
---

# Generate a stage prompt from the roadmap

1. Read `AGENTS.md`.
2. Read `project/roadmap.yaml` and
   `project/roadmap/implementation-roadmap.md`.
3. Receive a requested stage ID and verify that it exists and the roadmap is
   approved for prompt generation.
4. Create only the matching stage prompt under `prompts/codex/stages/`.
5. Copy all roadmap requirements faithfully, including entry checks, scope,
   outputs, documentation, validation, human review, and exit gates.

Do not execute the generated stage, invent conflicting requirements, generate
Stages 10–31 in advance, inspect source bodies, or commit/push. Validate the
new prompt metadata and report the requested ID, roadmap evidence, output path,
validation, and unresolved issues.
