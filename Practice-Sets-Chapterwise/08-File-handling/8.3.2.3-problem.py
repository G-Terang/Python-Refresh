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

# simple way 

'''
import os

try:
    path1 = 'Practice-Sets-Chapterwise/08-File-handling/my_folder/folder1/delete.bat'

    os.remove(path1)
    
except FileExistsError as error :
    print("Error occured, Error is : ",error)

'''
    


# more accurate way of doing it 
import os

try:
    directory = "Practice-Sets-Chapterwise/08-File-handling/my_folder/folder1"
    filename = "delete.bat"

    path = os.path.join(directory, filename)

    os.remove(path)

except FileNotFoundError as error:
    print("Error occurred, Error is:", error)
