'''
4. Sets and Set Methods

    1.  Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)
    
    2.  Add 5 to the set, remove 2 , and check if 4 is in the set.
    
    3.  Create two sets:
    
        a = {1, 2, 3}
        b = {3, 4, 5}
        
            Find their:
            
            1.  Union
            2.  Intersection
            3.  Difference ( a - b )

'''
a = {1, 2, 3}
b = {3, 4, 5}

# operation 1- Union 
c = a.union(b)
print(f"Union of set a = {a} and b = {b} is: {c}")

#Operation 2- Intersection 
d = a.intersection(b)
print(f"Intersection of set a = {a} and b = {b} is: {d}")

#Operation 3 - Difference ( a - b )
e = a.difference(b)
print(f"Difference of set a = {a} and b = {b} is: {e}")