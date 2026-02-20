'''
Q2. String Slicing and Indexing
    1.  Given text = "Python Programming" , do the following:
        1.  Print the first 6 characters
        2.  Print the last 6 characters
        3.  Print every second character from the string
        
    2.  Reverse the string text using slicing.
'''

text = 'Python Programming'
print(f"Given string is : {text}")
print(f"Printing the first 6 characters: {text[0:6]}")
print(f"Printing the last 6 characters: {text[-6:]}")
print(f"Printing every second character from the string: {text[::2]}")
