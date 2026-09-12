# Palindrome Checker 

A clean, robust Python 3 program designed to determine whether a given word or sentence is a palindrome. This project handles case normalization, whitespace ignoring, and punctuation stripping to correctly evaluate complex sentences as well as single words.

---

## Features

- **Robust Normalization:** Automatically strips out punctuation, symbols, and spaces while converting characters to lowercase.
- **Interactive CLI Loop:** Continuously prompts the user for inputs until an exit command is given.
- **Pythonic Implementation:** Utilizes efficient list comprehensions and string slicing (`[::-1]`).

---

## Sample Input and Output

```text
=== Palindrome Checker ===
Type 'exit' or 'quit' to stop the program.

Enter a word or sentence: Racecar
Result: 'Racecar' is a valid palindrome!

Enter a word or sentence: A man, a plan, a canal: Panama
Result: 'A man, a plan, a canal: Panama' is a valid palindrome!

Enter a word or sentence: Hello Python
Result: 'Hello Python' is NOT a palindrome.

Enter a word or sentence: exit
Exiting Palindrome Checker. Goodbye!
```

---

## Concepts Covered

1. **String Slicing (`[::-1]`):** A concise Pythonic way to reverse strings.
2. **Generator Expressions & Alphanumeric Filtering (`char.isalnum()`):** Cleans raw input safely.
3. **Control Flow:** Using `while` loops and break conditions for continuous interactive CLI applications.
