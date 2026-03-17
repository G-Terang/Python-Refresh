import os
if os.path.exists("notes.txt"):
    try:
        os.rename("notes.txt", "notes-2.txt")
    except FileExistsError as Error:
        print(f"Some error occured! {Error}")
else:
    print("File does not exist!")
        