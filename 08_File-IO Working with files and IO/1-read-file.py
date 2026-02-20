#Reading the content of the file hello.txt

# f = open("f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello.txt", "r")
# content = f.read()
# print(content)

# f.close()





# updated code using try method


# try:
#     file=open("f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello.txt", "r")
#     content_of_the_file = file.read()
#     print(content_of_the_file)
#     file.close()
# except FileNotFoundError as e:
#     print(f"Error: File not found.\n{e}")
    
    
# Another updated code using try method to read the file content line by line.

try :
    file = open('f:/CODE PLAYGROUND/PYTHON/File-IO Working with files and IO/hello.txt','r')
    for line in file:
        print(line.strip())  #this will eventually remove the new lines.
    file.close
except FileNotFoundError as error:
    print(f"File is not found.\nThe error is : {error}")