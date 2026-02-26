'''
8. *args and **kwargs

    1.  Write a function sum_all(*args) that accepts any number of integers and returns their sum.
    2.  Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
        
        print_details(name="Alice", age=25, city="Delhi")
                name: Alice
                age: 25
                city: Delhi

'''

def print_details(**kwargs):
    for i in kwargs.keys():
        print(f"{i} : {kwargs[i]}")


print_details(name="Alice", age=25, city="Delhi")
