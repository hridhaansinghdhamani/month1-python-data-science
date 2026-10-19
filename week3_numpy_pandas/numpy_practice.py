"""Practise NumPy arrays, vectorized operations, and broadcasting."""
import numpy as np

def main():
    daily_sales = np.array([1200, 950, 1430, 1100, 1675], dtype=float)
    target = 1200

    print("Daily sales:", daily_sales)
    print("Mean:", round(float(np.mean(daily_sales)), 2))
    print("Days above target:", daily_sales > target)
    print("Sales after a 5% increase:", np.round(daily_sales * 1.05, 2))

    # Broadcasting adds each day's sales to a different adjustment value.
    adjustments = np.array([0, 50, 0, -25, 100], dtype=float)
    print("Adjusted sales:", daily_sales + adjustments)

if __name__ == "__main__":
    main()
