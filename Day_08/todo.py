def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*25)
    print("      TO-DO LIST")
    print("="*25)
    print("1. Add a Task (Create)")
    print("2. View Tasks (Read)")
    print("3. Update a Task (Update)")
    print("4. Remove a Task (Delete)")
    print("5. Exit")
    print("="*25)

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f"\n✅ Task '{task}' added successfully!")
    else:
        print("\n❌ Task cannot be empty.")

def view_tasks(tasks):
    """Displays all current tasks."""
    if not tasks:
        print("\n📭 Your to-do list is currently empty.")
        return False
    else:
        print("\n--- Current Tasks ---")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        return True

def update_task(tasks):
    """Updates an existing task by its index."""
    if view_tasks(tasks):
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    old_task = tasks[task_num - 1]
                    tasks[task_num - 1] = new_task
                    print(f"\n✅ Task updated from '{old_task}' to '{new_task}'!")
                else:
                    print("\n❌ Task description cannot be empty.")
            else:
                print("\n❌ Invalid task number.")
        except ValueError:
            print("\n❌ Please enter a valid numerical input.")

def remove_task(tasks):
    """Removes a task by its index."""
    if view_tasks(tasks):
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"\n🗑️ Task '{removed}' removed successfully!")
            else:
                print("\n❌ Invalid task number.")
        except ValueError:
            print("\n❌ Please enter a valid numerical input.")

def main():
    """Main function to drive the application loop."""
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("\nExiting To-Do List. Goodbye! 👋\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
