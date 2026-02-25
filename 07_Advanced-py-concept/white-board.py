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