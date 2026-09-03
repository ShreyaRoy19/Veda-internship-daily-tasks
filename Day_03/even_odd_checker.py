def main():
    print("Type 'exit' or press Ctrl+C to stop.")
    
    # Adding a loop so it handles multiple inputs continually
    while True:
        # 1. Accept a number from the user
        user_input = input("Enter a number: ")
        
        if user_input.lower() == 'exit':
            break
            
        try:
            # Convert the string input into an integer
            number = int(user_input)
            
            # 2. Determine if it is even or odd
            if number % 2 == 0:
                print(f"{number} is Even.")
            else:
                print(f"{number} is Odd.")
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Fixed the double underscores here!
if __name__ == "__main__":
    main()
