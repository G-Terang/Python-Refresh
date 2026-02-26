'''
Q4. Magic/Dunder Methods

    1.  Create a class Book with attributes title and author .
        1.  Implement __str__() so that printing the object displays "Title by Author" .
        2.  Implement __len__() so that len(book) returns the length of the title.
        
    2.  Create two Book objects and test these methods.

'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Titled by author : {self.author}"
        
    def __len__(self):
        return len(self.title)
    
    

book1 = Book("ZERO to Mastery in Python Programming.", "Ganesh Terang")
print(book1)
print(f"The lenght of the title is : {len(book1)}")


book2 = Book("ZERO to Mastery in Python Programming VOL - II", "Ganesh Terang VOL - II")
print(book2)
print(f"The lenght of the title is : {len(book2)}")