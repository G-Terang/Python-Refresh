'''
5. Exception Handling and Custom Errors

    1.  Write a program that asks the user to enter a number and handles:
        1.  ValueError if the input is not a number
        2.  ZeroDivisionError if you try to divide by zero
        
    2.  Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

'''

'''
class NegativeValueError(Exception):
    pass

while True:
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        if a<0 or b<0:
            raise NegativeValueError("Do not enter negative values!")
        
        result = a/b
        print(f"The result of {a} divided by {b} is : {result}")
        
        
    except ValueError:
        print("Kindly do not enter anything other than numbers!")
    
    except ZeroDivisionError:
        print("Do not divide a number with 0 !")
        
        '''
class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a number : "))
    if num<0:
        raise NegativeNumberError("You have entered a negative number.")
    result = 10/num
    print(result)
except ValueError:
    print("Enter a valid number. ")
except ZeroDivisionError:
    print("Given number can not be divided by 0")
except NegativeNumberError:
    print("Error: The number can not be negative.")