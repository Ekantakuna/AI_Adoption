import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.extract_pptx_text import extract_pptx_content


class ExtractPptxTextTests(unittest.TestCase):
    def test_extracts_text_in_numeric_slide_order(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.pptx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr(
                    "ppt/slides/slide10.xml",
                    '<p:sld xmlns:p="urn:p" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:t>Ten</a:t></p:sld>',
                )
                archive.writestr(
                    "ppt/slides/slide2.xml",
                    '<p:sld xmlns:p="urn:p" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:t>Two</a:t><a:t>Details</a:t></p:sld>',
                )
            self.assertEqual(
                extract_pptx_content(path),
                "=== Slide 2 ===\nTwo\nDetails\n\n=== Slide 10 ===\nTen\n",
            )

    def test_rejects_archive_without_slides(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.pptx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("docProps/core.xml", "<core />")
            with self.assertRaises(ValueError):
                extract_pptx_content(path)


if __name__ == "__main__":
    unittest.main()
