import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io
import os

def parse_document(path: str) -> str:
    text = ""
    if path.endswith(".pdf"):
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
            if not text.strip():  # fallback to OCR
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                text += pytesseract.image_to_string(img, lang='ara')
    return text.strip()