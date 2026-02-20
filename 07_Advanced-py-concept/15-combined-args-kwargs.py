def func1(*args, **kwargs):
    print(args)
    print(kwargs)

def func2(*args, **kutte):
    total=0
    total1=0
    for items in args:
        total+=items
        print(items, end=" ")
    print(f"\nThe total combined numbers are: {total}\n")
    
    for items in kutte.keys():
        print(f"The mark {items} has obtained is : {kutte[items]}")
        total1+=kutte[items]
    print(f"\nThe combined mark of all is : {total1}")


# func1(1,2,3,4,5, hello=4, ram=5, nice=44)
func2(1,2,3,4,5,90,27, hello=4, ram=5, nice=44, Terang=100)