'''
1. Defining Functions
    1.  Write a function greet() that prints "Hello, Python Learner!" when called.
    2.  Write a function square(num) that returns the square of a given number. Test it with different numbers.


'''

def square(a):
    a=a**2
    return a
    
num=int(input("Enter a number to find the square of it :  "))
print(square(num))