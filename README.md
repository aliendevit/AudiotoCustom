# Voice to Law – Arabic Legal Summarizer

## 🚀 Goal
Upload Arabic voice or PDF → Summarize into formal legal Arabic.

## 📦 Tech Stack
- FastAPI for backend
- Streamlit for UI
- Whisper for Arabic speech-to-text
- HuggingFace models for Arabic summarization
- pdfminer, PyMuPDF or OCR (tesserocr) for PDF/scan parsing

## 📁 Project Structure
- `app/`: Logic for transcription, summarization, parsing
- `ui/`: Streamlit UI
- `models/`: Local/remote NLP models
- `data/`: Input/output files
- `tests/`: Unit tests
- `run.py`: FastAPI entry
