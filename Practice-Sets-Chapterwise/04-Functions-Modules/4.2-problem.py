'''
Q4. Recursion in Python
    1.  Write a recursive function factorial(n) that returns the factorial of a number.
    2.  Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
    
'''
def sum_of_digits(n):
    if n == 0 :
        return 0
    return n+sum_of_digits(n-1)

a=int(input("Enter a number to get the sum of all the numbers(1 to N) : "))
print(f"The total is : {sum_of_digits(a)}")













# def sumof(n):
#     if n == 0:
#         return 0
#     return n+sumof(n-1)

# a = int(input("Enter a number: "))
# print(f"The sum is : {sumof(a)}")