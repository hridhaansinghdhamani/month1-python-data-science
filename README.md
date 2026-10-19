# Month 1: Python Basics and Data Manipulation

A four-week practice repository covering Python fundamentals, data structures, data cleaning, NumPy, Pandas, and data visualization.

## What is included

- **Week 1 — Python fundamentals:** variables, input/output, operators, conditions, loops, a calculator, a temperature converter, and a temperature-summary script.
- **Week 2 — Data structures and functions:** lists, tuples, dictionaries, sets, reusable functions, lambda expressions, recursion, list comprehensions, and a small data-cleaning task.
- **Week 3 — NumPy and Pandas:** arrays, vectorized operations, missing-value handling, indexing, grouping, and summary statistics.
- **Week 4 — Visualization:** Matplotlib and Seaborn plots, including histograms, scatter plots, box plots, and a correlation heatmap.

## Folder structure

```text
month1-python-data-science/
├── README.md
├── requirements.txt
├── data/
│   ├── daily_temperatures.csv
│   └── sales_sample.csv
├── week1_python_fundamentals/
│   ├── calculator.py
│   ├── temperature_converter.py
│   ├── temperature_summary.py
│   └── SUMMARY.md
├── week2_data_structures_functions/
│   ├── data_cleaning.py
│   ├── functions_practice.py
│   └── SUMMARY.md
├── week3_numpy_pandas/
│   ├── numpy_practice.py
│   ├── pandas_analysis.py
│   └── SUMMARY.md
└── week4_visualization/
    ├── visualize_sales.py
    └── SUMMARY.md
```

## Setup

Use Python 3.10 or newer. From the repository folder, create and activate a virtual environment if desired.

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```powershell
py -m venv .venv
.venv\Scripts\activate
```

Install the packages used in Weeks 3–4:

```bash
pip install -r requirements.txt
```

## Run the scripts

Run commands from the repository root, for example:

```bash
python week1_python_fundamentals/temperature_summary.py
python week2_data_structures_functions/data_cleaning.py
python week3_numpy_pandas/pandas_analysis.py
python week4_visualization/visualize_sales.py
```

The visualization script saves charts to `week4_visualization/outputs/`. It creates that folder if it does not exist.

## Dataset note

The CSV files in `data/` are small, illustrative practice datasets created for this repository. They are not real customer or client records. The examples are intended to demonstrate basic data-processing steps and can be replaced with a dataset approved for your assignment.

## Learning outcomes

By the end of this month, the aim is to be comfortable writing small Python scripts, organizing logic into functions, cleaning tabular data, calculating grouped summaries, and selecting plots that help explain patterns in a dataset.

## Before submitting

- Run each script locally and check the output.
- Open the saved charts and confirm they look correct.
- Update the repository owner/details if required by your course.
- Add only work you understand and can explain. If your instructor expects screenshots or a specific format, include those separately.
