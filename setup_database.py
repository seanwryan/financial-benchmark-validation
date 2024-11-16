import sqlite3
import pandas as pd
import os

# Load reconciled data
reconciled_path = "data/outputs/reconciled_data.csv"
if not os.path.exists(reconciled_path):
    raise FileNotFoundError(f"{reconciled_path} not found.")

data = pd.read_csv(reconciled_path)

# Connect to SQLite database (creates a new file if it doesn't exist)
db_path = "data/outputs/benchmark_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table and insert the reconciled data
data.to_sql("reconciled_data", conn, if_exists="replace", index=False)

print(f"Database created at {db_path}")
conn.close()