'''
2. Function Arguments & Return Values

    1.  Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last" .
    
    2.  Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
        1.  Both length and width
        2.  Only length (use default width)


'''

def calculate_area(length, width):
    area = length*width
    return area

a=int(input("Enter the length of a rectangle: "))
b=int(input("Enter the width of a rectangle: "))

print(f"The area of the rectangle is : {calculate_area(a, b)}")