import os
import time 

path = "f:/CODE PLAYGROUND/PYTHON/Projects/7-file-organizer/"

n = int(input("Enter how many numbers of file you want to create in total (50% for file type .txt and 50% for file type .jpg): "))
for i in range(1,n//2):
    ext_txt = ".txt"
    filename_txt = f"{i}{ext_txt}"

    with open(path + filename_txt, 'w') as file:
        file.write(f"txt file number {i}")
        
print(f"Total {n//2} text file has been created.")
time.sleep(0.5)
        
for i in range(1, n//2):
          
    ext_jpg = ".jpg"
    filename_jpg = f"{i}{ext_jpg}"
    
    with open(path + filename_jpg, 'w') as file:
        file.write("")
        
print(f"Total {n//2} photo file has been created.")
time.sleep(0.5)
        
        
print("Loading", end="", flush=True)

for _ in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

print(f" Done! A total of {n} file has been created. {n//2} of text file and {n//2} of image files")