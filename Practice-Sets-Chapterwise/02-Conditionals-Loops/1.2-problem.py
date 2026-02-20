'''
1. If-Else Conditional Statements

    1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
    2. Create a program that checks if a person is eligible to vote (age >= 18).
    3. Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

'''


num = int(input("How old are you : "))
if num>18 and num<100:
    print("You are eligible to vote")
elif num<18 and num>0:
    print("You are not eligible to vote")
else:
    print("Opps you have entered an unrealistict age")