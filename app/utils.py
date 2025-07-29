import re

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'[^؀-ۿ\s\d.,؟!"\']+', '', text)  # keep Arabic and common symbols
    return text.strip()