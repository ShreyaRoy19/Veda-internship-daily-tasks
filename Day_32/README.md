# Student Management System

A Python-based command-line application designed to manage student academic records, calculate grades, perform data lookups, and generate class performance summaries.

---

## Features

- **Record Management:** Add new student records and update existing details or subject marks.
- **Dynamic Subject Handling:** Support for custom subject names and varying subject counts per student.
- **Input Validation:** Enforces numerical entry and standard range constraints ($0$–$100$) for marks before calculations.
- **Automated Grading:** Calculates total score, percentage, and assigned letter grades ($A+$, $A$, $B$, $C$, $D$, $F$).
- **Search Capability:** Find students quickly by their Unique Student ID or Name.
- **Performance Analytics:** Computes overall class average, identifies top and lowest performers, and tracks pass/fail counts.

---

## Grading Scale

| Percentage Range | Grade |
| :--- | :--- |
| 90% – 100% | A+ |
| 80% – 89.99% | A |
| 70% – 79.99% | B |
| 60% – 69.99% | C |
| 50% – 59.99% | D |
| Below 50% | F (Fail) |

---

## Project Structure

```text
student-management-system/
│
├── main.py              # Main Python source file containing system logic
└── README.md            # Project documentation and setup guide
