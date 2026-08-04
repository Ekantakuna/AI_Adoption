import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import yaml

from scripts.validate_schemas import main, validate_repository


DIALECT = "https://json-schema.org/draft/2020-12/schema"


class SchemaValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        for directory in ("config", "schemas", "sources", "knowledge/concepts"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self._write_yaml("schemas/sources.yaml", {
            "$schema": DIALECT,
            "type": "object",
            "required": ["records"],
            "properties": {"records": {"type": "array"}},
            "additionalProperties": False,
        })
        self._write_yaml("schemas/concept.schema.yaml", {
            "$schema": DIALECT,
            "type": "object",
            "required": ["id", "type", "title"],
            "properties": {
                "id": {"type": "string", "pattern": "^CONCEPT-[0-9]{6}$"},
                "type": {"const": "concept"},
                "title": {"type": "string", "minLength": 1},
            },
            "additionalProperties": False,
        })
        self._write_yaml("sources/catalogue.yaml", {"records": []})
        self._write_yaml("config/knowledge-types.yaml", {"object_types": [{
            "type": "concept",
            "directory": "knowledge/concepts",
            "schema": "schemas/concept.schema.yaml",
        }]})

    def tearDown(self):
        self.tempdir.cleanup()

    def _write_yaml(self, relative_path, data):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    def test_valid_schemas_and_records_pass(self):
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", {
            "id": "CONCEPT-000001", "type": "concept", "title": "Fixture",
        })
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.schemas, 2)
        self.assertEqual(result.knowledge_records, 1)

    def test_governed_source_processing_register_is_validated(self):
        self._write_yaml("schemas/processing-run.schema.yaml", {
            "$schema": DIALECT,
            "type": "object",
            "required": ["records"],
            "properties": {"records": {"type": "array"}},
            "additionalProperties": False,
        })
        self._write_yaml("sources/processing-runs.yaml", {"records": "invalid"})
        result = validate_repository(self.root)
        self.assertTrue(any("not of type 'array'" in error for error in result.errors))

    def test_invalid_source_catalogue_fails(self):
        self._write_yaml("sources/catalogue.yaml", {"records": "not-an-array"})
        result = validate_repository(self.root)
        self.assertTrue(any("not of type 'array'" in error for error in result.errors))

    def test_invalid_schema_fails_meta_schema_validation(self):
        self._write_yaml("schemas/concept.schema.yaml", {
            "$schema": DIALECT, "type": "not-a-json-schema-type",
        })
        result = validate_repository(self.root)
        self.assertTrue(any("invalid Draft 2020-12 schema" in error for error in result.errors))

    def test_invalid_knowledge_record_fails(self):
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", {
            "id": "CONCEPT-000001", "type": "concept", "title": "",
        })
        result = validate_repository(self.root)
        self.assertTrue(any("should be non-empty" in error for error in result.errors))

    def test_templates_are_ignored(self):
        self._write_yaml("knowledge/concepts/concept-template.yaml", {
            "template": True, "id": "CONCEPT-000000", "type": "concept",
        })
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.knowledge_records, 0)

    def test_configured_reference_schema_is_enforced(self):
        self._write_yaml("schemas/reference.schema.yaml", {
            "$schema": DIALECT,
            "type": "object",
            "required": ["id", "type", "locator"],
            "properties": {
                "id": {"type": "string", "pattern": "^REF-[0-9]{6}$"},
                "type": {"const": "reference"},
                "locator": {"type": "string", "minLength": 1},
            },
            "additionalProperties": False,
        })
        self._write_yaml("config/knowledge-types.yaml", {"object_types": [{
            "type": "reference",
            "directory": "knowledge/references",
            "schema": "schemas/reference.schema.yaml",
        }]})
        self._write_yaml("knowledge/references/REF-000001.yaml", {
            "id": "REF-000001", "type": "reference",
        })
        result = validate_repository(self.root)
        self.assertTrue(any("'locator' is a required property" in error for error in result.errors))

    def test_cli_exit_codes_follow_validation_result(self):
        with redirect_stdout(StringIO()):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self._write_yaml("sources/catalogue.yaml", {"records": "not-an-array"})
        with redirect_stdout(StringIO()):
            self.assertNotEqual(main(["--root", str(self.root)]), 0)


if __name__ == "__main__":
    unittest.main()
