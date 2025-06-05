import json
import os

QUESTIONS_FILE = 'questions.json'


def load_questions():
    """Load list of questions from QUESTIONS_FILE if it exists."""
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_questions(qs):
    """Save list of questions to QUESTIONS_FILE."""
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2)
