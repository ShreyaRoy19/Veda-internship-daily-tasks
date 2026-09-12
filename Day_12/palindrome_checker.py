def is_palindrome(text: str) -> bool:
    """
    Determines whether a word or sentence is a palindrome 
    after normalizing case, ignoring spaces, and removing punctuation.
    """
    # Normalize the string: convert to lowercase and keep only alphanumeric characters
    normalized = "".join(char.lower() for char in text if char.isalnum())
    
    # Check if the normalized string equals its reverse
    return normalized == normalized[::-1]


def main():
    print("=== Palindrome Checker ===")
    print("Type 'exit' or 'quit' to stop the program.\n")
    
    while True:
        user_input = input("Enter a word or sentence: ").strip()
        
        if user_input.lower() in ('exit', 'quit'):
            print("Exiting Palindrome Checker. Goodbye!")
            break
            
        if not user_input:
            print("Please enter a valid word or sentence.\n")
            continue
            
        if is_palindrome(user_input):
            print(f"Result: '{user_input}' is a valid palindrome!\n")
        else:
            print(f"Result: '{user_input}' is NOT a palindrome.\n")


if __name__ == "__main__":
    main()
