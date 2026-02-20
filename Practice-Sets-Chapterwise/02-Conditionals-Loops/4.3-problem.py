'''
4. While Loops
    1.  Print numbers from 1 to 10 using a while loop.
    2.  Write a program that keeps asking the user to enter a password until they enter the correct one.
    3.  Use a while loop to reverse a given number (e.g., 123 → 321).
'''
num = int(input("Enter a number to reverse it like 123 to 321 : "))
print(f"The number you have entered is : {num}")
rev_num = 0
while num != 0:
    if num == 0:
        print("Kindly do not enter 0.")
    else:
        digit = num%10
        rev_num = rev_num*10 + digit
        num//=10
print(f"The reversed number is : {rev_num}")