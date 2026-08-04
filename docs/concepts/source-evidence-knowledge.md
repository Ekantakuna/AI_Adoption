# Source, evidence, and knowledge

Source metadata describes an external asset without interpreting its body. The
canonical metadata record is a `SRC` entry in `sources/catalogue.yaml`; the
original asset stays outside Git. A processing run uses a reviewed route and
tool to create an extraction derivative. Extraction alone is neither evidence
nor knowledge.

Atomic evidence is one source-attributable statement in an `EVID` YAML record.
Its inputs are a catalogue source and approved processing run; its output
preserves the source ID, precise locator, run ID, classification, confidence,
creator, and review status. Stage 9 validates source IDs but the processing-run
contract was approved immediately after Stage 9. The run register is currently
operational with one verified run. `EVID-000001` is the first AI-origin atomic
statement and was human-verified for source fidelity; that verification does
not establish implementation or broader approval.

Knowledge is interpretation built from evidence. Terms, concepts, frameworks,
metrics, risks, trends, use cases, and knowledge decisions cite evidence IDs.
Assumptions explicitly represent unverified propositions and may expose an
evidence gap. Relationships link existing knowledge objects and also cite
evidence. Knowledge does not modify upstream source metadata or evidence.

Assessments apply a method to reviewed knowledge. Reports select reviewed
assessment or knowledge content for an audience, and presentations are
derivatives of approved report inputs. Downstream generation never grants
authority to an upstream record.
