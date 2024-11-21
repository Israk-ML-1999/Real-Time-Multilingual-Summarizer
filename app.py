import streamlit as st
from summarizer import detect_language, summarize_text

# Streamlit UI
st.title("Real-Time Multilingual Summarizer")

# User input
text = st.text_area("Enter the text to summarize:")

if st.button("Analyze"):
    if text.strip():
        # Detect language
        language = detect_language(text)
        st.write(f"Detected Language: **{language}**")
        
        # Summarize text
        summary = summarize_text(text)
        st.write("### Summary:")
        st.write(summary)
    else:
        st.error("Please enter some text to analyze.")
