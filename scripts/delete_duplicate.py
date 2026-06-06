import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE fund_master")

conn.commit()

print("fund_master table deleted")

conn.close()