'''

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_first_name = f"{first} {l[1]}"
        self.name = new_first_name
        return self.name
    
e1 = Employee("Ninja Terang", 66000)
print(e1.name)

e1.first_name = "Ganesh"
print(e1.name)
print(e1.first_name)

'''

'''

class Employee:
    company = "Hp"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    
    # Instance method
    def print_info(self):
        p = f"The name is {self.name} and salary is {self.salary}"
        print(p)
    
    # Static method
    @staticmethod
    def sum(a, b): #We will need self to execute this portion of code but since we are using staticmethod we no more need to pass self to run this portion of code, So staticmethod is a method where is does not need self and self is not passed automatically when we call this function
        return a + b
    
    #class method
    @classmethod
    def print_company(cls):
        print(cls.company)
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        return new_company
    
e1 = Employee("John", 50000)
e2 = Employee("Chena", 60000)

e1.print_info()
e2.print_info()

print(e2.sum(10,5))

e1.print_company()
e1.change_company("Google")

e1.print_company()

'''



# dunder method 

'''

class Employee:
    
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
    
    def __str__(self):
        return f"The name of the Employee is {self.name} and salary is {self.salary}"
    
    def __repr__(self):
        return f"name : {self.name}, salary : {self.salary}"
    
e1=Employee("Ganesh Terang", 120000)

print(e1.name, e1.salary)
print(str(e1))
print(repr(e1))

'''

# Exception handling 
'''

while True:
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print(f"This sum of {a} and {b} is : {a+b}")
        
    # except:
    #     print("Some error occured!")
    
    except ZeroDivisionError:
        print("Avoide dividing with 0")
        
    except ValueError:
        print("Do not type character kinldy!")
        
        
    except Exception as a :
        print("Some error occured!", a)
'''


'''


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if b ==0:
    raise ValueError("Please do not divide by 0")

print(f"This sum of {a} and {b} is : {a/b}")
'''


# else error 
'''
try:
    
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"Result is : {a/b}")
    
except Exception as a:
    print("There was an error ! ",a)
    
else:
    print("Hey I'm doing good. Thank you")

'''


# finally Error 

'''
try:
    
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"Result is : {a/b}")
    
except Exception as a:
    print("There was an error ! ",a)
    
finally:
    print("Hey I'm doing good. Thank you")
'''

# map functions in python 
'''

a = [1, 3, 4, 5, 7]
def square(x):
    return x*x
c = list(map(square, a))
print(c)
'''


# filter function in python 
'''

a = [11, 9, 3, 5,90, 20, 2, 1, 5, 13, 14, 51, 17]
# def is_greater(a):
#     if a>5:
#         return True
#     else: 
#         return False

new = list(filter(lambda x: x>5, a))
print(new)
'''


# use of reduce function 
'''

from functools import reduce 

a = [1,2,3,4,5]

b = reduce(lambda a,b: a+b , a)

print(b)

'''
