import unittest
from app.summarizer import summarize_text

class TestSummarizer(unittest.TestCase):
    def test_summarize_text(self):
        input_text = """وزارة الداخلية أعلنت اليوم عن خطة أمنية جديدة لحماية المواطنين خلال العطلة."""
        result = summarize_text(input_text)
        self.assertTrue(isinstance(result, str) and len(result) > 0)