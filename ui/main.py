import streamlit as st
import requests
from ui.components import upload_file_section, display_output

API_URL_AUDIO = "http://localhost:8000/transcribe-audio"
API_URL_PDF = "http://localhost:8000/summarize-pdf"

st.set_page_config(page_title="Voice to Law", layout="centered")
st.title("⚖️ Voice to Law - Arabic Legal Summarizer")

uploaded_file = upload_file_section()

if uploaded_file:
    file_type = uploaded_file.type
    with st.spinner("Processing..."):
        files = {"file": (uploaded_file.name, uploaded_file, file_type)}
        if "audio" in file_type:
            response = requests.post(API_URL_AUDIO, files=files)
            result = response.json()
            display_output(transcript=result.get("transcript"), summary=result.get("summary"))
        elif "pdf" in file_type:
            response = requests.post(API_URL_PDF, files=files)
            result = response.json()
            display_output(transcript=result.get("extracted_text"), summary=result.get("summary"))
