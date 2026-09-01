# Build a Personal Information Program
# Task 1 - Python Programming Track

def main():
    print("--- Welcome to the Profile Builder ---")
    
    # 1. Accepting basic information using input()
    # Using meaningful variable names
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # 2. Type conversion: converting string input to an integer
    age_input = input("Enter your age: ")
    age = int(age_input) 
    
    profession = input("Enter your current profession or major: ")
    hobby = input("What is your favorite hobby? ")

    # 3. Formatted output using f-strings
    print("\n" + "="*35)
    print("         USER PROFILE CARD         ")
    print("="*35)
    
    # F-strings allow us to embed variables directly into the string
    print(f"Name:       {first_name.title()} {last_name.title()}")
    print(f"Age:        {age} years old")
    print(f"Profession: {profession.capitalize()}")
    print(f"Hobby:      {hobby.capitalize()}")
    print("="*35)

if __name__ == "__main__":
    main()
