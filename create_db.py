import sqlite3
import pandas as pd

# Connect to SQLite
conn = sqlite3.connect("pollution.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE complaints (
    id INTEGER PRIMARY KEY,
    name TEXT,
    area TEXT,
    pollution_type TEXT,
    description TEXT,
    date TEXT
)
""")

# Read CSV
df = pd.read_csv("Complaints.csv", header=None)

df.columns = [
    "id",
    "name",
    "area",
    "pollution_type",
    "description",
    "date"
]

# Insert data
df.to_sql("complaints", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Database created successfully!")