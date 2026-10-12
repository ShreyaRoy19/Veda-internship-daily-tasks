import json
import os
from datetime import datetime

DATA_FILE = "expense_tracker_data.json"


def load_data():
    """Load expenses and budgets from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return {"expenses": [], "budgets": {}}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read data file. Initializing empty dataset.")
        return {"expenses": [], "budgets": {}}


def save_data(data):
    """Save expenses and budgets to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")


def get_valid_date(prompt="Enter date (YYYY-MM-DD) or press Enter for today: "):
    """Prompt and validate date input."""
    while True:
        entry = input(prompt).strip()
        if not entry:
            return datetime.now().strftime("%Y-%m-%d")
        try:
            valid_date = datetime.strptime(entry, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD (e.g., 2026-05-15).")


def get_valid_amount(prompt="Enter amount: "):
    """Prompt and validate positive numerical amount."""
    while True:
        entry = input(prompt).strip()
        try:
            amount = float(entry)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid number. Please enter a valid decimal or integer.")


def get_non_empty_string(prompt):
    """Ensure user input is not blank."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("This field cannot be empty.")


def add_expense(data):
    """Add a new expense record."""
    print("\n--- Add New Expense ---")
    date_str = get_valid_date()
    category = get_non_empty_string("Enter category (e.g., Food, Travel, Utilities): ").capitalize()
    amount = get_valid_amount()
    description = input("Enter description (optional): ").strip()

    next_id = max([exp["id"] for exp in data["expenses"]], default=0) + 1

    expense = {
        "id": next_id,
        "date": date_str,
        "category": category,
        "amount": amount,
        "description": description or "N/A"
    }

    data["expenses"].append(expense)
    save_data(data)
    print(f"Expense #{next_id} successfully recorded!")


def view_expenses(expenses):
    """Display a list of expenses in a clean table format."""
    if not expenses:
        print("No expense records found.")
        return

    print("\n" + "-" * 75)
    print(f"{'ID':<6}{'Date':<12}{'Category':<16}{'Amount ($)':<12}{'Description'}")
    print("-" * 75)
    for exp in expenses:
        print(f"{exp['id']:<6}{exp['date']:<12}{exp['category']:<16}{exp['amount']:<12.2f}{exp['description']}")
    print("-" * 75)


def edit_expense(data):
    """Edit an existing expense record."""
    view_expenses(data["expenses"])
    if not data["expenses"]:
        return

    try:
        target_id = int(input("\nEnter the ID of the expense to edit: "))
    except ValueError:
        print("Invalid ID format.")
        return

    for exp in data["expenses"]:
        if exp["id"] == target_id:
            print("\nLeave blank to keep existing value.")
            
            new_date = input(f"New Date (Current: {exp['date']}): ").strip()
            if new_date:
                try:
                    exp["date"] = datetime.strptime(new_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format; keeping original date.")

            new_cat = input(f"New Category (Current: {exp['category']}): ").strip()
            if new_cat:
                exp["category"] = new_cat.capitalize()

            new_amt = input(f"New Amount (Current: {exp['amount']}): ").strip()
            if new_amt:
                try:
                    amt_val = float(new_amt)
                    if amt_val > 0:
                        exp["amount"] = round(amt_val, 2)
                except ValueError:
                    print("Invalid amount format; keeping original amount.")

            new_desc = input(f"New Description (Current: {exp['description']}): ").strip()
            if new_desc:
                exp["description"] = new_desc

            save_data(data)
            print("Expense updated successfully.")
            return

    print(f"Expense with ID {target_id} not found.")


def delete_expense(data):
    """Delete an expense record by ID."""
    view_expenses(data["expenses"])
    if not data["expenses"]:
        return

    try:
        target_id = int(input("\nEnter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID format.")
        return

    initial_count = len(data["expenses"])
    data["expenses"] = [exp for exp in data["expenses"] if exp["id"] != target_id]

    if len(data["expenses"]) < initial_count:
        save_data(data)
        print(f"Expense #{target_id} deleted successfully.")
    else:
        print(f"Expense with ID {target_id} not found.")


def search_and_filter(data):
    """Filter records by category, date range, or keyword."""
    print("\n--- Search and Filter ---")
    print("1. Filter by Category")
    print("2. Filter by Date Range")
    print("3. Search by Description Keyword")
    choice = input("Select an option (1-3): ").strip()

    if choice == "1":
        cat = input("Enter category name: ").strip().capitalize()
        filtered = [exp for exp in data["expenses"] if exp["category"] == cat]
        view_expenses(filtered)
    elif choice == "2":
        start = get_valid_date("Enter start date (YYYY-MM-DD): ")
        end = get_valid_date("Enter end date (YYYY-MM-DD): ")
        filtered = [exp for exp in data["expenses"] if start <= exp["date"] <= end]
        view_expenses(filtered)
    elif choice == "3":
        keyword = input("Enter search keyword: ").strip().lower()
        filtered = [exp for exp in data["expenses"] if keyword in exp["description"].lower()]
        view_expenses(filtered)
    else:
        print("Invalid choice.")


def manage_budgets(data):
    """Set monthly spending budget limits per category."""
    print("\n--- Set Monthly Budget ---")
    month = input("Enter month (YYYY-MM, e.g., 2026-05): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format. Must be YYYY-MM.")
        return

    category = get_non_empty_string("Enter category: ").capitalize()
    limit = get_valid_amount("Enter budget limit amount: ")

    if month not in data["budgets"]:
        data["budgets"][month] = {}

    data["budgets"][month][category] = limit
    save_data(data)
    print(f"Budget for {category} in {month} set to ${limit:.2f}.")


def generate_summary(data):
    """Summarize expenses by total, category, and monthly budget comparison."""
    if not data["expenses"]:
        print("No expenses to summarize.")
        return

    month = input("\nEnter month for summary (YYYY-MM, e.g., 2026-05): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format.")
        return

    month_expenses = [exp for exp in data["expenses"] if exp["date"].startswith(month)]
    if not month_expenses:
        print(f"No records found for {month}.")
        return

    category_totals = {}
    total_spent = 0.0

    for exp in month_expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + exp["amount"]
        total_spent += exp["amount"]

    print(f"\n================ Summary for {month} ================")
    print(f"Total Spent: ${total_spent:.2f}\n")
    print(f"{'Category':<18}{'Spent ($)':<12}{'Budget ($)':<12}{'Status'}")
    print("-" * 55)

    month_budgets = data["budgets"].get(month, {})
    for cat, spent in category_totals.items():
        budget = month_budgets.get(cat, 0.0)
        if budget > 0:
            status = "EXCEEDED" if spent > budget else f"OK (${budget - spent:.2f} left)"
            budget_str = f"{budget:.2f}"
        else:
            status = "No limit set"
            budget_str = "N/A"

        print(f"{cat:<18}{spent:<12.2f}{budget_str:<12}{status}")
    print("=" * 55)


def main():
    data = load_data()

    while True:
        print("\n==========================================")
        print("    PERSONAL EXPENSE & BUDGET TRACKER     ")
        print("==========================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Search & Filter Expenses")
        print("6. Set Monthly Budget")
        print("7. View Monthly Spending Summary")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data["expenses"])
        elif choice == "3":
            edit_expense(data)
        elif choice == "4":
            delete_expense(data)
        elif choice == "5":
            search_and_filter(data)
        elif choice == "6":
            manage_budgets(data)
        elif choice == "7":
            generate_summary(data)
        elif choice == "8":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 8.")


if __name__ == "__main__":
    main()
