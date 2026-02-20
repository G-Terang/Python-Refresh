'''
4. While Loops
    1.  Print numbers from 1 to 10 using a while loop.
    2.  Write a program that keeps asking the user to enter a password until they enter the correct one.
    3.  Use a while loop to reverse a given number (e.g., 123 → 321).
'''

password = input("Kindly enter your password : ")
while password != 'Mango':
    password = input("Incorrect!\nKindly enter your password again : ")
    if password == 'Mango':
        print("Correct Password.")