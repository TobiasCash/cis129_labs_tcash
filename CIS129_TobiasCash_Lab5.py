# Tobias Cash
# 2/25/2024
# This program calculates the total amount
# of bottles returned for one week
# and the total amount paid out

# code declares necessary variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

# outer while-loop
# resets values and controls execution of program
while keepGoing == 'y':
    totalBottles = 0
    totalPayout = 0

    # asks user for input
    print("Do you want to enter another week's worth of data?")
    print('Enter y or n')
    keepGoing = input().lower()

    # input sanitation for keepGoing (yes, no, or invalid)
    # .lower() to avoid capitalize error
    while keepGoing not in ['y', 'n']:
        print('Invalid input, please enter y or n:')
        keepGoing = input().lower()

    # if statement to check if code will execute
    # declares variable for 7 days
    # sets counter to day 1
    if keepGoing == 'y':
        NBR_OF_DAYS = 7
        totalBottles = 0
        todayBottles = 0
        counter = 1

        # inner while-loop gets the number of bottles for each day
        # input sanitation for invalid value (number instead of string)
        while counter <= NBR_OF_DAYS:
            print('Enter number of bottles returned for day', counter, ':')
            try:
                todayBottles = int(input())
                totalBottles = totalBottles + todayBottles
                counter = counter + 1
            except ValueError:
                print('Invalid input, please enter a valid number.')

        # calculates payout for whole week
        PAYOUT_PER_BOTTLE = .10
        totalPayout = totalBottles * PAYOUT_PER_BOTTLE

        # prints total bottles returned and total payout for week
        print('Total bottles returned for the week:', totalBottles)
        print('Total payout for the week: $ {:,.2f}'.format(totalPayout))
