import string
import getpass

def validate_password(password):
    """
    Checks if a password meets the basic complexity requirements.
    Returns a tuple: (is_valid: bool, message: str)
    """
    # 1. Minimum Length Check (standard is usually 8 characters)
    if len(password) < 8:
        return False, "Invalid: Password must be at least 8 characters long."

    # Initialization for character checks
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    
    # string.punctuation provides a string of all standard special characters
    special_chars = string.punctuation 

    # 2. Character Checks using a single loop for efficiency
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True

    # 3. Validation Rule Enforcement
    if not has_upper:
        return False, "Invalid: Password must contain at least one uppercase letter."
    if not has_lower:
        return False, "Invalid: Password must contain at least one lowercase letter."
    if not has_number:
        return False, "Invalid: Password must contain at least one number."
    if not has_special:
        return False, "Invalid: Password must contain at least one special character."

    return True, "Success: Password is valid!"

# --- Deliverables: Examples of Valid and Invalid Passwords ---
if __name__ == "__main__":
    print("--- Password Validation Test Cases ---")
    
    test_passwords = [
        "short",                # Fails length
        "nouppercase1!",        # Fails uppercase
        "NOLOWERCASE1!",        # Fails lowercase
        "NoNumberHere!",        # Fails number
        "NoSpecialChar123",     # Fails special character
        "PerfectPass123!"       # Valid
    ]
    
    for pwd in test_passwords:
        # Note: We are printing the test passwords here just for the deliverable demonstration.
        
        is_valid, message = validate_password(pwd)
        print(f"[{'PASS' if is_valid else 'FAIL'}] {message}")

    print("\n--- Interactive Prompt ---")
    # Using getpass hides the input from the screen, satisfying the security hint.
    user_password = getpass.getpass("Enter a password to validate (input will be hidden): ")
    valid, msg = validate_password(user_password)
    print(msg)
