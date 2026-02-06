import json
import sqlite3
from pathlib import Path

from src.config import DB_PATH


class Load:
    def __init__(self, db_path=DB_PATH):
        self.db_path = Path(db_path)

    def _connect(self):
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                \"\"\"
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    price REAL,
                    description TEXT,
                    category TEXT,
                    image TEXT,
                    rating_rate REAL,
                    rating_count INTEGER
                )
                \"\"\"
            )
            connection.commit()

    def load_from_json(self, json_path):
        json_path = Path(json_path)
        with json_path.open(\"r\", encoding=\"utf-8\") as handle:
            data = json.load(handle)

        self.create_table()
        with self._connect() as connection:
            cursor = connection.cursor()
            for item in data:
                rating = item.get(\"rating\", {}) or {}
                cursor.execute(
                    \"\"\"
                    INSERT INTO products (
                        id, title, price, description, category, image, rating_rate, rating_count
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        title=excluded.title,
                        price=excluded.price,
                        description=excluded.description,
                        category=excluded.category,
                        image=excluded.image,
                        rating_rate=excluded.rating_rate,
                        rating_count=excluded.rating_count
                    \"\"\"
                    ,
                    (
                        item.get(\"id\"),
                        item.get(\"title\"),
                        item.get(\"price\"),
                        item.get(\"description\"),
                        item.get(\"category\"),
                        item.get(\"image\"),
                        rating.get(\"rate\"),
                        rating.get(\"count\"),
                    ),
                )
            connection.commit()
