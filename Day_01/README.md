# Personal Information Program

## Description
This Python program prompts the user to enter their basic personal details and then displays them in a neatly formatted "Profile Card".

## Inputs
The program accepts the following inputs from the user via the command line:
* **First Name** (String): The user's first name.
* **Last Name** (String): The user's last name.
* **Age** (Integer): The user's age. The program reads this as a string and explicitly converts it to an integer using `int()`.
* **Profession** (String): The user's current job or field of study.
* **Hobby** (String): The user's favorite hobby.

## Outputs
After collecting the data, the program outputs a bordered Profile Card. It utilizes **f-strings** to embed the variables into the print statements and uses built-in string methods like `.title()` and `.capitalize()` to ensure the text looks clean and professional.
