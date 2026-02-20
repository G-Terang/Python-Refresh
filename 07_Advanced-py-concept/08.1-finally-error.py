def divide(a,b):
    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print(e)
    finally:
        print("This line is also executed.") #This would have not excuted if it was not written inside finally.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
divide(a,b)