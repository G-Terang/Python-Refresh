try :
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    
    print("\nWhat operation do you want to perform?\nPress + for addition\nPress - for substraction\nPress * for multiplication\nPress / for division ")
    o = input("Choose operation: ")
    match o:
        case '+':
            print(f"Result: {a + b}")
        case '-':
            print(f"Result: {a - b}")
        case '*':
            print(f"Result: {a * b}")
        case '/':
            print(f"Result: {a / b}")
        case default:
            print("There was an error!")
except ValueError:
    print("Kindly enter the integer numbers.")
except ZeroDivisionError:
    print("Kindly do not divide a number with the number 0.")
except Exception as e:
    print(f"There has been some error during your operation. \nError: {e}")
    
