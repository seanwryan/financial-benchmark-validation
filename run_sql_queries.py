import sqlite3

# Connect to SQLite database
db_path = "data/outputs/benchmark_data.db"
conn = sqlite3.connect(db_path)

# Define SQL queries
queries = {
    "Missing Data Check": """
        SELECT COUNT(*) AS missing_rows, column_name
        FROM (
            SELECT 'Open' AS column_name, COUNT(*) AS missing_rows FROM reconciled_data WHERE Open IS NULL
            UNION ALL
            SELECT 'High', COUNT(*) FROM reconciled_data WHERE High IS NULL
            UNION ALL
            SELECT 'Low', COUNT(*) FROM reconciled_data WHERE Low IS NULL
            UNION ALL
            SELECT 'Close', COUNT(*) FROM reconciled_data WHERE Close IS NULL
            UNION ALL
            SELECT 'Volume', COUNT(*) FROM reconciled_data WHERE Volume IS NULL
        )
        WHERE missing_rows > 0;
    """,
    "Outliers Check": """
        SELECT column_name, COUNT(*) AS outlier_rows
        FROM (
            SELECT 'Open' AS column_name, COUNT(*) AS outlier_rows FROM reconciled_data WHERE Open < 5300 OR Open > 6000
            UNION ALL
            SELECT 'High', COUNT(*) FROM reconciled_data WHERE High < 5400 OR High > 6100
            UNION ALL
            SELECT 'Low', COUNT(*) FROM reconciled_data WHERE Low < 5200 OR Low > 5900
            UNION ALL
            SELECT 'Close', COUNT(*) FROM reconciled_data WHERE Close < 5300 OR Close > 6000
            UNION ALL
            SELECT 'Volume', COUNT(*) FROM reconciled_data WHERE Volume < 100000000 OR Volume > 7000000000
        )
        WHERE outlier_rows > 0
        GROUP BY column_name;
    """,
}

# Execute queries and display results
for query_name, query in queries.items():
    print(f"\n{query_name}")
    cursor = conn.execute(query)
    for row in cursor.fetchall():
        print(row)

conn.close()