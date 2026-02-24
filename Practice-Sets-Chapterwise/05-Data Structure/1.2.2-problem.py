'''
Introduction to Lists

    1.  Create a list fruits = ["apple", "banana", "cherry"] .
        1.  Print the first fruit.
        2.  Replace "banana" with "orange" .
        3.  Print the length of the list.
        
    2.  Create a list of numbers from 1 to 10 .
        1.  Print the first three numbers using slicing.
        2.  Print the last three numbers using slicing. 

'''

numbers = []
for i in range(10):
    numbers.append(i+1)

print(numbers)
print(f"Printing the last 3 numbers from the above list using slicing : {numbers[7:10]}")