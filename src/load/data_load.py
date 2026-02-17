import json
import sqlite3

def insert_raw_data(raw_json_data, table_name):
    try:
        # Connection to the SQLite database
        conn = sqlite3.connect('db/raw.db')
        cursor = conn.cursor()

        # Insert data into the specified table
        cursor.execute(f"INSERT INTO {table_name} (data) VALUES (?)", (json.dumps(raw_json_data),))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# insert_raw_data("src\\extract\\data_files\\product.json",'product')