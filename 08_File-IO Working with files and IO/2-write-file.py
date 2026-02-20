f = open("f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello2.txt", 'w')

content = '''Hi, This is Ganesh Terang.
I am a Python Developer in a company based in the NYC, USA
I get paid 300000 USD a year.
'''
lets_write = f.write(content)
print(lets_write)
f.close() 