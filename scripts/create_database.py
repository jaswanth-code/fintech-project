import sqlite3
conn = sqlite3.connect("data/db/bluestock_mf.db")
print("Database created successfully")
conn.close()