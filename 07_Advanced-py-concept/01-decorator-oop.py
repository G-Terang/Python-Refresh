# A Decorator is a function that takes a function and creates a new function inside its body (eg. wrapper) and then returns the newly created function.

def decorate(func):
    def wrapper():
        print("\nI am about to print something now: ----------->\n")
        func()
        print("\nI have printed the middle line .\n")
    return wrapper

@decorate #alternate way to use decorator

def say_hello():
    print("Hello !")

say_hello()

# lets_say = decorate(say_hello)
# lets_say()