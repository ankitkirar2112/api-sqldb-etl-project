
import sqlite3

def insert_raw_data(raw_json_data, table_name):
    try:
        # Connection to the SQLite database
        conn = sqlite3.connect('db/raw.db')
        cursor = conn.cursor()

        # Create the table ddl dynamically based on data 
        sample = raw_json_data[0] if isinstance(raw_json_data,list) else raw_json_data
        columns = sample.keys()
        crt_col =  ', '.join([f"{col} TEXT" for col in columns])
        table_ddl = f"CREATE TABLE IF NOT EXISTS {table_name} ({crt_col})"
        cursor.execute(table_ddl)
        
        # Preparing Insert Statement
        column_name = ', '.join(columns)
        placeholder = ', '.join(["?" for i in columns])
        insert_query = f"INSERT INTO {table_name} ({column_name}) VALUES({placeholder})"

        
        

        # Insert data into the specified table
        records = [raw_json_data] if not(isinstance(raw_json_data,list)) else raw_json_data
        for row in records:
            values = [str(row[col]) for col in columns]
            cursor.execute(insert_query, values)

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# insert_raw_data("src\\extract\\data_files\\product.json",'product')