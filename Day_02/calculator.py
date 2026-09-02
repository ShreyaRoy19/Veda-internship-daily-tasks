def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handling division by zero
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def modulus(x, y):
    # Handling modulo by zero
    if y == 0:
        return "Error: Cannot perform modulus by zero."
    return x % y

def run_calculator():
    print("--- Simple Python Calculator ---")
    
    # Input handling
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return

    print("\nAvailable Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    choice = input("\nSelect an operation (1/2/3/4/5): ")

    print("\n--- Output ---")
    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
    else:
        print("Invalid selection. Please choose a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    run_calculator()
