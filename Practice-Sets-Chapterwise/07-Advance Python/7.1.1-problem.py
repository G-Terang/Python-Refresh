'''
1. Decorators in Python

    1.  Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints
    "Hello!" .
    
    2.  Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

'''

def this_is_decorator(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# @decorator

def say_hello():
    print("Hello!")
f = this_is_decorator(say_hello)

f()