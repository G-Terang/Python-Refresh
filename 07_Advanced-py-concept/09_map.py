number = [1,2,3,4,6,7,8,9]


# using function to get the square values
# def square(x):
#     return x*x
# new_number = list(map(square, number))


# using lambda anonymous function 
new_number = list(map(lambda x:x*x, number))
print(new_number)