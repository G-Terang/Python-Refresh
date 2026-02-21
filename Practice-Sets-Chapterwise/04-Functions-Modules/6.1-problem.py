'''
6. Variable Scope and Docstrings
    1.  Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
    
    2.  Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
'''

def increment():
    counter = 0
    return counter + 1

print(increment())
print(increment())
print(increment())
print(increment())
#this wont increment the value of the counter since conter is a local variable not a global variable.
