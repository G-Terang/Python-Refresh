#While using with open we do not need to close a file, since it is already closed by default

# with open("f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello.txt", 'r') as file:
#     content = file.read()
#     print(content)
    
    
# using try 
try :
    with open("f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello2.txt", 'r') as file:
        for line in file:  
            print(line.strip())
except FileNotFoundError as e: 
    print(f"{e}\nError: File not found.")