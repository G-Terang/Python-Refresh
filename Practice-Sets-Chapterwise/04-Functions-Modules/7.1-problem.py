'''
7. Bonus Challenges

    1.  Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
    2.  Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .
    3.  Create a small module my_utils.py with a function is_even(n) that returns True if n is even Import and use it in another Python file.

'''

# def fibonachi(n):
#     if n<=1:
#         return n
#     else:
#         return fibonachi(n-1)+fibonachi(n-2)

# a = 5
# print(f"The {a}th fibonachi number is : {fibonachi(a)}")



def fibonacci_recursive(n):
    # Base cases: handles the first two numbers in the sequence (0 and 1)
    if n <= 1:
        return n
    # Recursive case: each number is the sum of the two preceding ones
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example of how to use the function to get a specific number
num = 5
print(f"The {num}th Fibonacci number is: {fibonacci_recursive(num)}") 