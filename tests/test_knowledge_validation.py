import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import yaml

from scripts.validate_knowledge import main, validate_repository


class KnowledgeValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        for directory in (
            "config", "sources", "schemas", "knowledge/evidence",
            "knowledge/glossary", "knowledge/concepts", "knowledge/relationships",
        ):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self._write_yaml("sources/catalogue.yaml", {"records": [{"id": "SRC-TST-000001"}]})
        self._write_yaml("sources/processing-runs.yaml", {"records": [{
            "id": "RUN-000001", "status": "succeeded", "review_status": "verified",
        }]})
        self._write_yaml("config/knowledge-types.yaml", {"object_types": [
            {"type": "evidence_statement", "prefix": "EVID", "directory": "knowledge/evidence", "schema": "schemas/evidence.schema.yaml", "evidence_required": False},
            {"type": "glossary_term", "prefix": "TERM", "directory": "knowledge/glossary", "schema": "schemas/glossary-entry.schema.yaml", "evidence_required": True},
            {"type": "concept", "prefix": "CONCEPT", "directory": "knowledge/concepts", "schema": "schemas/concept.schema.yaml", "evidence_required": True},
            {"type": "relationship", "prefix": "REL", "directory": "knowledge/relationships", "schema": "schemas/relationship.schema.yaml", "evidence_required": True},
        ]})
        self._write_yaml("config/review-statuses.yaml", {"review_statuses": [{"id": value} for value in ("draft", "needs_review", "under_review", "verified", "approved", "rejected", "deprecated")]})
        self._write_yaml("config/evidence-confidence.yaml", {"confidence_values": [{"id": value} for value in ("low", "medium", "high")]})
        self._write_yaml("schemas/evidence.schema.yaml", {"required": ["id", "type", "statement", "source_id", "source_locator", "processing_run_id", "confidence", "review_status", "origin"]})
        self._write_yaml("schemas/glossary-entry.schema.yaml", {"required": ["id", "type", "term", "definition", "evidence_ids", "review_status", "origin"]})
        self._write_yaml("schemas/concept.schema.yaml", {"required": ["id", "type", "title", "summary", "evidence_ids", "review_status", "origin"]})
        self._write_yaml("schemas/relationship.schema.yaml", {"required": ["id", "type", "relationship_type", "from_id", "to_id", "evidence_ids", "review_status", "origin"]})

    def tearDown(self):
        self.tempdir.cleanup()

    def _write_yaml(self, relative_path, data):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    def _evidence(self, **changes):
        record = {
            "id": "EVID-000001", "type": "evidence_statement", "statement": "Fixture statement.",
            "source_id": "SRC-TST-000001", "source_locator": "page 1", "processing_run_id": "RUN-000001",
            "confidence": "medium", "review_status": "draft", "origin": "human",
        }
        record.update(changes)
        return record

    def _glossary(self, **changes):
        record = {
            "id": "TERM-000001", "type": "glossary_term", "term": "Fixture term",
            "definition": "Fixture definition.", "evidence_ids": ["EVID-000001"],
            "review_status": "draft", "origin": "human",
        }
        record.update(changes)
        return record

    def _concept(self, **changes):
        record = {
            "id": "CONCEPT-000001", "type": "concept", "title": "Fixture concept",
            "summary": "Fixture summary.", "evidence_ids": ["EVID-000001"],
            "review_status": "draft", "origin": "human",
        }
        record.update(changes)
        return record

    def test_empty_framework_passes(self):
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.records, 0)

    def test_valid_evidence_record_passes(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.evidence_records, 1)

    def test_unknown_source_id_fails(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence(source_id="SRC-TST-999999"))
        self.assertTrue(any("unknown source ID" in error for error in validate_repository(self.root).errors))

    def test_unreviewed_processing_run_fails(self):
        self._write_yaml("sources/processing-runs.yaml", {"records": [{
            "id": "RUN-000001", "status": "succeeded", "review_status": "draft",
        }]})
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())
        result = validate_repository(self.root)
        self.assertTrue(any("not a reviewed successful run" in error for error in result.errors))

    def test_duplicate_id_fails(self):
        self._write_yaml("knowledge/evidence/first.yaml", self._evidence())
        self._write_yaml("knowledge/evidence/second.yaml", self._evidence())
        self.assertTrue(any("duplicate ID" in error for error in validate_repository(self.root).errors))

    def test_invalid_review_status_fails(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence(review_status="published"))
        self.assertTrue(any("invalid review status" in error for error in validate_repository(self.root).errors))

    def test_glossary_entry_without_evidence_fails(self):
        self._write_yaml("knowledge/glossary/TERM-000001.yaml", self._glossary(evidence_ids=[]))
        self.assertTrue(any("requires at least one evidence ID" in error for error in validate_repository(self.root).errors))

    def test_invalid_identifier_fails(self):
        self._write_yaml("knowledge/evidence/invalid.yaml", self._evidence(id="EVID-1"))
        self.assertTrue(any("invalid identifier" in error for error in validate_repository(self.root).errors))

    def test_templates_are_ignored(self):
        self._write_yaml("knowledge/evidence/evidence-template.yaml", {"template": True, "id": "EVID-000000", "type": "evidence_statement"})
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.records, 0)

    def test_placeholder_id_in_production_file_fails(self):
        self._write_yaml("knowledge/evidence/record.yaml", self._evidence(id="EVID-000000"))
        self.assertTrue(any("placeholder ID" in error for error in validate_repository(self.root).errors))

    def test_approved_record_without_reviewer_fails(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence(review_status="approved"))
        self.assertTrue(any("requires reviewer" in error for error in validate_repository(self.root).errors))

    def test_catalogue_records_structure_is_supported(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())
        result = validate_repository(self.root)
        self.assertFalse(any("expected top-level 'records'" in error for error in result.errors))
        self.assertTrue(result.ok, result.errors)

    def test_legacy_markdown_note_is_not_structured_or_approved(self):
        (self.root / "knowledge/legacy-analysis.md").write_text("# Legacy analysis\n\nSubstantive but unstructured note.\n", encoding="utf-8")
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.records, 0)
        self.assertEqual(result.legacy_files, 1)

    def test_unstructured_markdown_in_object_directory_fails(self):
        (self.root / "knowledge/glossary/unstructured.md").write_text(
            "# Unstructured production content\n", encoding="utf-8"
        )
        self.assertTrue(any("requires YAML front matter" in error for error in validate_repository(self.root).errors))

    def test_unknown_evidence_reference_fails(self):
        self._write_yaml("knowledge/glossary/TERM-000001.yaml", self._glossary(evidence_ids=["EVID-999999"]))
        self.assertTrue(any("unknown evidence ID" in error for error in validate_repository(self.root).errors))

    def test_non_string_evidence_reference_fails_without_crashing(self):
        self._write_yaml(
            "knowledge/glossary/TERM-000001.yaml",
            self._glossary(evidence_ids=[{"id": "EVID-000001"}]),
        )
        result = validate_repository(self.root)
        self.assertTrue(any("unknown evidence ID" in error for error in result.errors))

    def test_non_string_controlled_values_fail_without_crashing(self):
        self._write_yaml(
            "knowledge/evidence/EVID-000001.yaml",
            self._evidence(
                source_id={"id": "SRC-TST-000001"},
                confidence=["medium"],
                review_status={"id": "draft"},
            ),
        )
        result = validate_repository(self.root)
        self.assertTrue(any("unknown source ID" in error for error in result.errors))
        self.assertTrue(any("invalid evidence confidence" in error for error in result.errors))
        self.assertTrue(any("invalid review status" in error for error in result.errors))

    def test_dangling_relationship_endpoint_fails(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", self._concept())
        self._write_yaml("knowledge/relationships/REL-000001.yaml", {
            "id": "REL-000001", "type": "relationship", "relationship_type": "relates_to",
            "from_id": "CONCEPT-000001", "to_id": "CONCEPT-999999",
            "evidence_ids": ["EVID-000001"], "review_status": "draft", "origin": "human",
        })
        self.assertTrue(any("to_id references unknown" in error for error in validate_repository(self.root).errors))

    def test_non_string_relationship_endpoint_fails_without_crashing(self):
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", self._concept())
        self._write_yaml("knowledge/relationships/REL-000001.yaml", {
            "id": "REL-000001", "type": "relationship", "relationship_type": "relates_to",
            "from_id": {"id": "CONCEPT-000001"}, "to_id": "CONCEPT-000001",
            "evidence_ids": ["EVID-000001"], "review_status": "draft", "origin": "human",
        })
        result = validate_repository(self.root)
        self.assertTrue(any("from_id references unknown" in error for error in result.errors))

    def test_unsupported_object_type_fails(self):
        self._write_yaml("knowledge/evidence/unknown.yaml", {
            "id": "UNKNOWN-000001", "type": "unknown", "review_status": "draft"
        })
        self.assertTrue(any("unsupported object type" in error for error in validate_repository(self.root).errors))

    def test_non_string_object_type_fails_without_crashing(self):
        self._write_yaml("knowledge/evidence/unknown.yaml", {
            "id": "EVID-000001", "type": {"name": "evidence_statement"},
            "review_status": "draft",
        })
        result = validate_repository(self.root)
        self.assertTrue(any("unsupported object type" in error for error in result.errors))

    def test_structured_record_outside_configured_directory_fails(self):
        self._write_yaml("knowledge/EVID-000001.yaml", self._evidence())
        self.assertTrue(any("outside a configured" in error for error in validate_repository(self.root).errors))

    def test_cli_exit_codes_follow_validation_result(self):
        with redirect_stdout(StringIO()):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence(source_id="SRC-TST-999999"))
        with redirect_stdout(StringIO()):
            self.assertNotEqual(main(["--root", str(self.root)]), 0)


if __name__ == "__main__":
    unittest.main()
