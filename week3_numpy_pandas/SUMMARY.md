# Week 3 — NumPy and Pandas for Data Manipulation

## Topics covered

NumPy was used for arrays, calculations across an array, boolean comparisons, and broadcasting. Pandas was used to load a CSV into a DataFrame, inspect missing values, remove duplicate IDs, filter invalid records, create calculated columns, and group data for summaries.

## Practical work

- `numpy_practice.py` calculates a mean, checks which values meet a target, applies a percentage increase, and demonstrates broadcasting with an adjustment array.
- `pandas_analysis.py` checks the shape and missing values of the sales dataset, validates rows, calculates gross sales and net sales after discount, and summarizes net sales by city and category.

## What I learned

Array operations can apply a calculation to many values without writing a loop for every element. In Pandas, a DataFrame makes it easier to inspect and transform tabular data. Grouping provides a compact way to compare totals across categories. The sales calculations in this exercise use `units × unit_price` for gross sales and subtract the percentage discount to estimate net sales.

## How to test

Install dependencies with `pip install -r requirements.txt`, then run both scripts from the repository root. The scripts use the provided sample CSV and print their results in the terminal.
