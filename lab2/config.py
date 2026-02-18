import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / 'TOKEN.txt', 'r') as file:
    TOKEN = file.read()
with open(BASE_DIR / 'headers/texts.json', 'r', encoding='utf-8') as text_json:
    TEXTS = json.load(text_json)