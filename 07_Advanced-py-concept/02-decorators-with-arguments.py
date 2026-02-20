def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                print(f"{i+1}.", end=' ')
                func(a)
        return wrapper
    return decorator


num = int(input("Enter the number how many time you want to execute the program : ")) # modification for the number of time i want to execute.
@repeat(num)

def say_hello(a): 
    print(f"Hello, {a}")

say_hello("Ganesh")
