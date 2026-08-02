import tempfile
import unittest
from pathlib import Path

from scripts.extract_text import extract_content, resolve_output_path, sha256_file


class ExtractTextTests(unittest.TestCase):
    def test_plain_text_is_normalized(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.mmd"
            path.write_text("alpha   beta\n\n gamma\n", encoding="utf-8")
            self.assertEqual(extract_content(path), "alpha beta\ngamma\n")

    def test_html_omits_script_and_style_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.html"
            path.write_text(
                "<html><style>hidden</style><body><h1>Title</h1><p>Visible text</p>"
                "<script>hidden()</script></body></html>",
                encoding="utf-8",
            )
            self.assertEqual(extract_content(path), "Title\nVisible text\n")

    def test_unsupported_extension_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.pages"
            path.write_text("fixture", encoding="utf-8")
            with self.assertRaises(ValueError):
                extract_content(path)

    def test_sha256_file_hashes_raw_source_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.mmd"
            path.write_bytes(b"alpha\r\nbeta\n")
            self.assertEqual(
                sha256_file(path),
                "4f85d1b0cff7bb76f0c9a58366030c6dc1eb8e1243e3709c72452278ddce7c13",
            )

    def test_internal_output_requires_private_extraction_area(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            allowed = resolve_output_path(
                root, Path("sources/extracted/private/RUN-000001.txt"), "internal"
            )
            self.assertEqual(
                allowed, root / "sources/extracted/private/RUN-000001.txt"
            )
            with self.assertRaises(ValueError):
                resolve_output_path(
                    root, Path("sources/extracted/RUN-000001.txt"), "internal"
                )

    def test_output_cannot_escape_extraction_area(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            with self.assertRaises(ValueError):
                resolve_output_path(root, Path("outside.txt"), "public")


if __name__ == "__main__":
    unittest.main()
