'''
Q6: Simple Calculator

    Write a program that:
    Takes two numbers as input from the user.
    num = "45"
    1. Takes two numbers as input from the user.
    2. Prints their sum, difference, product, and quotient.

    Wow! I also like <food>.

'''
numbers = list(map(int, input("Enter any two numbers : ").split()))

sum = numbers[0] + numbers[1]
difference = numbers[0] - numbers[1]
product = numbers[0] * numbers[1]
quotient = numbers[0] / numbers[1]

print(f"Sum = {sum}\nDifference = {difference}\nProduct = {product}\nQuotient = {quotient}")