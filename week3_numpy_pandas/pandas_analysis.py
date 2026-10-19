"""Clean and summarize the sample sales dataset with Pandas."""
from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "sales_sample.csv"

def main():
    df = pd.read_csv(DATA_FILE)
    print("Initial shape:", df.shape)
    print("\nMissing values by column:")
    print(df.isna().sum())

    # Remove duplicate order IDs, then drop rows missing required fields.
    df = df.drop_duplicates(subset="order_id")
    required = ["order_id", "city", "category", "units", "unit_price"]
    df = df.dropna(subset=required)
    df = df[(df["units"] > 0) & (df["unit_price"] >= 0)].copy()

    df["gross_sales"] = df["units"] * df["unit_price"]
    df["discount_amount"] = df["gross_sales"] * df["discount_pct"] / 100
    df["net_sales"] = df["gross_sales"] - df["discount_amount"]

    print("\nCleaned data preview:")
    print(df.head().to_string(index=False))
    print("\nSummary statistics:")
    print(df[["units", "unit_price", "net_sales"]].describe().round(2))
    print("\nNet sales by city:")
    print(df.groupby("city")["net_sales"].sum().sort_values(ascending=False).round(2))
    print("\nNet sales by category:")
    print(df.groupby("category")["net_sales"].sum().sort_values(ascending=False).round(2))

if __name__ == "__main__":
    main()
