import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import yaml

from scripts.validate_relationship_impact import main, traverse, validate_repository


class RelationshipImpactValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        for directory in (
            "config", "knowledge/evidence", "knowledge/concepts",
            "knowledge/metrics", "knowledge/risks", "knowledge/relationships",
        ):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self._write_yaml("config/review-statuses.yaml", {
            "review_statuses": [{"id": value} for value in (
                "draft", "needs_review", "under_review", "verified",
                "approved", "rejected", "deprecated",
            )]
        })
        self._write_yaml("config/knowledge-types.yaml", {"object_types": [
            {"type": "evidence_statement", "directory": "knowledge/evidence"},
            {"type": "concept", "directory": "knowledge/concepts"},
            {"type": "metric", "directory": "knowledge/metrics"},
            {"type": "risk", "directory": "knowledge/risks"},
            {"type": "relationship", "directory": "knowledge/relationships"},
        ]})
        self._write_yaml("config/relationship-types.yaml", {
            "schema_version": 1,
            "traversal": {
                "default_max_depth": 1,
                "hard_max_depth": 25,
                "reviewed_statuses": ["verified", "approved"],
                "audit_statuses": [
                    "draft", "needs_review", "under_review", "verified",
                    "approved", "rejected", "deprecated",
                ],
            },
            "relationship_types": [
                self._relationship_definition("supports", "directed", "from_to", "conceptual"),
                self._relationship_definition("contradicts", "symmetric", "both", "conceptual"),
                self._relationship_definition("refines", "directed", "both", "conceptual"),
                self._relationship_definition("depends_on", "directed", "to_from", "acyclic_homogeneous"),
                self._relationship_definition("influences", "directed", "from_to", "conceptual"),
                {
                    **self._relationship_definition("measures", "directed", "to_from", "conceptual"),
                    "allowed_from_types": ["metric"],
                },
                {
                    **self._relationship_definition("mitigates", "directed", "both", "conceptual"),
                    "allowed_to_types": ["risk"],
                },
                self._relationship_definition("relates_to", "symmetric", "both", "conceptual"),
                {
                    **self._relationship_definition("supersedes", "directed", "to_from", "acyclic_any"),
                    "same_endpoint_type_required": True,
                    "target_status_required": "deprecated",
                },
            ],
        })
        self._write_yaml("knowledge/evidence/EVID-000001.yaml", self._evidence())

    def tearDown(self):
        self.tempdir.cleanup()

    @staticmethod
    def _relationship_definition(name, direction, impact_direction, cycle_policy):
        return {
            "id": name,
            "direction": direction,
            "impact_direction": impact_direction,
            "allowed_from_types": ["any_knowledge"],
            "allowed_to_types": ["any_knowledge"],
            "cycle_policy": cycle_policy,
        }

    def _write_yaml(self, relative_path, data):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        return path

    @staticmethod
    def _reviewer():
        return {"name": "Reviewer", "reviewed_at": "2026-08-14"}

    def _evidence(self, **changes):
        data = {
            "id": "EVID-000001",
            "type": "evidence_statement",
            "review_status": "verified",
            "classification": "internal",
            "reviewer": self._reviewer(),
        }
        data.update(changes)
        return data

    def _concept(self, record_id, **changes):
        data = {
            "id": record_id,
            "type": "concept",
            "evidence_ids": ["EVID-000001"],
            "review_status": "approved",
            "classification": "internal",
            "reviewer": self._reviewer(),
        }
        data.update(changes)
        return data

    def _relationship(self, record_id, source, target, kind="supports", **changes):
        data = {
            "id": record_id,
            "type": "relationship",
            "relationship_type": kind,
            "from_id": source,
            "to_id": target,
            "evidence_ids": ["EVID-000001"],
            "review_status": "approved",
            "classification": "internal",
            "reviewer": self._reviewer(),
        }
        data.update(changes)
        return data

    def _add_concepts(self, *record_ids):
        for record_id in record_ids:
            self._write_yaml(f"knowledge/concepts/{record_id}.yaml", self._concept(record_id))

    def test_valid_one_hop_relationship(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        graph = traverse(result, "CONCEPT-000001", "downstream", 1)
        self.assertEqual([node["id"] for node in graph.nodes], ["CONCEPT-000001", "CONCEPT-000002"])

    def test_valid_multi_hop_impact_traversal(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        result = validate_repository(self.root)
        graph = traverse(result, "EVID-000001", "impact", 2)
        self.assertEqual(
            {node["id"] for node in graph.nodes},
            {"EVID-000001", "CONCEPT-000001", "CONCEPT-000002"},
        )

    def test_dangling_source_fails(self):
        self._add_concepts("CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-999999", "CONCEPT-000002"
        ))
        errors = validate_repository(self.root).errors
        self.assertTrue(any("source endpoint" in error for error in errors))

    def test_dangling_target_fails(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-999999"
        ))
        errors = validate_repository(self.root).errors
        self.assertTrue(any("target endpoint" in error for error in errors))

    def test_unknown_relationship_type_fails(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "invented"
        ))
        self.assertTrue(any("unknown relationship type" in error for error in validate_repository(self.root).errors))

    def test_duplicate_relationship_id_fails(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        relationship = self._relationship("REL-000001", "CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/one.yaml", relationship)
        self._write_yaml("knowledge/relationships/two.yaml", relationship)
        self.assertTrue(any("duplicate ID REL-000001" in error for error in validate_repository(self.root).errors))

    def test_missing_evidence_reference_fails(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002",
            evidence_ids=["EVID-999999"],
        ))
        self.assertTrue(any("unknown evidence ID" in error for error in validate_repository(self.root).errors))

    def test_dependency_cycle_is_structurally_invalid(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "depends_on"
        ))
        self._write_yaml("knowledge/relationships/REL-000002.yaml", self._relationship(
            "REL-000002", "CONCEPT-000002", "CONCEPT-000001", "depends_on"
        ))
        self.assertTrue(any("structurally invalid" in error for error in validate_repository(self.root).errors))

    def test_any_cycle_containing_supersedes_is_structurally_invalid(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/concepts/CONCEPT-000002.yaml", self._concept(
            "CONCEPT-000002", review_status="deprecated", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "supersedes"
        ))
        self._write_yaml("knowledge/relationships/REL-000002.yaml", self._relationship(
            "REL-000002", "CONCEPT-000002", "CONCEPT-000001", "supports"
        ))
        self.assertTrue(any("structurally invalid" in error for error in validate_repository(self.root).errors))

    def test_conceptual_cycle_is_reported_and_traversal_terminates(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "relates_to"
        ))
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("permitted conceptual cycle" in warning for warning in result.warnings))
        graph = traverse(result, "CONCEPT-000001", "downstream", 5)
        self.assertEqual(len(graph.nodes), 2)
        self.assertTrue(graph.cycles)

    def test_valid_supersession_resolves_deprecated_object(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/concepts/CONCEPT-000002.yaml", self._concept(
            "CONCEPT-000002", review_status="deprecated", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "supersedes"
        ))
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertFalse(any("deprecated target" in warning for warning in result.warnings))
        graph = traverse(result, "CONCEPT-000002", "impact", 1)
        self.assertIn("CONCEPT-000001", {node["id"] for node in graph.nodes})
        self.assertTrue(any("deprecated object" in warning for warning in graph.warnings))

    def test_impact_direction_follows_dependency_to_dependent(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "depends_on"
        ))
        result = validate_repository(self.root)
        graph = traverse(result, "CONCEPT-000002", "impact", 1)
        self.assertIn("CONCEPT-000001", {node["id"] for node in graph.nodes})

    def test_repeated_node_is_emitted_once_with_alternate_path(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002", "CONCEPT-000003")
        for number, source, target in (
            (1, "CONCEPT-000001", "CONCEPT-000002"),
            (2, "CONCEPT-000001", "CONCEPT-000003"),
            (3, "CONCEPT-000002", "CONCEPT-000003"),
        ):
            self._write_yaml(f"knowledge/relationships/REL-{number:06d}.yaml", self._relationship(
                f"REL-{number:06d}", source, target
            ))
        result = validate_repository(self.root)
        graph = traverse(result, "CONCEPT-000001", "downstream", 2)
        self.assertEqual([node["id"] for node in graph.nodes].count("CONCEPT-000003"), 1)
        self.assertTrue(any(path["to_id"] == "CONCEPT-000003" for path in graph.alternate_paths))

    def test_self_relation_fails(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000001"
        ))
        self.assertTrue(any("self-relation" in error for error in validate_repository(self.root).errors))

    def test_invalid_review_state_fails(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", review_status="magically_approved"
        ))
        self.assertTrue(any("invalid review status" in error for error in validate_repository(self.root).errors))

    def test_active_relationship_to_unreviewed_endpoint_fails(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/concepts/CONCEPT-000002.yaml", self._concept(
            "CONCEPT-000002", review_status="needs_review", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        self.assertTrue(any("non-reviewed target" in error for error in validate_repository(self.root).errors))

    def test_reviewed_relationship_without_reviewer_metadata_fails(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", reviewer=None
        ))
        self.assertTrue(any("requires reviewer metadata" in error for error in validate_repository(self.root).errors))

    def test_prohibited_endpoint_type_pairing_fails(self):
        self._write_yaml("knowledge/metrics/METRIC-000001.yaml", {
            **self._concept("METRIC-000001"),
            "type": "metric",
        })
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", self._concept(
            "CONCEPT-000001", review_status="deprecated", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "METRIC-000001", "CONCEPT-000001", "supersedes"
        ))
        self.assertTrue(any("endpoints must have the same type" in error for error in validate_repository(self.root).errors))

    def test_active_relationship_to_rejected_endpoint_fails(self):
        self._add_concepts("CONCEPT-000001")
        self._write_yaml("knowledge/concepts/CONCEPT-000002.yaml", self._concept(
            "CONCEPT-000002", review_status="rejected", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        self.assertTrue(any("rejected target endpoint" in error for error in validate_repository(self.root).errors))

    def test_semantic_duplicate_and_deprecated_endpoint_are_warnings(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/concepts/CONCEPT-000003.yaml", self._concept(
            "CONCEPT-000003", review_status="deprecated", reviewer=None
        ))
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        self._write_yaml("knowledge/relationships/REL-000002.yaml", self._relationship(
            "REL-000002", "CONCEPT-000001", "CONCEPT-000002"
        ))
        self._write_yaml("knowledge/relationships/REL-000003.yaml", self._relationship(
            "REL-000003", "CONCEPT-000001", "CONCEPT-000003"
        ))
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("semantic duplicate" in warning for warning in result.warnings))
        self.assertTrue(any("deprecated target endpoint" in warning for warning in result.warnings))

    def test_contradiction_is_exposed_as_unresolved_conflict(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "contradicts"
        ))
        result = validate_repository(self.root)
        graph = traverse(result, "CONCEPT-000001", "downstream", 1)
        self.assertEqual(["REL-000001"], graph.conflicts)

    def test_text_output_prints_alternate_cycle_and_conflict_sections(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002", "CONCEPT-000003")
        for number, source, target, kind in (
            (1, "CONCEPT-000001", "CONCEPT-000002", "relates_to"),
            (2, "CONCEPT-000001", "CONCEPT-000003", "contradicts"),
            (3, "CONCEPT-000002", "CONCEPT-000003", "supports"),
        ):
            self._write_yaml(f"knowledge/relationships/REL-{number:06d}.yaml", self._relationship(
                f"REL-{number:06d}", source, target, kind
            ))
        output = StringIO()
        with redirect_stdout(output):
            exit_code = main([
                "--root", str(self.root), "--start-id", "CONCEPT-000001",
                "--direction", "downstream", "--max-depth", "3",
            ])
        self.assertEqual(0, exit_code)
        rendered = output.getvalue()
        self.assertIn("ALTERNATE", rendered)
        self.assertIn("CYCLE", rendered)
        self.assertIn("CONFLICT relationship=REL-000002 status=unresolved", rendered)

    def test_reviewed_and_audit_views_filter_unreviewed_records(self):
        self._write_yaml("knowledge/concepts/CONCEPT-000001.yaml", self._concept(
            "CONCEPT-000001", review_status="needs_review", reviewer=None
        ))
        result = validate_repository(self.root)
        with self.assertRaisesRegex(ValueError, "not eligible"):
            traverse(result, "CONCEPT-000001", "impact", 1)
        audit = traverse(result, "CONCEPT-000001", "impact", 1, include_unreviewed=True)
        self.assertEqual(["CONCEPT-000001"], [node["id"] for node in audit.nodes])

    def test_depth_truncation_and_hard_limit_are_reported(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        result = validate_repository(self.root)
        truncated = traverse(result, "CONCEPT-000001", "downstream", 0)
        self.assertTrue(truncated.truncated)
        self.assertTrue(any("impact beyond this boundary is unknown" in warning for warning in truncated.warnings))
        with self.assertRaisesRegex(ValueError, "between 0 and 25"):
            traverse(result, "CONCEPT-000001", "downstream", 26)

    def test_upstream_and_both_directions_are_explicit(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        result = validate_repository(self.root)
        upstream = traverse(result, "CONCEPT-000002", "upstream", 1)
        self.assertIn("CONCEPT-000001", {node["id"] for node in upstream.nodes})
        both = traverse(result, "CONCEPT-000002", "both", 1)
        self.assertIn("CONCEPT-000001", {node["id"] for node in both.nodes})
        self.assertIn("EVID-000001", {node["id"] for node in both.nodes})

    def test_remaining_relationship_types_follow_configured_impact_directions(self):
        self._add_concepts(
            "CONCEPT-000001", "CONCEPT-000002", "CONCEPT-000003",
            "CONCEPT-000004", "CONCEPT-000005", "CONCEPT-000006",
        )
        self._write_yaml("knowledge/metrics/METRIC-000001.yaml", {
            **self._concept("METRIC-000001"),
            "type": "metric",
        })
        self._write_yaml("knowledge/risks/RISK-000001.yaml", {
            **self._concept("RISK-000001"),
            "type": "risk",
        })
        for number, source, target, kind in (
            (1, "CONCEPT-000001", "CONCEPT-000002", "refines"),
            (2, "CONCEPT-000003", "CONCEPT-000004", "influences"),
            (3, "METRIC-000001", "CONCEPT-000005", "measures"),
            (4, "CONCEPT-000006", "RISK-000001", "mitigates"),
        ):
            self._write_yaml(f"knowledge/relationships/REL-{number:06d}.yaml", self._relationship(
                f"REL-{number:06d}", source, target, kind
            ))
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)

        cases = (
            ("refines forward", "CONCEPT-000001", "CONCEPT-000002", True),
            ("refines reverse", "CONCEPT-000002", "CONCEPT-000001", True),
            ("influences forward", "CONCEPT-000003", "CONCEPT-000004", True),
            ("influences reverse", "CONCEPT-000004", "CONCEPT-000003", False),
            ("measures from measured object", "CONCEPT-000005", "METRIC-000001", True),
            ("measures from metric", "METRIC-000001", "CONCEPT-000005", False),
            ("mitigates forward", "CONCEPT-000006", "RISK-000001", True),
            ("mitigates reverse", "RISK-000001", "CONCEPT-000006", True),
        )
        for label, start, expected, present in cases:
            with self.subTest(label=label):
                node_ids = {node["id"] for node in traverse(result, start, "impact", 1).nodes}
                self.assertEqual(present, expected in node_ids)

    def test_measures_and_mitigates_endpoint_constraints_fail(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002", "CONCEPT-000003")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002", "measures"
        ))
        self._write_yaml("knowledge/relationships/REL-000002.yaml", self._relationship(
            "REL-000002", "CONCEPT-000001", "CONCEPT-000003", "mitigates"
        ))
        errors = validate_repository(self.root).errors
        self.assertTrue(any("source type 'concept' is prohibited for measures" in error for error in errors))
        self.assertTrue(any("target type 'concept' is prohibited for mitigates" in error for error in errors))

    def test_relationship_record_cannot_be_used_as_traversal_node(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml("knowledge/relationships/REL-000001.yaml", self._relationship(
            "REL-000001", "CONCEPT-000001", "CONCEPT-000002"
        ))
        result = validate_repository(self.root)
        with self.assertRaisesRegex(ValueError, "edge record"):
            traverse(result, "REL-000001", "impact", 1)

    def test_traversal_does_not_modify_canonical_records_or_write_graph_store(self):
        self._add_concepts("CONCEPT-000001", "CONCEPT-000002")
        self._write_yaml(
            "knowledge/relationships/REL-000001.yaml",
            self._relationship("REL-000001", "CONCEPT-000001", "CONCEPT-000002"),
        )
        before_files = {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in sorted(self.root.rglob("*")) if path.is_file()
        }
        before_directories = {
            str(path.relative_to(self.root))
            for path in sorted(self.root.rglob("*")) if path.is_dir()
        }
        result = validate_repository(self.root)
        for direction in ("upstream", "downstream", "both", "impact"):
            traverse(result, "CONCEPT-000001", direction, 2)
        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(0, main([
                "--root", str(self.root), "--start-id", "CONCEPT-000001",
                "--direction", "impact", "--max-depth", "2", "--format", "json",
            ]))
        after_files = {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in sorted(self.root.rglob("*")) if path.is_file()
        }
        after_directories = {
            str(path.relative_to(self.root))
            for path in sorted(self.root.rglob("*")) if path.is_dir()
        }
        self.assertEqual(before_files, after_files)
        self.assertEqual(before_directories, after_directories)


if __name__ == "__main__":
    unittest.main()
