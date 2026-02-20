'''
2. Function Arguments & Return Values

    1.  Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last" .
    
    2.  Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
        1.  Both length and width
        2.  Only length (use default width)


'''

def full_name(a, b):
    f_name = a+' '+b
    return f_name

first_name = input("Enter your first name : ")
Last_name = input("Enter your last name : ")
print(full_name(first_name, Last_name))