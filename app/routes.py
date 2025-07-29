from fastapi import APIRouter, UploadFile, File
from app.audio_handler import save_audio, convert_to_wav
from app.transcriber import Transcriber
from app.summarizer import summarize_text
from app.document_parser import parse_document
import os

router = APIRouter()

transcriber = Transcriber()

@router.post("/transcribe-audio")
async def transcribe_audio(file: UploadFile = File(...)):
    path = save_audio(file)
    wav_path = convert_to_wav(path)
    text = transcriber.transcribe(wav_path)
    summary = summarize_text(text)
    return {"transcript": text, "summary": summary}

@router.post("/summarize-pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    pdf_path = save_audio(file, file_ext=".pdf")
    text = parse_document(pdf_path)
    summary = summarize_text(text)
    return {"extracted_text": text, "summary": summary}
