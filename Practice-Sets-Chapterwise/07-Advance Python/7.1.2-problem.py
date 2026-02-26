'''
1. Decorators in Python

    1.  Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints
    "Hello!" .
    
    2.  Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

'''
from time import time

def decorator(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print(f"Time taken for the execution of above function is {t2-t1:.2f} sec.")
    return wrapper

@decorator
def sum(n):
    total = 0
    for i in range(1,n+1):
        total +=i
    print(f"The sum of all the numbers from 1 - 1000000 is : {total}") 

sum(1000000)
        
