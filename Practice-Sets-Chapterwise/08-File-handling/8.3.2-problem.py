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


import shutil

try:
    path1 = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder1/file1.txt'

    path2 = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder2/file1-copy.txt'

    shutil.copy(path1, path2)
    
except FileExistsError as error :
    print("Error occured, Error is : ",error)
    


'''

import os
import shutil

path1 = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder1/file1.txt'
path2 = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder2/file1-copy.txt'

# Ensure directories exist
os.makedirs(os.path.dirname(path1), exist_ok=True)
os.makedirs(os.path.dirname(path2), exist_ok=True)

# Create a sample source file if it doesn't exist
if not os.path.exists(path1):
    with open(path1, 'w', encoding='utf-8') as f:
        f.write('Sample content\n')

try:
    shutil.copy(path1, path2)
    print(f"Copied {path1} to {path2}")
except Exception as error:
    print("Error occurred:", error)

'''