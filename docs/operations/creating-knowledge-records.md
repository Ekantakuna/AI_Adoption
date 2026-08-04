# Creating knowledge records

1. Confirm classification, Git eligibility, and the approved upstream route.
2. Select the object type in `config/knowledge-types.yaml` and copy its local
   template to a production filename.
3. Allocate the next unused six-digit ID without renumbering or reusing an ID.
   Replace every `000000` placeholder and remove `template: true`.
4. Populate the applicable schema fields. For evidence, cite a catalogue
   source, exact locator, and processing run. For knowledge, cite existing
   evidence. For a relationship, cite existing knowledge endpoints and
   evidence.
5. Set inherited classification, `origin`, creator, date, and `draft` or
   `needs_review` for AI-created content. Do not add reviewer approval yourself.
6. Run `python scripts/validate_schemas.py` and
   `python scripts/validate_knowledge.py`, inspect errors, and submit the record
   through `project/knowledge-review-workflow.md`.

The validator accepts empty production directories and ignores READMEs and
templates. It treats the two preserved root-level Markdown notes without front
matter as legacy/provisional; unstructured Markdown inside an object directory
is an error. It does not authorize source access or confirm semantic
correctness.
