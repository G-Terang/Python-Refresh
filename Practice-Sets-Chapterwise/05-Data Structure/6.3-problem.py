'''
6. Bonus Challenges

    1.  Write a program that takes a list of numbers and removes all duplicates using a set.
    2.  Given a dictionary of products and their prices, find the product with the highest price.
    3.  Write a program that merges two dictionaries into one.

'''


dict_one = {
    "name":"Ganesh",
    "surename":"Terang",
    "salary":86000
}

dict_two = {
    "new_name":"Random",
    "new_surename":"Unknown",
    "new_salary":32000
}

# now let's merge the above two dictionaries
dict_one.update(dict_two)

print(f"The merged dictionary is : {dict_one}")