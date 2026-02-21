def sum(a,b):
    '''This is the sum of 2 numbers using local variable:'''
    c = a + b
    global z #I can modify the global variable this way
    z = 100 #This will basically refer to global variable and not create local variable
    return c


print(sum.__doc__) # __doc__ will give the information of a function when the multiline comment is writtten right after the function defination. And this information can also be seen when I or anyone hover orver the "sum" function.