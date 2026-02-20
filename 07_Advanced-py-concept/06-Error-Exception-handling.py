while True:
    try:
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        print(f"The sum of {a} and {b} is : {a+b}")
    except Exception as e:
        print("Some ERRORS occured!",e)