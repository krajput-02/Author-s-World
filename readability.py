# Readability calculations using the textstat library (works offline).
import re
import textstat


def split_sentences(text):
    """Split text into sentences."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def get_level(score):
    """Turn the Flesch score (higher = easier) into a difficulty label."""
    if score >= 80:
        return "Very Easy", "#16a34a"
    if score >= 60:
        return "Easy", "#65a30d"
    if score >= 50:
        return "Moderate", "#d97706"
    if score >= 30:
        return "Difficult", "#ea580c"
    return "Very Difficult", "#dc2626"


def analyze_text(text):
    """Return word count, sentence count, average sentence length, score, level."""
    words = textstat.lexicon_count(text)
    sentences = max(textstat.sentence_count(text), 1)
    score = round(textstat.flesch_reading_ease(text), 1)
    level, color = get_level(score)
    return {
        "words": words,
        "sentences": sentences,
        "avg_length": round(words / sentences, 1),
        "score": score,
        "level": level,
        "color": color,
    }
