def sum(a,b):
    print("This is the sum of 2 numbers using local variable: ")
    c = a + b
    global z #I can modify the global variable this way
    z = 100 #This will basically refer to global variable and not create local variable
    return c

z = 9
print(sum(3, 99))
print(f"Printing the value of a global variable: {z}")