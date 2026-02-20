'''
Q6. Little tough Questions

    1.  Write a program that counts how many vowels are in a given string.
    2.  Take a user input string and check if it is a palindrome (same forwards and backwards).

'''

string = input("Enter a word to check wheather it is palindrome or not: ")
revered_string = string[::-1]
print(f"The word you entered is : {string}")
print(f"The word after reversing is {revered_string}")

if string == revered_string:
    print(f"'{string}' after reversing is '{revered_string}' therefore it is a PALINDROME")
else:
    print(f"Since the word you entered '{string}' after reversing is '{revered_string}' and is not the same therefore it is NOT a PALINDROME")
