# Student Grade Calculator

## 📝 Description
This project is a Python-based console application that accepts marks for multiple subjects, calculates the total marks and percentage, and assigns a final grade based on predefined conditions. 

It was developed as part of a Python Programming Track task (Level 1 - Day 4).

## 🎯 Objective
To practice and demonstrate proficiency in:
* Using conditional statements (`if-elif-else`).
* Performing basic arithmetic operations.
* Implementing robust user input validation (`try-except`, `while` loops).

## ✨ Features
* **Dynamic Subject Count:** Allows the user to specify how many subjects they want to calculate grades for.
* **Strict Input Validation:** 
  * Ensures users enter valid numbers (handles non-integer/non-float inputs gracefully).
  * Enforces an allowed range (0 - 100) for subject marks.
* **Optimized Calculations:** Accumulates total marks in a loop and calculates the final percentage only once to avoid unnecessary repetition.
* **Clear Grade Boundaries:** Uses straightforward grading criteria:
  * `90% - 100%`: A
  * `80% - 89.99%`: B
  * `70% - 79.99%`: C
  * `60% - 69.99%`: D
  * `50% - 59.99%`: E
  * `< 50%`: F

## 🚀 How to Run
1. Ensure you have Python 3.x installed on your system.
2. Download or copy the `grade_calculator.py` script.
3. Open your terminal or command prompt.
4. Run the script using the following command:
   ```bash
   python grade_calculator.py
