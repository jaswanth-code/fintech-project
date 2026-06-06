import pandas as pd
import sqlite3

df = pd.read_csv("data/raw/01_fund_master.csv")

conn = sqlite3.connect("data/db/bluestock_mf.db")

df.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

print("fund_master loaded successfully")

conn.close()