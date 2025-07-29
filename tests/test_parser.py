import unittest
from app.document_parser import parse_document

class TestDocumentParser(unittest.TestCase):
    def test_parse_pdf(self):
        result = parse_document("tests/sample.pdf")
        self.assertTrue(isinstance(result, str))