class employee:
    
    def __init__(self, salary, name, bond):  # __init__ by default means a constructor and it is used to initialize an object
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        
    def get_salary(self): # self is important here because self is a way to reference the object of the class being created.
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is : {self.name}. Salary is {self.salary} and the bond is for {self.bond} years. ")


e1 = employee(120000, "Ganesh Terang", 5)
print(e1.get_salary())
e1.get_info()