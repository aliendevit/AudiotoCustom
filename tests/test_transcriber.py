import unittest
from app.transcriber import Transcriber

class TestTranscriber(unittest.TestCase):
    def test_transcribe_empty(self):
        transcriber = Transcriber()
        result = transcriber.transcribe("tests/sample_silent.wav")
        self.assertIsInstance(result, str)