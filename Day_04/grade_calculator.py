def get_grade(percentage):
    """Assigns a grade based on percentage using clear boundaries."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'

def main():
    print("--- Student Grade Calculator ---")
    
    # Get the number of subjects
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    total_marks = 0
    max_marks_per_subject = 100

    # Accept and validate marks for each subject
    for i in range(1, num_subjects + 1):
        while True:
            try:
                marks = float(input(f"Enter marks for subject {i} (0-100): "))
                # Validate that marks are within the allowed range
                if 0 <= marks <= 100:
                    total_marks += marks
                    break
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")

    # Calculate percentage once to avoid unnecessary repetition
    max_total = num_subjects * max_marks_per_subject
    percentage = (total_marks / max_total) * 100
    grade = get_grade(percentage)

    # Deliverables: Sample student results
    print("\n--- Final Results ---")
    print(f"Total Marks: {total_marks} / {max_total}")
    print(f"Percentage:  {percentage:.2f}%")
    print(f"Final Grade: {grade}")

if __name__ == "__main__":
    main()
