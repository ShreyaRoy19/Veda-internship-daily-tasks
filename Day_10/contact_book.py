def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. View All Contacts")
    print("6. Exit")

def main():
    # Initializing the dictionary with sample contact data

    contacts = {
        "1234567890": {"name": "Alice Smith", "email": "alice@example.com"},
        "9876543210": {"name": "Bob Jones", "email": "bob@example.com"}
    }

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        # 1. CREATE (Add)
        if choice == '1':
            phone = input("Enter phone number: ")
            # Validate duplicate entries
            if phone in contacts:
                print("Error: A contact with this phone number already exists.")
            else:
                name = input("Enter contact name: ")
                email = input("Enter contact email: ")
                contacts[phone] = {"name": name, "email": email}
                print(f"Contact '{name}' added successfully!")

        # 2. READ (Search)
        elif choice == '2':
            phone = input("Enter phone number to search: ")
            if phone in contacts:
                info = contacts[phone]
                print(f"\nContact Found - Name: {info['name']}, Email: {info['email']}")
            else:
                print("Error: Contact not found.")

        # 3. UPDATE
        elif choice == '3':
            phone = input("Enter phone number to update: ")
            if phone in contacts:
                print("Leave blank if you do not want to change the current value.")
                new_name = input(f"Enter new name (current: {contacts[phone]['name']}): ")
                new_email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
                
                if new_name:
                    contacts[phone]['name'] = new_name
                if new_email:
                    contacts[phone]['email'] = new_email
                print("Contact updated successfully!")
            else:
                print("Error: Contact not found.")

        # 4. DELETE
        elif choice == '4':
            phone = input("Enter phone number to delete: ")
            if phone in contacts:
                deleted_contact = contacts.pop(phone)
                print(f"Contact '{deleted_contact['name']}' deleted successfully.")
            else:
                print("Error: Contact not found.")

        # EXTRA: View All
        elif choice == '5':
            if not contacts:
                print("The contact book is empty.")
            else:
                print("\n--- All Contacts ---")
                for phone, info in contacts.items():
                    print(f"Phone: {phone} | Name: {info['name']} | Email: {info['email']}")

        # EXIT
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option from 1 to 6.")

if __name__ == "__main__":
    main()
