class Employee:
    company = "Google"
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def __str__(self):
        return f"The name of the employee is : {self.name} and salary per month is : {self.salary}"
    
    def __repr__(self):
        return f"Name : {self.name}, Salary : {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
    def __add__(self,other):
        total_earnings = self.salary + other
        return total_earnings
    
    def __sub__(self, other):
        total_savings = self.__add__(other) - other
        return total_savings
    
    
    
e1 = Employee("Ganesh Terang", 86500)
print(e1.name, e1.salary)
print(str(e1))
print(repr(e1))
print(len(e1))
print(e1 + 20000)
print(e1-10000)