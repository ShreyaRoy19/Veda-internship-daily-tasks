# Prime Number Analyzer

A robust and optimized Python program designed to check for prime numbers and generate all prime numbers within a specified range. Built as part of the Python programming track to practice loops, conditional logic, functions, and algorithmic optimization.

## Features

* **Prime Checker (`is_prime`)**: Evaluates whether any given integer is a prime number, with built-in handling for edge cases like $0$ and $1$.
* **Range Generator (`generate_primes_in_range`)**: Scans a specified inclusive range and returns a list of all prime numbers found within it.
* **Optimized Performance**: Utilizes square root bounding ($\sqrt{n}$) and the $6k \pm 1$ wheel factorization method to bypass unnecessary divisibility checks.

## Project Structure

```text
prime analyzer
│
├── prime.py    # Core implementation and demonstration code
└── README.md            # Documentation
