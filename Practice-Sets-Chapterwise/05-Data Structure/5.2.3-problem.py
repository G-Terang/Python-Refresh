'''
5. Dictionaries and Dictionary Methods

    1.  Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
        1.  Print the value of "name" .
        2.  Change "grade" to "A+" .
        3.  Add a new key "city" with value "Delhi" .
        
    2.  Create a dictionary of three friends and their phone numbers. Use:
        1.  keys() to get all names
        2.  values() to get all numbers
        3.  items() to loop over key-value pairs and print them
'''

friends = {'Ram': 1234567890, "Lakhs": 1324756890, "kakhs": 9087654213}


# Operation number 2 - keys() to get all the names from the above dictionary
print(f"{friends.items()}")