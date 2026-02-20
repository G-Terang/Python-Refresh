class employee:
    company = "Assus" #This is a class attribute
    
    def __init__(self, salary, name, bond, company):  # __init__ by default means a constructor and it is used to initialize an object
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
        
    def get_salary(self): # self is important here because self is a way to reference the object of the class being created.
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is : {self.name}. Salary is {self.salary} and the bond is for {self.bond} years. ")


e1 = employee(120000, "Ganesh Terang", 5, "Turing,USA")
print(e1.company) #This will print the instance attribute whenever present but if the instance attribute is absent the class attribute will be printed.

print(employee.company) # This will always print the class attribute 


# Object introspection
print(dir(e1))



