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
total = 0
for i in range(100):
    total += i+1
print(f"The sum of all the numbers from 1 to 100 is : {total}")
    