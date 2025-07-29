import whisper
import os
from pathlib import Path

MODEL_PATH = "models/whisper"

class Transcriber:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: str) -> str:
        result = self.model.transcribe(audio_path, language="ar")
        return result.get("text", "")
