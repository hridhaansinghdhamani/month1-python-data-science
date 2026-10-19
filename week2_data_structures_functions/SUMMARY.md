# Week 2 — Data Structures and Functions

## Topics covered

The exercises use lists for ordered collections, tuples for fixed groups of values, dictionaries for named fields, and sets to track unique items. They also practise defining functions, list comprehensions, `lambda`, `map`, and recursion.

## Practical work

- `functions_practice.py` includes reusable functions for sum of squares, threshold filtering, and factorial calculation.
- `data_cleaning.py` reads sample order records, skips duplicate order IDs, rejects invalid quantities or prices, and standardizes city and category names.

## What I learned

A function makes a repeated operation easier to test and reuse. A set is useful for checking whether an identifier has already appeared, while a dictionary keeps related fields together. Data cleaning also needs explicit rules: in this example, an order is retained only if its ID is present and unique, units are positive, and price is not negative.

## How to test

Run both scripts from the repository root. The sample sales file has ten records; the cleaning script reports the number read and retained. The supplied sample has no duplicates or invalid rows, so the retained count should match the input count.
