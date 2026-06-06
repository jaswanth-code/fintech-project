import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

query = """
SELECT category, COUNT(*) as total_funds
FROM '01_fund_master'
GROUP BY category
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()