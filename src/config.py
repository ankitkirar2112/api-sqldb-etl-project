from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / 'db'
DATA_DIR = BASE_DIR / 'src' / 'extract' / 'data_files'
