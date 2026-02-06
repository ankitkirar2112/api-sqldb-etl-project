import json
from pathlib import Path

import requests as req

from src.config import API_URL, DATA_DIR, DATA_PATH

def authentication():
    pass

def extract_data_api():
    response = req.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()

def save_to_json(data, path=DATA_PATH):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(path)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
