import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/02_nav_history.csv")

# Filter one fund
fund = df[df["amfi_code"] == 119551].copy()

# Convert date column
fund["date"] = pd.to_datetime(fund["date"])

plt.figure(figsize=(10,5))
plt.plot(fund["date"], fund["nav"])

plt.title("SBI Bluechip NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.grid(True)

plt.show()