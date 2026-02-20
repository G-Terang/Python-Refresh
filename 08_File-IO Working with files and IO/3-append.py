f = open('f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello2.txt', 'a')

content = '''


Use of append fn for file i/o in Python: 
This is another new line added later using the apend function() of the python. '''

f.write(content)

f.close()