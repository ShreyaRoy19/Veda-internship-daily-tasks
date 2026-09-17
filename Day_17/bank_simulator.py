def show_menu():
    print("\n--- Veda Technology: Bank Account Simulator ---")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def check_balance(balance):
    print(f"\nCurrent Available Balance: ${balance:.2f}")

def deposit(balance, history):
    try:
        amount = float(input("\nEnter amount to deposit: $"))
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return balance
        
        balance += amount
        history.append(f"Deposited: ${amount:.2f}")
        print(f"Successfully deposited ${amount:.2f}.")
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
    return balance

def withdraw(balance, history):
    try:
        amount = float(input("\nEnter amount to withdraw: $"))
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return balance
        
        if amount > balance:
            print("Error: Insufficient funds! Withdrawal exceeds available balance.")
            return balance
        
        balance -= amount
        history.append(f"Withdrew: ${amount:.2f}")
        print(f"Successfully withdrew ${amount:.2f}.")
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
    return balance

def show_history(history):
    print("\n--- Transaction History ---")
    if not history:
        print("No transactions recorded yet.")
    else:
        for idx, transaction in enumerate(history, 1):
            print(f"{idx}. {transaction}")

def main():
    account_balance = 0.0
    transaction_history = []
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            check_balance(account_balance)
        elif choice == '2':
            account_balance = deposit(account_balance, transaction_history)
        elif choice == '3':
            account_balance = withdraw(account_balance, transaction_history)
        elif choice == '4':
            show_history(transaction_history)
        elif choice == '5':
            print("\nThank you for using the Bank Account Simulator. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()
