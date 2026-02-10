import sqlite3

def insert_raw_data(raw_json_data, table_name):
    # Connection to the SQLite database
    conn = sqlite3.connect('db/raw.db')
    cursor = conn.cursor()

    # Insert data into the specified table
    


