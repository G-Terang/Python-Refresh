def sum(a,b):
    # a and b are local variable, that basically means that i want access these variable only inside this function. 
    c = a + b
    z = 2 # It creates a local variable z which is destroyed after thif function execution.
    return c

z = 99 # z is a global variable
print(sum(2,3))
# print(c) 
print(z) 