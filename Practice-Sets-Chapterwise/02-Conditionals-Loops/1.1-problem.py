'''
1. If-Else Conditional Statements

    1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
    2. Create a program that checks if a person is eligible to vote (age >= 18).
    3. Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

'''


num = int(input("Enter a number : "))
if num>0:
    print("Number is positive.")
elif num<0:
    print("Number is negative.")
else:
    print("Number is zero.")