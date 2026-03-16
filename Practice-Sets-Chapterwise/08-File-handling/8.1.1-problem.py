'''
1. File I/O Basics

    1.  Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
    
    2.  Open notes.txt , read its content, and print it to the console.
    
'''


# write the file (remove the invalid 'cd:' prefix) and then read & print its contents
file_path = '/Users/terang/CODING/PLAYGROUND/Python-Refresh/Practice-Sets-Chapterwise/08-File-handling/notes.txt'


with open(file_path, 'w') as f:
    f.write("Learning Python is fun!")
