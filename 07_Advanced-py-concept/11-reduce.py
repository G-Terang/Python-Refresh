from functools import reduce

numbers = [ 1, 2, 3,4 , 6,9]

def sum(a,b):
    return a+b

new = reduce(sum, numbers)
print(new)