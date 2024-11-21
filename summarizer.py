from transformers import pipeline 
from langdetect import detect 

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "unknown"

def summarize_text(text, max_length=130, min_length=30):
    # Load a summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
