while True:
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print(f"The result after performing division is : {a/b}")
        
    except ValueError:
        print("Warning: Kindly avoid bad typecasting!")
        
    except ZeroDivisionError: 
        print("Warning: Kindly do not divide a number with the number 0 or Zero!")
    except Exception as exe:
        print("Unknown Error!",exe)