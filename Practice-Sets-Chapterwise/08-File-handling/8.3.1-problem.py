'''
3. OS and Shutil Modules

    1.  Use the os module to:
        1.  Print the current working directory
        2.  List all files and folders in the current directory
        3.  Create a new folder my_folder
        
    2.  Use the shutil module to:
        1.  Copy a file from one folder to another
        2.  Move a file to a new folder
        3.  Delete a file (careful: irreversible!)
'''

import os

#Printing the current working directory
a = os.getcwd()
print(f"\nThis is the current working directory: {a}")

# List all files and folders in the current directory
print(f"\nList all files and folders in my current directory: {os.listdir()}")


# Create a new folder my_folder
os.mkdir('Practice-Sets-Chapterwise/08-File-handling/my_folder')