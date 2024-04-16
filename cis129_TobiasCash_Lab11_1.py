# Tobias Cash
# cis129
# Lab11 exercise 9.1 and 9.2
# 4/15/2024
# This program is for inputting grades, calculating the average and saving the data.
# User can choose between adding grades or calculating the average. Focus is on saved
# data after program is terminated.

# Function to append grades to the file
def append_grades_to_file():
    with open('grades.txt', 'a') as file:  # Open in append mode
        print("Enter grades. Type '-1' to stop entering grades.")
        while True:
            grade = input('Enter a grade: ')
            if grade == '-1':
                break
            file.write(grade + '\n')
        print("Grades appended to grades.txt successfully.")

# Function to read grades from the file and calculate statistics
def read_grades_and_calculate_statistics():
    try:
        with open('grades.txt', 'r') as file:
            grades = [int(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print("No grades file found. Please enter some grades first.")
        return

    if grades:
        total = sum(grades)
        count = len(grades)
        average = total / count
        print("Grades read from file:")
        for grade in grades:
            print(grade)
        print(f"\nTotal of grades: {total}")
        print(f"Count of grades: {count}")
        print(f"Average grade: {average:.2f}")
    else:
        print("No valid grades to display.")

# Main script logic to ask what the user wants to do
while True:
    action = input("Do you want to 'add' grades or 'calculate' statistics? (add/calculate/exit): ").lower()
    if action == 'add':
        append_grades_to_file()
    elif action == 'calculate':
        read_grades_and_calculate_statistics()
    elif action == 'exit':
        break
    else:
        print("Invalid option, please choose 'add', 'calculate', or 'exit'.")
