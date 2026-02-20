'''
Q4. Recursion in Python
    1.  Write a recursive function factorial(n) that returns the factorial of a number.
    2.  Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
    
'''
def factorial(n):
    if n == 0 or n ==1: 
        return 1
    else:
        return n*factorial(n-1)

a=int(input("Enter a number to find the factorial of the number : "))
print(f"The factorial of {a} is : {factorial(a)}")