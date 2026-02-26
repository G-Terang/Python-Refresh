'''
7. Walrus Operator

    1.  Use the walrus operator to read input until the user enters "quit" . Print each input as it is entered.
    2.  Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.
    
'''
# Solusion number 2

words = ["python", "rocks", "ai"]

lengths = [length for word in words if(length:= len(word))>=4]
print(lengths)