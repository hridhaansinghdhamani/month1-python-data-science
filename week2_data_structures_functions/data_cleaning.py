"""Clean a small list of order records using core Python structures."""
from pathlib import Path
import csv

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "sales_sample.csv"

def load_orders(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def clean_orders(rows):
    """Drop duplicate order IDs and rows with invalid/non-positive units."""
    cleaned = []
    seen_ids = set()

    for row in rows:
        order_id = row.get("order_id", "").strip()
        try:
            units = int(row.get("units", ""))
            price = float(row.get("unit_price", ""))
        except (TypeError, ValueError):
            continue

        if not order_id or order_id in seen_ids or units <= 0 or price < 0:
            continue

        seen_ids.add(order_id)
        cleaned.append({
            "order_id": order_id,
            "city": row.get("city", "").strip().title(),
            "category": row.get("category", "").strip().title(),
            "units": units,
            "unit_price": price,
        })
    return cleaned

def main():
    raw_rows = load_orders(DATA_FILE)
    cleaned_rows = clean_orders(raw_rows)
    print(f"Rows read: {len(raw_rows)}")
    print(f"Rows retained after validation: {len(cleaned_rows)}")
    print("First three cleaned records:")
    for row in cleaned_rows[:3]:
        print(row)

if __name__ == "__main__":
    main()
