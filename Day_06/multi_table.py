def generate_multiplication_table():
    try:
        # Allow the user to specify the number and the range/limit
        num = int(input("Enter the number you want a table for: "))
        limit = int(input("Enter the limit (e.g., 10): "))

        print(f"\n--- Multiplication Table for {num} ---")
        
        
        for i in range(1, limit + 1):
           
            print(f"{num} x {i:2} = {num * i}")
            
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")

# Deliverable: Output for at least three different numbers
print("Welcome to the Multiplication Table Generator!")
for attempt in range(1, 4):
    print(f"\n--- Test Run {attempt} of 3 ---")
    generate_multiplication_table()
