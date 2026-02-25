'''
6. Bonus Challenges

    1.  Write a program that takes a list of numbers and removes all duplicates using a set.
    2.  Given a dictionary of products and their prices, find the product with the highest price.
    3.  Write a program that merges two dictionaries into one.

'''

n = int(input("Enter how many product you want to enter : "))
products = {}

for i in range(n):
    name = input("Enter the product name : ")
    price = float(input("Enter price : "))
    products[name]=price
    
highest_product = max(products, key=products.get)

print(f"The product of the highest price is : {highest_product}")
print(f"The highest price of the product is : {products[highest_product]} rs")