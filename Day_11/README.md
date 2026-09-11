# Word and Character Counter

A robust Python 3 text analysis program that calculates the number of characters, words, sentences, and spaces in a given paragraph. 

## Features

*   **Multi-line Input Support:** Utilizes standard input (`sys.stdin`) to seamlessly process large blocks of text or multiple paragraphs without premature termination.
*   **Accurate Sentence Parsing:** Uses regular expressions to correctly identify sentences ending in various punctuation marks (`.`, `!`, `?`), including consecutive punctuation.
*   **Edge-Case Handling:** Safely handles empty inputs and strings consisting only of whitespace, preventing errors and unnecessary processing.
*   **Efficient Word Counting:** Leverages built-in string methods to accurately count words regardless of irregular spacing or tabs.

## Requirements

*   Python 3.x

## Usage

You can run this script directly from your terminal or command prompt. Because it reads from standard input, you can either paste your text interactively or pipe a text file into it.

### Interactive Mode
1. Run the script:
   ```bash
   python counter.py
