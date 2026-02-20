while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a == 0:
        raise ValueError("Kindly do not divide a 0 !")
    elif b == 0:
        raise ValueError("Kindly do not divide any number with a 0 !")
    else:
        print(f"The result-1 is : {a/b}")
        print(f"The result-2 is : {a//b}")
        print(f"The result-3 is : {a%b}")