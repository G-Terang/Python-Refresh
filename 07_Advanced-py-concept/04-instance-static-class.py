class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
    
    
    # Instance method (default method)
    def print_info(self):
        f=f"The name of the employee is : '{self.name}' and the salary is {self.salary}"
        print(f)
        
    # Static Method 
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class Method 
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        return cls.company

e1 = Employee("Jack", 45000)
e2 = Employee("Jill", 55000)

print(e1.company)
# print(Employee.name) # This is throw error 
print("\nInstance Method -->")
e1.print_info()
e2.print_info()

print("\nStatic Method -->")
print(e1.sum(40, 50))

print("\nClass Method -->")
print("Before changing, the company name was :")
e1.print_company()
e1.change_company("Tesla")
print("After changing, the company name is :")
e1.print_company()