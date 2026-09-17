# Detailed Explanation: Menu-Driven Bank Account Simulator

This document provides a comprehensive breakdown of the Python code written for the **Bank Account Simulator** task. It covers architectural design, state management, validation logic, and execution flow.

---

## 1. Architectural Design & Modularization

The program avoids a monolithic structure by breaking down responsibilities into distinct, reusable functions. This follows standard software engineering practices (separation of concerns):

* `show_menu()`: Renders the interface options for the user.
* `check_balance(balance)`: Handles read-only operations on the account state.
* `deposit(balance, history)`: Manages incoming funds and appends to the log.
* `withdraw(balance, history)`: Validates and subtracts funds safely.
* `show_history(history)`: Iterates through the transaction list to present a chronological summary.
* `main()`: Acts as the central controller, orchestrating the infinite `while` loop and user choice mapping.

---

## 2. State Management

In a command-line application without a database, **state management** refers to how data persists during a running session. 

* **Local State variables** are initialized inside the `main()` function:
  ```python
  account_balance = 0.0          # Tracks the floating-point financial state
  transaction_history = []       # A Python list acting as an in-memory database
