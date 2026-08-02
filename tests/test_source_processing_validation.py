import tempfile
import unittest
import hashlib
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import yaml

from scripts.validate_source_processing import main, validate_repository


class SourceProcessingValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        for directory in ("config", "sources"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self._write_yaml("config/source-processing.yaml", {
            "authorization_statuses": ["proposed", "approved", "revoked"],
            "run_statuses": ["planned", "in_progress", "succeeded", "failed", "blocked"],
            "tool_statuses": ["proposed", "approved", "deprecated"],
            "environments": ["approved_local", "approved_on_prem", "approved_external"],
            "routes": [{
                "id": "local_only", "allowed_classifications": ["public", "internal", "restricted"],
            }],
            "tools": [{
                "id": "pdftotext_local", "source_types": ["pdf"],
                "extensions": [".pdf"], "allowed_routes": ["local_only"],
                "status": "approved",
            }],
        })
        self._write_yaml("sources/catalogue.yaml", {"records": [self._source()]})
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations", "records": [],
        })
        self._write_yaml("sources/processing-runs.yaml", {
            "register": "source_processing_runs", "records": [],
        })

    def tearDown(self):
        self.tempdir.cleanup()

    def _write_yaml(self, relative_path, data):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    def _source(self, **changes):
        record = {
            "id": "SRC-TST-000001", "classification": "public",
            "processing_status": "metadata_catalogued", "source_type": "pdf",
            "file_extension": ".pdf", "content_hash_sha256": "a" * 64,
        }
        record.update(changes)
        return record

    def _authorization(self, **changes):
        record = {
            "id": "AUTH-000001", "source_id": "SRC-TST-000001",
            "classification": "public", "route_id": "local_only",
            "tool_id": "pdftotext_local", "environment": "approved_local",
            "status": "approved", "approved_by": "Maksim Zakharenkau",
            "approved_at": "2026-08-02", "basis_refs": ["review.md"],
        }
        record.update(changes)
        return record

    def _run(self, **changes):
        record = {
            "id": "RUN-000001", "authorization_id": "AUTH-000001",
            "source_id": "SRC-TST-000001", "source_hash_sha256": "a" * 64,
            "classification": "public", "route_id": "local_only",
            "tool_id": "pdftotext_local", "tool_version": "1.0",
            "environment": "approved_local", "status": "succeeded",
            "started_at": "2026-08-02T10:00:00Z", "completed_at": "2026-08-02T10:01:00Z",
            "output_ref": "local/output.txt", "output_hash_sha256": "b" * 64,
            "executed_by": "fixture", "review_status": "verified",
            "reviewer": {"name": "Maksim Zakharenkau", "reviewed_at": "2026-08-02"},
        }
        record.update(changes)
        return record

    def test_empty_nonprocessable_framework_passes(self):
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)

    def test_processable_source_requires_approved_authorization(self):
        self._write_yaml("sources/catalogue.yaml", {
            "records": [self._source(processing_status="approved_for_processing")],
        })
        result = validate_repository(self.root)
        self.assertTrue(any("processable without" in error for error in result.errors))

    def test_valid_approved_authorization_passes(self):
        self._write_yaml("sources/catalogue.yaml", {
            "records": [self._source(processing_status="approved_for_processing")],
        })
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations", "records": [self._authorization()],
        })
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.approved_authorizations, 1)

    def test_ambiguous_approver_fails(self):
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations",
            "records": [self._authorization(approved_by="user")],
        })
        result = validate_repository(self.root)
        self.assertTrue(any("identified human approver" in error for error in result.errors))

    def test_classification_mismatch_fails(self):
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations",
            "records": [self._authorization(classification="internal")],
        })
        result = validate_repository(self.root)
        self.assertTrue(any("classification does not match" in error for error in result.errors))

    def test_approved_authorization_cannot_use_proposed_tool(self):
        config = yaml.safe_load((self.root / "config/source-processing.yaml").read_text())
        config["tools"][0]["status"] = "proposed"
        self._write_yaml("config/source-processing.yaml", config)
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations",
            "records": [self._authorization()],
        })
        result = validate_repository(self.root)
        self.assertTrue(any("uses an unapproved tool" in error for error in result.errors))

    def test_valid_reviewed_run_is_evidence_eligible(self):
        self._write_yaml("sources/catalogue.yaml", {
            "records": [self._source(processing_status="approved_for_processing")],
        })
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations", "records": [self._authorization()],
        })
        self._write_yaml("sources/processing-runs.yaml", {
            "register": "source_processing_runs", "records": [self._run()],
        })
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.evidence_eligible_runs, 1)

    def test_run_hash_mismatch_fails(self):
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations", "records": [self._authorization()],
        })
        self._write_yaml("sources/processing-runs.yaml", {
            "register": "source_processing_runs",
            "records": [self._run(source_hash_sha256="c" * 64)],
        })
        result = validate_repository(self.root)
        self.assertTrue(any("source hash does not match" in error for error in result.errors))

    def test_local_output_verification_checks_derivative_hash(self):
        output = self.root / "sources/extracted/private/RUN-000001.txt"
        output.parent.mkdir(parents=True)
        output.write_bytes(b"synthetic derivative\n")
        output_hash = hashlib.sha256(output.read_bytes()).hexdigest()
        self._write_yaml("sources/catalogue.yaml", {
            "records": [self._source(processing_status="extracted")],
        })
        self._write_yaml("sources/processing-authorizations.yaml", {
            "register": "source_processing_authorizations",
            "records": [self._authorization()],
        })
        self._write_yaml("sources/processing-runs.yaml", {
            "register": "source_processing_runs",
            "records": [self._run(
                output_ref="sources/extracted/private/RUN-000001.txt",
                output_hash_sha256=output_hash,
            )],
        })
        result = validate_repository(self.root, verify_local_outputs=True)
        self.assertTrue(result.ok, result.errors)
        output.write_bytes(b"changed derivative\n")
        result = validate_repository(self.root, verify_local_outputs=True)
        self.assertTrue(any("local output hash does not match" in e for e in result.errors))

    def test_cli_exit_codes_follow_validation_result(self):
        with redirect_stdout(StringIO()):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self._write_yaml("sources/catalogue.yaml", {
            "records": [self._source(processing_status="approved_for_processing")],
        })
        with redirect_stdout(StringIO()):
            self.assertNotEqual(main(["--root", str(self.root)]), 0)


if __name__ == "__main__":
    unittest.main()
