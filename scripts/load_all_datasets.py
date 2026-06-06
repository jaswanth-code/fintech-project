import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("data/db/bluestock_mf.db")

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        df = pd.read_csv(os.path.join(folder, file))

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully")

conn.close()

print("\nAll datasets loaded into SQLite.")