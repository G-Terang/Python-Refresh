'''
5. Bonus Challenges

    1.  Write a program that reads a file and creates another file with all words converted to uppercase.
    
    2.  Create a script that deletes all .tmp files from the current directory using os and os.remove() .
    
    3.  Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize() ).

'''

import os
import sys

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size = os.path.getsize(file_path)
            except OSError:
                print(f"File could not acces {file_path}")
    return total_size

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python folder_size.py <folder_path>")
        sys.exit(1)
    
    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print("Invalid folder path!")
        sys.exit(1)
    
    size = get_folder_size(folder)
    print(f"The total size of the files in the folder '{folder}' is : {size} byte.")
            
    