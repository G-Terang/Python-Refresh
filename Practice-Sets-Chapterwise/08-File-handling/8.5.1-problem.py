'''
5. Bonus Challenges

    1.  Write a program that reads a file and creates another file with all words converted to uppercase.
    
    2.  Create a script that deletes all .tmp files from the current directory using os and os.remove() .
    
    3.  Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize() ).

'''

import os

directory = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder1'
file_input = "notes-2.txt"
file_output = "notes-2-UPPER.txt"

if os.path.exists(directory):
    try:
        path1 = os.path.join(directory, file_input)
        path2 = os.path.join(directory, file_output)
        with open(path1 , 'r') as file:
            content = file.read()
            
        content_upper = content.upper()
        
        with open(path2, 'w') as new_file:
            new_file.write(content_upper)
            
        print(f"The new file has been created with all uppercase letters.\nAnd both the files are in this directory :{directory}")
        
    except FileNotFoundError as error: 
        print("File not found!")
else:
    print("Directory does not exist!")
    
