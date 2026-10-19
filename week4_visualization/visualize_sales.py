"""Create a small set of charts from the sample sales dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "sales_sample.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    df = df.drop_duplicates(subset="order_id").dropna(
        subset=["city", "category", "units", "unit_price", "discount_pct"]
    )
    df = df[(df["units"] > 0) & (df["unit_price"] >= 0)].copy()
    df["gross_sales"] = df["units"] * df["unit_price"]
    df["net_sales"] = df["gross_sales"] * (1 - df["discount_pct"] / 100)

    sns.set_theme(style="whitegrid")

    # 1. Distribution of order values.
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(data=df, x="net_sales", bins=8, kde=True, color="steelblue", ax=ax)
    ax.set(title="Distribution of Net Sales per Order", xlabel="Net sales", ylabel="Number of orders")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "net_sales_histogram.png", dpi=150)
    plt.close(fig)

    # 2. Compare sales across cities.
    city_totals = df.groupby("city", as_index=False)["net_sales"].sum().sort_values("net_sales", ascending=False)
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(data=city_totals, x="city", y="net_sales", color="steelblue", ax=ax)
    ax.set(title="Net Sales by City", xlabel="City", ylabel="Total net sales")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "net_sales_by_city.png", dpi=150)
    plt.close(fig)

    # 3. Explore the relationship between units and net sales.
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.scatterplot(data=df, x="units", y="net_sales", hue="category", s=85, ax=ax)
    ax.set(title="Order Size and Net Sales", xlabel="Units in order", ylabel="Net sales")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "units_vs_net_sales.png", dpi=150)
    plt.close(fig)

    # 4. Correlation heatmap for numeric columns.
    numeric = df[["units", "unit_price", "discount_pct", "gross_sales", "net_sales"]]
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
    ax.set_title("Correlation Between Numeric Sales Features")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "sales_correlation_heatmap.png", dpi=150)
    plt.close(fig)

    print(f"Created 4 charts in: {OUTPUT_DIR}")
    print("Review the charts before submitting and include any observations you can explain.")

if __name__ == "__main__":
    main()
