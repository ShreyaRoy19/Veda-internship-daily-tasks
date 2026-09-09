def main():
    # Initialize parallel lists for student names and marks
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    marks = [85, 92, 78, 95, 88]

    print("--- Student Record Program ---")

    # 1. Searching Functionality
    search_name = "Charlie"
    print(f"\nSearching for '{search_name}':")
    if search_name in names:
        # Find the index of the name to get the synchronized mark
        index = names.index(search_name)
        print(f"Found: {search_name} scored {marks[index]}")
    else:
        print(f"{search_name} not found in records.")

    # 2. Highest and Lowest Score Results
    # Using built-in functions max() and min() as suggested in the hints
    highest_mark = max(marks)
    highest_index = marks.index(highest_mark)
    print(f"\nHighest Score: {names[highest_index]} with {highest_mark}")

    lowest_mark = min(marks)
    lowest_index = marks.index(lowest_mark)
    print(f"Lowest Score: {names[lowest_index]} with {lowest_mark}")

    # 3. Sorting Functionality
    print("\nRecords sorted by score (Highest to Lowest):")
    # Using zip() to keep names and marks synchronized while sorting
    synchronized_records = list(zip(names, marks))
    
    # Using sorted() to create a new sorted list based on the marks (index 1 of the tuple)
    sorted_records = sorted(synchronized_records, key=lambda x: x[1], reverse=True)

    for student_name, student_mark in sorted_records:
        print(f"{student_name}: {student_mark}")

if __name__ == "__main__":
    main()
