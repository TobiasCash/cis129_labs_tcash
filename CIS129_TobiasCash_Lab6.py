# Tobias Cash
# CIS129_Lab6
# 3/3/2024
# This program calculates the number of packages of hot dogs
# and hot dog buns are needed for a cookout with the minimum
# amount of leftovers.

def get_numeric_input(prompt):
    """
    function prompts the user for a numeric input and validates it.
    Repeats it until a valid integer is given.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_yes_no_input(prompt):
    """
    function prompts the user for a 'y' or 'n' input and validates it.
    Repeats it until a valid input is given.
    """
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def getTotalHotDogs(attendees, hotDogs_per_attendee):
    """
    Calculates the total number of hot dogs needed.
    """
    return attendees * hotDogs_per_attendee

def showResults(totalHotDogs):
    """
    Calculates and prints the required packages of hot dogs and buns, and the leftovers.
    """
    DOGS = 10
    BUNS = 8

    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS

    minDogs = (totalHotDogs // DOGS) + (0 ** (0 ** dogsLeft))
    minBuns = (totalHotDogs // BUNS) + (0 ** (0 ** bunsLeft))

    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)

def main():
    """
    The main function prompts user to enter number of attendees and average number of hot dogs
    that attendees will eat. It also calculates the number of hot dogs and minimum amount
    of packages needed. run_again will ask if user want's to stop program or run it again.
    """
    while True:
        attendees = get_numeric_input("Enter the number of people attending the cookout: ")
        hotDogs_per_attendee = get_numeric_input("Enter the number of hot dogs per person: ")

        totalHotDogs = getTotalHotDogs(attendees, hotDogs_per_attendee)
        showResults(totalHotDogs)

        run_again = get_yes_no_input("Do you want to run the program again? (y/n): ")
        if run_again == 'n':
            break

# calls the main function which executes the program
main()
