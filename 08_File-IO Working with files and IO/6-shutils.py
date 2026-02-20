import shutil


# deleting a directory using shutil.mrtree is very dangerous so i have commented out this line 
# shutil.rmtree('f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\dir-delete')

# this for coping a file.
'''
n=int(input("Enter how many copies of the file you want to make : "))

for i in range(n):
    shutil.copy(r'f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\hello2.txt', f'f:\\CODE PLAYGROUND\\PYTHON\\File-IO Working with files and IO\\hello2-copy{i}.txt')
'''
source_path = 'f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO'
destination_path = 'f:\CODE PLAYGROUND\PYTHON\File-IO Working with files and IO\dir'
shutil.move(f'{source_path}\hello2-copy0.txt', f'{destination_path}')