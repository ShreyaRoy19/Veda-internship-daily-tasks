# Student Performance Management System

students = {}


def calculate_grade(percentage):
    """Determine letter grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def get_validated_marks(subject_name):
    """Prompt for marks and validate that they are between 0 and 100."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject_name} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid range. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_student():
    """Add a new student record."""
    student_id = input("\nEnter unique Student ID: ").strip()
    if student_id in students:
        print("A student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            print("Student must have at least 1 subject.")
        except ValueError:
            print("Please enter a valid whole number.")

    subjects = {}
    for i in range(1, num_subjects + 1):
        subj_name = input(f"Enter name for Subject {i}: ").strip()
        marks = get_validated_marks(subj_name)
        subjects[subj_name] = marks

    total_marks = sum(subjects.values())
    percentage = total_marks / len(subjects)
    grade = calculate_grade(percentage)

    students[student_id] = {
        "name": name,
        "subjects": subjects,
        "total": total_marks,
        "percentage": percentage,
        "grade": grade,
    }
    print(f"\nStudent '{name}' added successfully!")


def update_student():
    """Update marks or name for an existing student."""
    student_id = input("\nEnter Student ID to update: ").strip()
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    print(f"Updating record for: {student['name']}")

    new_name = input(
        "Enter new name (leave blank to keep current): "
    ).strip()
    if new_name:
        student["name"] = new_name

    print("\nUpdating Subject Marks:")
    for subj in list(student["subjects"].keys()):
        update_choice = (
            input(
                f"Update marks for '{subj}' (current: {student['subjects'][subj]})? (y/n): "
            )
            .strip()
            .lower()
        )
        if update_choice == "y":
            student["subjects"][subj] = get_validated_marks(subj)

    # Recalculate metrics
    total_marks = sum(student["subjects"].values())
    percentage = total_marks / len(student["subjects"])
    student["total"] = total_marks
    student["percentage"] = percentage
    student["grade"] = calculate_grade(percentage)

    print(f"\nRecord for Student ID {student_id} updated successfully!")


def search_student():
    """Search for a student by ID or Name."""
    query = (
        input("\nEnter Student ID or Name to search: ").strip().lower()
    )
    found = False

    for s_id, data in students.items():
        if query == s_id.lower() or query in data["name"].lower():
            print("\n" + "=" * 35)
            print(f"ID: {s_id}")
            print(f"Name: {data['name']}")
            print("Marks:")
            for subj, marks in data["subjects"].items():
                print(f"  - {subj}: {marks}")
            print(
                f"Total: {data['total']:.2f} / {len(data['subjects']) * 100}"
            )
            print(f"Percentage: {data['percentage']:.2f}%")
            print(f"Grade: {data['grade']}")
            print("=" * 35)
            found = True

    if not found:
        print("No matching student records found.")


def view_all_students():
    """Display all student records in a structured format."""
    if not students:
        print("\nNo student records available.")
        return

    print("\n" + "-" * 60)
    print(
        f"{'ID':<10}{'Name':<20}{'Total':<10}{'Percentage':<12}{'Grade':<6}"
    )
    print("-" * 60)
    for s_id, data in students.items():
        print(
            f"{s_id:<10}{data['name']:<20}{data['total']:<10.1f}{data['percentage']:<12.2f}{data['grade']:<6}"
        )
    print("-" * 60)


def performance_summary():
    """Generate aggregate statistics across all students."""
    if not students:
        print("\nNo student records available for summary.")
        return

    percentages = [data["percentage"] for data in students.values()]
    top_performer_id = max(
        students, key=lambda sid: students[sid]["percentage"]
    )
    lowest_performer_id = min(
        students, key=lambda sid: students[sid]["percentage"]
    )

    avg_percentage = sum(percentages) / len(percentages)
    passed_count = sum(
        1 for p in percentages if p >= 50
    )  # Passing threshold: 50%

    print("\n========== PERFORMANCE SUMMARY ==========")
    print(f"Total Enrolled Students: {len(students)}")
    print(f"Class Average Percentage: {avg_percentage:.2f}%")
    print(
        f"Top Performer: {students[top_performer_id]['name']} ({students[top_performer_id]['percentage']:.2f}%)"
    )
    print(
        f"Lowest Performer: {students[lowest_performer_id]['name']} ({students[lowest_performer_id]['percentage']:.2f}%)"
    )
    print(f"Passing Students: {passed_count}")
    print(f"Failing Students: {len(students) - passed_count}")
    print("=========================================")


def main():
    """Command-line menu interface."""
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student Record")
        print("2. Update Student Record")
        print("3. Search Student")
        print("4. View All Students")
        print("5. Performance Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            performance_summary()
        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 6.")


if __name__ == "__main__":
    main()
