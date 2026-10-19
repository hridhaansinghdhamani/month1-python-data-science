# Week 1 — Introduction to Python Programming

## Topics covered

This week focused on the building blocks used in small Python programs: variables, common data types, arithmetic and comparison operators, input/output, `if`/`elif`/`else`, and `for` loops. The scripts use these ideas to solve simple tasks instead of keeping the concepts separate from practice.

## Practical work

- `calculator.py` reads two numbers and an operator, then performs the selected calculation. It also handles invalid numeric input and division by zero.
- `temperature_converter.py` converts Celsius to Fahrenheit and Fahrenheit to Celsius using separate functions.
- `temperature_summary.py` reads the provided CSV file and reports the average, hottest day, and coolest day.

## What I learned

I practised converting text input into numeric values, checking conditions before performing an operation, and using a loop to process records. I also learned that small checks—such as validating input and checking whether a list is empty—make a script more reliable.

## How to test

Run each script from the repository root. The calculator and converter ask for input. The summary script reads `data/daily_temperatures.csv`; with the supplied sample data, it should process seven readings.
