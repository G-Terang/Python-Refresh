a = int(input("Enter first number here: "))
b = int(input("Enter second number here: "))

try:
    c=a/b
    print(c)
except Exception as e:
    print(e)

finally: #unlike try-else this finally always get executed, does not matter if the try block is throwing error or not.
    print("This always executes.")