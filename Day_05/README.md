# 🎯 Number Guessing Game (Task 5)

A Python 3 command-line application where the user guesses a randomly generated number between 1 and 100. The game provides continuous high/low feedback until the correct number is found, tracking the total attempts taken to win. 

## 🚀 Features

* **Randomized Gameplay:** Generates a unique target number each session using Python's `random` module.
* **Interactive Feedback:** Guides the player with immediate "Too high!" or "Too low!" hints.
* **Attempt Tracking:** Accurately counts and displays the total number of guesses upon winning.
* **Optimized Execution:** Uses an efficient `while True` loop that breaks cleanly upon success, ensuring the script runs smoothly without risking timeouts.
* **Robust Error Handling:** Prevents the program from crashing if a user inputs invalid data (like letters or symbols) using `try-except` blocks.

## 🛠️ Prerequisites

* Python 3.x installed on your local machine.

## 💻 How to Run

1. Download or save the `guessing_game.py` file to your computer.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved the file. For example:
   ```bash
   cd path/to/your/folder
## 📊 Input and Expected Output
When you run the script, the game will prompt you for your Input (number guesses) and display the corresponding Output based on whether your guess is too high, too low, or correct.
```bash
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too low! Try a higher number.

Enter your guess: 75
Too high! Try a lower number.

Enter your guess: 62
Too low! Try a higher number.

Enter your guess: 68
Congratulations! You guessed the correct number: 68
It took you 4 attempts to win.

