# Temperature Converter

A simple Python command-line utility to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**. This project is part of a Python programming track (Level 1, Task 14) focusing on functions, arithmetic operations, and input validation.

## Features

- **Multi-directional conversion:** Convert between Celsius, Fahrenheit, and Kelvin seamlessly.
- **Input validation:** Handles non-numeric inputs gracefully and checks for physically meaningful values (e.g., preventing temperatures below absolute zero).
- **Formatted output:** Results are cleanly formatted to two decimal places.

## Conversion Formulas

- **Celsius to Fahrenheit:** $(C \times \frac{9}{5}) + 32$
- **Celsius to Kelvin:** $C + 273.15$
- **Fahrenheit to Celsius:** $(F - 32) \times \frac{5}{9}$
- **Kelvin to Celsius:** $K - 273.15$

## Requirements

- Python 3.x

## How to Run

1. Open your terminal or VS Code.
2. Run the script using Python:
   ```bash
   python temperature_converter.py
