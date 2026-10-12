# Personal Expense & Budget Tracker

A terminal-based Python tool to record daily transactions, manage category-level monthly budgets, filter records, and track financial habits.

## Features
- **CRUD Operations**: Add, edit, view, and delete daily expenses.
- **Monthly Budgets**: Set budgets per category for specific months and monitor overspending alerts.
- **Search & Filter**: Lookup transactions by category, custom date range, or keyword.
- **Robust Validation**: Ensures valid dates , non-negative floats, and non-empty categories.
- **Data Persistence**: Uses a clean JSON structure to store transaction and budget data across sessions.

## Project Structure
- `tracker.py`: Main executable file containing all application logic and menu interface.
- `expense_tracker_data.json`: Local data store automatically generated at runtime.

## How to Run
1. Make sure Python 3.8+ is installed:
   ```bash
   python --version
