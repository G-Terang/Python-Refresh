'''
6. Bonus Challenges

    1.  Write a program that takes a list of numbers and removes all duplicates using a set.
    2.  Given a dictionary of products and their prices, find the product with the highest price.
    3.  Write a program that merges two dictionaries into one.

'''

numbers = list(map(int, input("Enter the numbers: ").split()))

#Since list is converted into set by typecasting this will remove all the duplicate numbers 
new_numbers = list(set(numbers))
print(f"Your initial list is : {numbers}")
print(f"The new list without any duplicates is : {new_numbers}")
