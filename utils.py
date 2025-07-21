import re

def clean_text(text):
    text = re.sub(r'<[^>]*?>', '', text)  # Remove HTML tags
    text = re.sub(r'http\S+', '', text)   # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)      # Normalize whitespace
    return text.strip()
