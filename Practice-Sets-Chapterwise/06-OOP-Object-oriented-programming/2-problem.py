'''
2. Constructor and Attributes
    Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes. Create an object and print the person’s name and age.
    
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        print(f"The name of the person is : {self.name} and age is : {self.age}")

person1 = Person("Ganesh Terang", 25)
person1.get_info()





















# Trying something out, this is not related to above problem's solution 
'''
class student:
    student_name = "ABC"
    student_age = 20
    student_marks = 90
    
std = student()
print(std.student_name)
print(std.student_age)
print(std.student_marks)

'''