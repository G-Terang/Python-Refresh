'''
Q3. String Methods and Functions

    1.  Take the string " i love python programming " and:
        1.  Remove extra spaces from both ends
        2.  Convert it to title case
        3.  Count how many times "o" appears
        
    2.  Check if the string "123abc" is alphanumeric.

'''

string = " i love python programming "

# Task 1
stripped = string.strip()
title_case = stripped.title()
o_count = string.count("o")

print(f"Original: '{string}'")
print(f"Stripped: '{stripped}'")
print(f"Title case: '{title_case}'")
print(f"Count of 'o': {o_count}")

# Task 2
test_string = "123abc"
is_alphanumeric = test_string.isalnum()
print(f"Is '{test_string}' alphanumeric? {is_alphanumeric}")
