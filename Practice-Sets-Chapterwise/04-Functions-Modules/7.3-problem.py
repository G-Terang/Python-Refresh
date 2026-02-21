'''
7. Bonus Challenges

    1.  Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
    2.  Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .
    3.  Create a small module my_utils.py with a function is_even(n) that returns True if n is even Import and use it in another Python file.

'''
import my_utils

my_utils.is_even(8)
print("Using my_utils.is_even:")
for value in (8, 11, 24):
    print(f"{value} -> {my_utils.is_even(value)}")