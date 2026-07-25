# Public source analysis

## Scope

This note summarizes downstream analysis of the approved public source set from `sources/catalogue.yaml`.

- Public sources approved for downstream processing: 32
- Public sources successfully extracted with local text parsing: 31
- Public source kept blocked for follow-up: `SRC-VIS-000005` (`From AI Deployment to Intelligence Design.pages`)

The analysis uses local extracted text for the 31 PDF sources and metadata-only handling for the blocked Pages package.

## Facts

- The public corpus is dominated by AI-adoption, agentic-AI, governance, security, and use-case material.
- The public set includes a mix of:
  - academic preprints and conference papers;
  - vendor documentation and product-oriented technical guidance;
  - consulting or analyst-style reports;
  - applied business-use-case writeups.
- Several sources are exact duplicates or cross-domain reuse of the same underlying document:
  - `SRC-PRM-000002` duplicates `SRC-MIS-000001`
  - `SRC-ORG-000001` duplicates `SRC-PRM-000004`
  - `SRC-UC-000006` duplicates `SRC-UC-000004`
  - `SRC-UC-000007` duplicates `SRC-UC-000005`
  - `SRC-UC-000008` duplicates `SRC-VIS-000008`

## Inferences

- The corpus is not a single-topic library; it is a reusable evidence set for the project’s main narrative layers:
  - strategic intent and deployment patterns
  - agent design and context engineering
  - governance and risk controls
  - security and trust
  - business value and use-case framing
- The agentic-AI material suggests a progression from narrow task-oriented dialogue toward more compositional and self-improving agent systems.
- The governance and security material suggests the project should treat scale, trust, and misuse resistance as first-class design constraints rather than afterthoughts.
- The use-case material is repetitive across domains, which suggests the corpus is being used as thematic reinforcement rather than as mutually independent evidence.

## Theme map

| Theme | Representative source IDs | Observed emphasis |
| --- | --- | --- |
| Agentic AI and task-oriented systems | `SRC-AGT-000001` to `SRC-AGT-000007` | In-context learning, agent tuning, agent composition, context engineering, early-experience learning |
| Strategic intent and adoption framing | `SRC-SCO-000001`, `SRC-VIS-000006`, `SRC-VIS-000007`, `SRC-VIS-000008`, `SRC-MAT-000001` | Deployment vs. design, intelligence architecture, maturity, value realization |
| Governance and risk | `SRC-GOV-000003`, `SRC-GOV-000004` | Adaptive governance and breach-cost awareness |
| Security and trust | `SRC-SEC-000001`, `SRC-SEC-000002`, `SRC-SEC-000003` | Poisoning risk, cybersecurity evaluation, production safety |
| Use cases and business value | `SRC-UC-000004` to `SRC-UC-000010`, `SRC-MIS-000001` to `SRC-MIS-000003`, `SRC-PRM-000002`, `SRC-PRM-000004`, `SRC-ORG-000004` | Customer service, telecom, generative-AI basics, context engineering, value at scale |

## Recommendations

- Treat this public corpus as directional evidence for framing and options, not as company-specific fact evidence.
- Keep the blocked Pages source (`SRC-VIS-000005`) out of downstream text analysis until a Pages-capable extractor is explicitly approved.
- For future analysis, preserve source-level provenance in every note by citing source IDs and original relative paths.
- Where duplicate sources exist, use one canonical source ID in the synthesis and reference duplicates only as cross-links.
- Separate synthesis notes from source-derived facts so it remains clear what is direct evidence and what is project interpretation.

## Limitations

- This analysis is based on locally extracted text and metadata only.
- It does not infer company facts.
- It does not alter the blocked status of `SRC-VIS-000005`.
