# Knowledge review statuses

| Status | Meaning | Reviewer required |
| --- | --- | --- |
| `draft` | Work is being prepared. | No |
| `needs_review` | Ready for authorized human review. | No |
| `under_review` | Review is in progress. | No |
| `verified` | Evidence or factual content was checked. | Yes |
| `approved` | Accepted for its stated use. | Yes |
| `rejected` | Declined but retained for audit. | No |
| `deprecated` | Retained and addressable but not for new use. | No |

AI-generated content may initially use only `draft` or `needs_review`. An
authorized human may later promote it while preserving `origin: ai`.
`verified` and `approved` require `reviewer.name` and `reviewer.reviewed_at` and
cannot be self-assigned by an AI agent. Status does not flow automatically:
approved evidence does not approve a knowledge interpretation, assessment,
report, or presentation. Controlled values are in
`config/review-statuses.yaml`.
