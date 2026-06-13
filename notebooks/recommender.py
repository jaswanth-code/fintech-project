import pandas as pd

def recommend_funds(risk_level, fund_stats):

    filtered = fund_stats[
        fund_stats["risk_grade"] == risk_level
    ]

    return filtered.sort_values(
        "sharpe",
        ascending=False
    ).head(3)


if __name__ == "__main__":
    print("Fund Recommender Module Loaded")