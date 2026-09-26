# Configuration-Driven ETL Pipeline

A lightweight, automated ETL (Extract, Transform, Load) pipeline built in Python. All pipeline parameters—including data sources, validation criteria, transformation rules, and output destinations—are externalized and controlled entirely through a JSON configuration file.

---

## Features

- **Configuration-Driven Architecture:** Modify input paths, transformations, and output targets without editing Python code.
- **Stage Isolation & Testability:** Independent methods for extraction, validation, transformation, and loading.
- **Data Validation & Cleaning:** Enforces required schemas and non-null constraints before transformations execute.
- **Auditing & Logging:** Captures record counts, dropped rows, execution timestamps, and pipeline failures into a structured log file.

---

## Project Structure

```text
├── pipeline_config.json   # Central configuration file
├── etl_pipeline.py        # Core ETL pipeline implementation
├── raw_data.csv           # Input source dataset
├── final_data.csv         # Generated output dataset
├── pipeline.log           # Output runtime logs
└── README.md              # Project documentation
