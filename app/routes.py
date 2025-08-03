from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.summarizer import summarize_text

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/summarize", tags=["Summarization"])
async def summarize_endpoint(input_data: TextInput):
    text = input_data.text.strip()

    if not text:
        raise HTTPException(status_code=422, detail="⚠️ النص المدخل فارغ أو غير صالح.")

    summary = summarize_text(text)

    if summary.startswith("❌") or "حدث خطأ" in summary:
        raise HTTPException(status_code=500, detail=summary)

    return {"summary": summary}
