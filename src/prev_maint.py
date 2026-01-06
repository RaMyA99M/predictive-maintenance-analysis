import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect(
    r"C:\Users\ramya\Desktop\SQL projects\predictive_maintenance.db"
)

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)
print(tables)

#Example query
query = """
SELECT
    type,
    COUNT(*) as total, 
    SUM(target) as failures,
    ROUND(100 * SUM(target) / COUNT(*), 2) as failure_rate_pct
FROM predictive_maintenance
GROUP BY type;
"""

df = pd.read_sql_query(query, conn)
print(df)

# Standardize column names
df.columns = df.columns.str.lower()

import matplotlib.pyplot as plt

plt.bar(df["type"], df["failure_rate_pct"])
plt.ylabel("Failure Rate (%)")
plt.xlabel("Machine Type")
plt.title("Failure Rate by Machine Type")
plt.show()

plt.savefig("figures/failure_rate_by_type.png", bbox_inches="tight")
