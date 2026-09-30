# Command-Line Data Analysis Tool

A lightweight, command-line data analysis tool built with Python, Pandas, and Argparse[cite: 1]. This tool allows users to quickly inspect, filter, group, and run statistical analyses on any CSV dataset directly from the terminal without needing a graphical interface[cite: 1].

---

## Features

* **Dataset Summary**: View total rows, columns, data types, and missing values.
* **Statistical Reports**: Generate statistical summaries (mean, standard deviation, min, max, percentiles) for all numeric columns or a specific column[cite: 1].
* **Data Filtering**: Filter rows based on specific column values[cite: 1].
* **Data Grouping & Aggregation**: Group data by specific columns and perform aggregate functions (mean, sum, count, min, max)[cite: 1].
* **Robust Error Handling**: Automatically validates file existence and checks if requested columns exist in the dataset[cite: 1].

---

## Prerequisites

Make sure you have Python installed along with the required library:

```bash
pip install pandas
