import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_roadmap import validate


ROOT = Path(__file__).resolve().parents[1]


class RoadmapValidationTests(unittest.TestCase):
    def test_repository_roadmap_passes(self):
        self.assertEqual(validate(ROOT), [])

    def make_fixture(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "project/roadmap").mkdir(parents=True)
        data = yaml.safe_load((ROOT / "project/roadmap.yaml").read_text())
        (root / "project/roadmap.yaml").write_text(yaml.safe_dump(data, sort_keys=False))
        (root / "project/roadmap/implementation-roadmap.md").write_text(
            (ROOT / "project/roadmap/implementation-roadmap.md").read_text()
        )
        return temp, root, data

    def test_duplicate_id_is_rejected(self):
        temp, root, data = self.make_fixture()
        self.addCleanup(temp.cleanup)
        data["stages"].append(dict(data["stages"][0]))
        (root / "project/roadmap.yaml").write_text(yaml.safe_dump(data, sort_keys=False))
        self.assertTrue(any("duplicate stage ID" in error for error in validate(root)))

    def test_missing_reference_is_rejected(self):
        temp, root, data = self.make_fixture()
        self.addCleanup(temp.cleanup)
        data["stages"][1]["dependencies"] = ["stage-99"]
        (root / "project/roadmap.yaml").write_text(yaml.safe_dump(data, sort_keys=False))
        self.assertTrue(any("references missing stage" in error for error in validate(root)))

    def test_dependency_cycle_is_rejected(self):
        temp, root, data = self.make_fixture()
        self.addCleanup(temp.cleanup)
        data["stages"][0]["dependencies"] = ["stage-09.5"]
        (root / "project/roadmap.yaml").write_text(yaml.safe_dump(data, sort_keys=False))
        self.assertTrue(any("dependency cycle" in error for error in validate(root)))

    def test_human_machine_mismatch_is_rejected(self):
        temp, root, _ = self.make_fixture()
        self.addCleanup(temp.cleanup)
        path = root / "project/roadmap/implementation-roadmap.md"
        path.write_text(path.read_text().replace("## Stage-16 —", "## Stage-99 —", 1))
        self.assertTrue(any("stage headings do not match" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
