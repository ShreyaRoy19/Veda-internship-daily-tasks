import random
import sys

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Hint 1: Use random.randint() to generate the target number
    target_number = random.randint(1, 100)
    
    # Deliverable 2: Attempt counter
    attempts = 0
    
    # Loop continues until the correct answer is found
    while True:
        try:
            # Deliverable 3: User interaction for gameplay
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Hint 2: Tell the user whether their guess is high or low
            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else:
                # Hint 3: Stop the game after the correct answer
                print(f"\nCongratulations! You guessed the correct number: {target_number}")
                print(f"It took you {attempts} attempts to win.")
                break # Exits the while loop
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            sys.exit(0)

if __name__ == "__main__":
    play_guessing_game()
