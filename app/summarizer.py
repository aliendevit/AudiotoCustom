from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="UBC-NLP/araT5-base", tokenizer="UBC-NLP/araT5-base")

def summarize_text(text: str, max_length=200, min_length=50) -> str:
    if not text.strip():
        return ""
    summary = summarizer_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']