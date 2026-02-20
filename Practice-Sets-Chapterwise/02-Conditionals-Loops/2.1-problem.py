'''
2. Match Case Statements
    1.  Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case .
    
    2.  Write a program using match case that simulates a simple calculator.
        1.  Ask the user for two numbers and an operation (+, -, *, /).
        2.  Perform the operation using match case .

'''

day=int(input("Enter the number of a day(from 1 to 7, where 1 is Monday and 7 is Sunday) and I will tell you which day it is: "))

match day:
    case 1:
        print("DAY 1 of a week is: MONDAY")
    case 2:
        print("DAY 2 of a week is: TUESDAY")
    case 3:
        print("DAY 3 of a week is: WEDNESDAY")
    case 4:
        print("DAY 4 of a week is: THURSDAY")
    case 5:
        print("DAY 5 of a week is: FRIDAY")
    case 6:
        print("DAY 6 of a week is: SATURDAY")
    case 7:
        print("DAY 7 of a week is: SUNDAY")