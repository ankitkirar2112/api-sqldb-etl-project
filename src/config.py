from pathlib import Path

API_URL = "https://fakestoreapi.com/products"
BASE_DIR = Path("api-sqldb-etl-project").resolve()
DATA_DIR = BASE_DIR / "data"
DATA_PATH = DATA_DIR / "products.json"
DB_PATH = BASE_DIR / "db" / "products.db"
