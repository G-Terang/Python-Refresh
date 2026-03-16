'''

2. Read, Write, and Append Files

    1.  Write a program that writes three lines of text to a file tasks.txt .
    2.  Open tasks.txt in append mode and add a new line "Task Completed!" .
    3.  Read the file and print all lines as a list using readlines() .
    
'''

file_path = '/Users/terang/CODING/PLAYGROUND/Python-Refresh/Practice-sets-Chapterwise/08-File-handling/tasks.txt'

try:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        print(lines)

except FileNotFoundError as Error:
    print(f"File is not found! Error : {Error}")