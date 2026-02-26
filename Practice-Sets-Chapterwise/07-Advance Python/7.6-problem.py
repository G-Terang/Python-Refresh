'''
Q6. map(), filter(), and reduce()

    1.  Use map() to convert [1, 2, 3, 4, 5] into their cubes.
    2.  Use filter() to get only even numbers from [10, 11, 12, 13, 14] .
    3.  Use reduce() from functools to find the product of all elements in [1, 2, 3, 4] .


'''
from functools import reduce

# Solution of problem number 1
given_numbers = [1, 2, 3, 4, 5]
numbers = list(map(lambda x:x**3, given_numbers))
print(f"Given numbers : {given_numbers}\nCubed numbers using map fn : {numbers}\n")

# solution of problem number 2
new_numbers = [10, 11, 12, 13, 14]
filter_numbers = list(filter(lambda x:x%2==0, new_numbers))
print(f"Given numbers : {new_numbers}\nFiltered even numbers: {filter_numbers}\n")

# solution of problem number 3
new_numbers3 = [1, 2, 3, 4]
product_numbers = reduce(lambda x,y:x*y, new_numbers3)
print(f"Given numbers : {new_numbers3}\nProduct of all the numbers: {product_numbers}")