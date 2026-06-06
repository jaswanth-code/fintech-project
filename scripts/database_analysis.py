import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

print("\nFunds by Category")
query1 = """
SELECT category, COUNT(*) as total_funds
FROM '01_fund_master'
GROUP BY category
"""
print(pd.read_sql(query1, conn))

print("\nFunds by Risk Category")
query2 = """
SELECT risk_category, COUNT(*) as total_funds
FROM '01_fund_master'
GROUP BY risk_category
"""
print(pd.read_sql(query2, conn))

print("\nTop Fund Houses")
query3 = """
SELECT fund_house, COUNT(*) as total_funds
FROM '01_fund_master'
GROUP BY fund_house
ORDER BY total_funds DESC
"""
print(pd.read_sql(query3, conn))

conn.close()