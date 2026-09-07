# Simple Password Validator

A Python command-line application that validates passwords against standard security complexity requirements. This project was built to practice strings, conditional logic, loops, and basic input validation.

## 📝 Description

This script checks whether a given password meets basic security standards. Instead of printing actual passwords unnecessarily during interactive use, it utilizes Python's built-in `getpass` module to securely hide user input. 

## ✨ Features and Validation Rules

The program validates passwords against the following criteria:
* **Minimum Length:** Must be at least 8 characters long.
* **Uppercase Letter:** Must contain at least one uppercase character (`A-Z`).
* **Lowercase Letter:** Must contain at least one lowercase character (`a-z`).
* **Number:** Must contain at least one numeric digit (`0-9`).
* **Special Character:** Must contain at least one special character (e.g., `!@#$%^&*`).

## 🛠️ Tools Used

* **Python 3:** Core programming language.
* **`string` module:** Used to easily access a complete list of special characters via `string.punctuation`.
* **`getpass` module:** Used to mask password input in the terminal for enhanced security.

## 🚀 How to Run

1. Ensure you have Python 3 installed on your system.
2. Save the script as `password_validator.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Execute the script using the following command:

   ```bash
   python password_validator.py

   
