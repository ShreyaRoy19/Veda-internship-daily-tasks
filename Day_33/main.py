"""
Student Performance & Records Management System
Features:
- Add, update, search, and view student records.
- Input validation for marks (0 - 100).
- Automatic calculation of total marks, percentage, and letter grade.
- Class-wide performance summary (highest, lowest, and average percentages).
"""

# Dictionary to store student records:
# Key: Student ID (str)
# Value: dict containing 'name', 'marks' (dict of subject: score), 'total', 'percentage', 'grade'
students = {}


def calculate_grade(percentage):
    """Assigns a letter grade based on the percentage."""
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


def get_valid_mark(subject_name):
    """Prompts and validates that a mark is a float between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Error: Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def collect_subject_marks():
    """Collects subject marks from the user and computes metrics."""
    marks = {}
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            print("Must enter at least 1 subject.")
        except ValueError:
            print("Please enter a valid positive integer.")

    for i in range(1, num_subjects + 1):
        subject = input(f"Enter name of subject #{i}: ").strip()
        marks[subject] = get_valid_mark(subject)

    total = sum(marks.values())
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    return marks, total, percentage, grade


def add_student():
    """Adds a new student record."""
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print(f"Error: Student ID '{student_id}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    marks, total, percentage, grade = collect_subject_marks()

    students[student_id] = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
    }
    print(f"\nStudent '{name}' (ID: {student_id}) successfully added!")


def update_student():
    """Updates an existing student's name or marks."""
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print(f"Error: Student with ID '{student_id}' not found.")
        return

    student = students[student_id]
    print(f"Updating records for: {student['name']}")

    new_name = input(f"Enter new name (leave blank to keep '{student['name']}'): ").strip()
    if new_name:
        student["name"] = new_name

    update_marks = input("Do you want to re-enter marks? (y/n): ").strip().lower()
    if update_marks == "y":
        marks, total, percentage, grade = collect_subject_marks()
        student["marks"] = marks
        student["total"] = total
        student["percentage"] = percentage
        student["grade"] = grade

    print(f"\nStudent ID '{student_id}' updated successfully.")


def search_student():
    """Searches for a student by ID or Name."""
    print("\n--- Search Student ---")
    query = input("Enter Student ID or Name to search: ").strip().lower()

    matches = []
    for s_id, data in students.items():
        if query == s_id.lower() or query in data["name"].lower():
            matches.append((s_id, data))

    if not matches:
        print("No matching student records found.")
        return

    for s_id, data in matches:
        display_single_student(s_id, data)


def display_single_student(s_id, data):
    """Helper function to print formatted details of one student."""
    print("\n" + "=" * 45)
    print(f"ID         : {s_id}")
    print(f"Name       : {data['name']}")
    print("Marks      :")
    for subject, mark in data["marks"].items():
        print(f"  - {subject}: {mark:.1f}")
    print(f"Total Marks: {data['total']:.2f}")
    print(f"Percentage : {data['percentage']:.2f}%")
    print(f"Grade      : {data['grade']}")
    print("=" * 45)


def view_all_students():
    """Displays all student records."""
    print("\n--- All Student Records ---")
    if not students:
        print("No student records available.")
        return

    for s_id, data in students.items():
        display_single_student(s_id, data)


def performance_summary():
    """Calculates and displays class-wide performance statistics."""
    print("\n--- Performance Summary ---")
    if not students:
        print("No student data available to calculate summary.")
        return

    total_percentage = sum(s["percentage"] for s in students.values())
    avg_percentage = total_percentage / len(students)

    highest_student = max(students.items(), key=lambda item: item[1]["percentage"])
    lowest_student = min(students.items(), key=lambda item: item[1]["percentage"])

    print(f"Total Enrolled Students : {len(students)}")
    print(f"Class Average Percentage: {avg_percentage:.2f}%")
    print(
        f"Top Performer           : {highest_student[1]['name']} "
        f"({highest_student[1]['percentage']:.2f}%, Grade: {highest_student[1]['grade']})"
    )
    print(
        f"Lowest Performer        : {lowest_student[1]['name']} "
        f"({lowest_student[1]['percentage']:.2f}%, Grade: {lowest_student[1]['grade']})"
    )


def main():
    """Main CLI driver menu."""
    while True:
        print("\n==========================================")
        print(" STUDENT RECORD & PERFORMANCE SYSTEM")
        print("==========================================")
        print("1. Add New Student")
        print("2. Update Student Details")
        print("3. Search Student")
        print("4. View All Students")
        print("5. Generate Performance Summary")
        print("6. Exit")
        print("==========================================")

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
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 6.")


if __name__ == "__main__":
    main()
