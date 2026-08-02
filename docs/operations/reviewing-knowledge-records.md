# Reviewing knowledge records

Reviewers first confirm they are authorized for the record classification and
decision boundary. Check that the stable ID and type match the directory, the
source/evidence references resolve, the locator permits fidelity checking, the
statement is atomic, interpretations do not masquerade as evidence, conflicts
remain explicit, and downstream uses match the requested authority.

Use `under_review` while checking. For accepted factual/evidence content, use
`verified`; for acceptance for the stated use, use `approved`. Both require:

```yaml
reviewer:
  name: "<authorized reviewer>"
  reviewed_at: "YYYY-MM-DD"
```

Reject or deprecate without reusing the ID. After any review outcome, run
`python scripts/validate_schemas.py` and
`python scripts/validate_knowledge.py`, then manually find downstream
references to the changed ID. Validation confirms structure and links, not
reviewer authority or content truth.
