"""Summarize a week's temperature readings from the sample CSV."""
from pathlib import Path
import csv

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "daily_temperatures.csv"

def main():
    readings = []
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                readings.append((row["day"], float(row["temperature_c"])))
            except (ValueError, KeyError):
                # Ignore rows that do not contain a usable temperature.
                continue

    if not readings:
        print("No valid temperature readings were found.")
        return

    values = [temperature for _, temperature in readings]
    hottest_day, hottest_temp = max(readings, key=lambda item: item[1])
    coolest_day, coolest_temp = min(readings, key=lambda item: item[1])

    print(f"Readings processed: {len(values)}")
    print(f"Average temperature: {sum(values) / len(values):.1f}°C")
    print(f"Hottest day: {hottest_day} ({hottest_temp:.1f}°C)")
    print(f"Coolest day: {coolest_day} ({coolest_temp:.1f}°C)")

if __name__ == "__main__":
    main()
