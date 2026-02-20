def decorator(func):
    def wrapper():
        print("I'm about to print something now ......")
        func()
        print("I have printed now")
    return wrapper

def this_print():
    print("Hello !")

# this_print()
f = decorator(this_print)
f()