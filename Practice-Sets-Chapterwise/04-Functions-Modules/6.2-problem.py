'''
6. Variable Scope and Docstrings
    1.  Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
    
    2.  Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
'''

def multiply(a,b):
    '''This is the docstring to help understand what this function does, for example this function will return the factor of value a and b.'''
    c = a*b
    print(c)

multiply(2,5)
multiply(4,7)
help(multiply)