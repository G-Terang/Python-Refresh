'''
9. Bonus Challenges

    1.  Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
    2.  Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
    3.  Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.


'''
def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is about to run now .....")
        result = func(*args, **kwargs)
        print("Function has finished running.")
        return result
    return wrapper


# Example usage:
@universal_decorator
def add(a, b):
    return a + b


@universal_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(add(5, 3))
print(greet("Alice"))
print(greet("Bob", greeting="Hi"))