from pydub import AudioSegment
import os
from uuid import uuid4

UPLOAD_DIR = "data/input"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_audio(file, file_ext=".mp3") -> str:
    filename = f"{uuid4()}{file_ext}"
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(file.read())
    return path

def convert_to_wav(input_path: str) -> str:
    audio = AudioSegment.from_file(input_path)
    wav_path = input_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path