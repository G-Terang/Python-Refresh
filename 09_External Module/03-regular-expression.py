import re

line = 'The quick brown dog jumps over the lazy dog. Brown dogs, Brown guy like me.'


#This is to find the first matching occurence.
match = re.search('brown', line)
if match :
    print("Match is found")
    print("Starting index is : ",match.start())
    print("Ending index is : ",match.end())
    
    
# this is to find all the occurences ignoring the cases (uppercase or lowercase)
all_matches = re.findall('brown', line, re.IGNORECASE)
print(all_matches)


#This is to replace or sub all the occurences 
new_line = re.sub('dog', 'cat', line)
print("The new line is : ", new_line)