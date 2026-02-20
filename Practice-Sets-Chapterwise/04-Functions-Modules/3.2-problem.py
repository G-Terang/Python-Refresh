'''
3. Lambda Functions
    1.  Write a lambda function that adds two numbers and test it.
    2.  Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares

'''

numbers = [1, 2, 3, 4, 5]

# Using plain FOR Loop, Without using lambda function with map()
square = []
for items in numbers :
    item = items**2
    square.append(item)

print(f"The initial list is : {numbers} and after squaring all the elements : {square}")

# this is using lambda function with map()
sec_square = list(map(lambda x:x**2, numbers))
print(f"This is using Lambda function: {sec_square}")