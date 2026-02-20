'''
Q3. For Loops

    1.  Print numbers from 1 to 10 using a for loop.
    2.  Print the multiplication table of a number (entered by user).
    3.  Calculate the sum of all numbers from 1 to 100 using a for loop.
    4.  Print the following pattern using a for loop:
    
                *
                **
                ***
                ****

'''
a=int(input("Enter the number of the Multiplication Table you would like to see: "))

for i in range(10):
    print(f"{a:<2} X {i+1:>2} = {(i+1)*a:>2}")