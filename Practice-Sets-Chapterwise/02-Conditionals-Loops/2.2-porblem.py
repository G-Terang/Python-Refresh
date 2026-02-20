'''
2. Match Case Statements
    1.  Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case .
    
    2.  Write a program using match case that simulates a simple calculator.
        1.  Ask the user for two numbers and an operation (+, -, *, /).
        2.  Perform the operation using match case .

'''

a=list(map(int, input("Enter any two numbers: ").split()))
print("-- OPTIONS --\n+, -, *, /\n")
b=input("Kindly choose one option to perform the operation. + for addition, - for substraction like wise: ")
match b:
    case "+":
        print(f"{a[0]} + {a[1]} = {a[0]+a[1]}")
    case "-":
        print(f"{a[0]} - {a[1]} = {a[0]-a[1]}")
    case "*":
        print(f"{a[0]} * {a[1]} = {a[0]*a[1]}")
    case "/":
        print(f"{a[0]} / {a[1]} = {a[0]/a[1]}")
    case _:
        print('Invalid option has been choosen')