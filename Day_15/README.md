# Task 15: Shopping Bill Generator 🛒

Welcome to the **Shopping Bill Generator** project! This Python program is designed to accept product names, quantities, and prices from a user, perform essential financial calculations (subtotal, discounts, and taxes), and generate a clean, professionally formatted itemized bill.

---

## 🚀 Features
- **Interactive Product Entry:** Add multiple products dynamically with continuous input prompts until you type `'done'`.
- **Robust Error Handling:** Validates numerical inputs for quantities, prices, discounts, and taxes to prevent runtime crashes.
- **Modular Functions:** Logic is neatly split into dedicated functions for calculating subtotals, applying discounts, and computing taxes.
- **Formatted Itemized Output:** Automatically aligns columns to print a neat, professional receipt with currency formatting (`.2f`).

---

## 🛠️ Technologies Used
- **Language:** Python 3.x
- **Concepts Applied:** 
  - Lists and Dictionaries (Structured Data)
  - `while` loops & `try-except` blocks (Control Flow & Error Handling)
  - Functions & Calculations (Modular Programming)

---

## 📂 Code Structure
The script consists of modular functions designed to handle specific tasks:
1. `calculate_subtotal(items)`: Loops through the list of product dictionaries to calculate the raw subtotal.
2. `apply_discount(subtotal, discount_percentage)`: Computes the monetary discount value based on a given percentage.
3. `apply_tax(amount_after_discount, tax_percentage)`: Calculates the tax applied on the discounted amount.
4. `generate_bill()`: Manages user inputs, invokes the calculation functions, and prints the final formatted receipt layout.

---

## ⚙️ How to Run the Program

1. Ensure you have **Python 3.x** installed on your machine.
2. Clone or download the script file (e.g., `bill_generator.py`).
3. Open your terminal or command prompt and run:
   ```bash
   python bill_generator.py
