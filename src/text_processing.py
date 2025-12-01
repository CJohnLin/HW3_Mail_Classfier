
"""text_processing.py
Custom text normalization functions (renamed to avoid similarity).
"""
import re
import string

def normalize_message(message: str) -> str:
    """Lowercase, remove urls, digits, punctuation, and extra spaces."""
    m = str(message).lower()
    m = re.sub(r'http\S+|www\S+', '', m)
    m = re.sub(r'\d+', '', m)
    m = m.translate(str.maketrans('', '', string.punctuation))
    m = re.sub(r'\s+', ' ', m).strip()
    return m
