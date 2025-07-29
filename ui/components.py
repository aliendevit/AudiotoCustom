import streamlit as st

def upload_file_section():
    st.markdown("## 📤 Upload Audio or PDF")
    return st.file_uploader("Choose a file", type=["mp3", "wav", "pdf"])

def display_output(transcript=None, summary=None):
    if transcript:
        st.markdown("### 🗣️ Transcript")
        st.text_area("", transcript, height=150)
    if summary:
        st.markdown("### 📜 Legal Summary")
        st.text_area("", summary, height=150)