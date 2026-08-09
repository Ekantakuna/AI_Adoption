import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_prompts import validate_repository


class PromptValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "prompts/codex").mkdir(parents=True)

    def tearDown(self):
        self.tempdir.cleanup()

    def write_prompt(self, name="one.md", **changes):
        data = {
            "id": "PRM-001", "title": "One", "type": "maintenance", "version": "1.0.0",
            "status": "active", "owner_role": "owner", "created_at": "2026-08-05",
            "updated_at": "2026-08-05", "roadmap_stage": "cross-stage",
            "source_access": "repository_only", "allowed_paths": [], "prohibited_actions": ["commit"],
            "required_inputs": [], "expected_outputs": [], "validation": [], "human_review": "required",
            "supersedes": None, "superseded_by": None,
        }
        data.update(changes)
        front = yaml.safe_dump(data, sort_keys=False).strip()
        path = self.root / "prompts/codex" / name
        path.write_text(f"---\n{front}\n---\n\n# Prompt\n", encoding="utf-8")
        self.write_catalogue(data, f"prompts/codex/{name}")

    def write_catalogue(self, data, path):
        entry = {k: data[k] for k in ("id", "type", "version", "status", "roadmap_stage", "source_access")}
        entry.update({"path": path, "purpose": "test", "expected_output_category": "report"})
        (self.root / "prompts/codex/prompt-catalogue.yaml").write_text(
            yaml.safe_dump({"catalogue_version": 1, "prompts": [entry]}, sort_keys=False), encoding="utf-8"
        )

    def test_valid_prompt_passes(self):
        self.write_prompt()
        self.assertTrue(validate_repository(self.root).ok)

    def test_active_prompt_must_be_catalogued(self):
        self.write_prompt()
        extra = self.root / "prompts/codex/two.md"
        extra.write_text((self.root / "prompts/codex/one.md").read_text().replace("PRM-001", "PRM-002"), encoding="utf-8")
        result = validate_repository(self.root)
        self.assertTrue(any("not catalogued" in error for error in result.errors))

    def test_template_cannot_be_active(self):
        self.write_prompt(type="template")
        result = validate_repository(self.root)
        self.assertTrue(any("production type" in error or "templates cannot" in error for error in result.errors))

    def test_deprecated_prompt_needs_replacement(self):
        self.write_prompt(status="deprecated")
        result = validate_repository(self.root)
        self.assertTrue(any("needs superseded_by" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
