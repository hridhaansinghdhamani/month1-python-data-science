# Week 4 — Data Visualization with Matplotlib and Seaborn

## Topics covered

This week uses Matplotlib to create figures and axes, and Seaborn to build statistical plots with less setup code. The charts are saved as image files so they can be reviewed or added to a report.

## Practical work

`visualize_sales.py` cleans the sample sales data and creates four plots:

1. **Histogram:** shows how net sales values are distributed across orders.
2. **Bar chart:** compares total net sales between cities.
3. **Scatter plot:** shows how order quantity relates to net sales, with colour used to distinguish categories.
4. **Correlation heatmap:** summarizes pairwise correlations between numeric columns.

## What I learned

A chart should answer a specific question rather than simply decorate a report. Histograms help inspect distributions, bar charts compare categories, scatter plots show relationships between two numeric variables, and heatmaps make a correlation matrix easier to scan. Correlation alone does not establish that one variable causes another.

## How to test

Install dependencies, then run `python week4_visualization/visualize_sales.py` from the repository root. The script saves PNG files in `week4_visualization/outputs/`. Open the images and write down two or three observations based on the actual plots before submitting.
