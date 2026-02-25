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

@this_is_decorator
def say_hello():
    print("Hello!")

say_hello()



'''
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Ganesh")
'''