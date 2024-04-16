# Tobias Cash
# cis129
# Lab11 exercise 9.3
# 4/15/2024
# This program enables the user to create a csv file with a header which identifies the columns
# and input of each student with complete name and exam grades. The focus here is to have permanent saved
# data.

import csv


def write_student_records_to_csv():
    """
    Prompts the instructor to enter student information and exam grades,
    and writes each student's record into 'grades.csv' in CSV format.

    """
    # Open the CSV file for writing
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write a header row (optional, but good practice)
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        while True:
            # Input student details
            first_name = input("Enter student's first name (or type 'exit' to stop): ")
            if first_name.lower() == 'exit':
                break
            last_name = input("Enter student's last name: ")
            grades = []
            for i in range(1, 4):  # Three exams
                while True:
                    try:
                        grade = int(input(f"Enter grade for Exam {i}: "))
                        grades.append(grade)
                        break
                    except ValueError:
                        print("Invalid input! Please enter an integer.")

            # Write the record to the CSV file
            writer.writerow([first_name, last_name] + grades)
            print("Record added successfully.")

    print("All records have been successfully written to 'grades.csv'.")


# Invoke the function
write_student_records_to_csv()