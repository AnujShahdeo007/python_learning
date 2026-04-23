import mysql.connector
import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/db_config.yaml')

with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)
db_conf = config['mysql']

# Connect to MySQL server (without specifying database)
conn = mysql.connector.connect(
    host=db_conf['host'],
    port=db_conf['port'],
    user=db_conf['user'],
    password=db_conf['password']
)
cursor = conn.cursor()

# Create database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_conf['database']}")

# Use the database
cursor.execute(f"USE {db_conf['database']}")

# Create source_table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS source_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    value INT
)
''')

# Insert sample data if table is empty
cursor.execute("SELECT COUNT(*) FROM source_table")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO source_table (id, name, value) VALUES (%s, %s, %s)",
        [
            (1, 'Alice', 100),
            (2, 'Bob', 200),
            (3, 'Charlie', 300)
        ]
    )
    conn.commit()

cursor.close()
conn.close()
print("Database and table setup complete.")
