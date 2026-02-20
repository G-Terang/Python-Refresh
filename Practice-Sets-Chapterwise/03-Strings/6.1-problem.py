'''
Q6. Little tough Questions

    1.  Write a program that counts how many vowels are in a given string.
    2.  Take a user input string and check if it is a palindrome (same forwards and backwards).

'''
string = '''
1.  Write a program that counts how many vowels are in a given string.
2.  Take a user input string and check if it is a palindrome (same forwards and backwards).
'''

a = string.count('a')
e = string.count('e')
i = string.count('i')
o = string.count('o')
u = string.count('u')

print(f"The string I took is :{string}\nAnd there are vowel occurences : ")
print(f"a = {a} times")
print(f"e = {e} times")
print(f"i = {i} times")
print(f"o = {o} times")
print(f"u = {u} times")

total  = a + e + i + o + u
print(f"Therefore the total number of vowel occurences is : {total}")