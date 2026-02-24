'''
Q3. Tuples and Operations on Tuples

    1.  Create a tuple coordinates = (10, 20) and print both elements.
    2.  Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
    3.  Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.


'''

coordinates = (10, 20)
new = list(coordinates)
new[0]=50
tuple(new)
print(new)