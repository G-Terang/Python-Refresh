class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def first_name(self):
        l = self.name.split(' ')
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(' ')
        new_name = f"{first} {l[1]}"
        self.name=new_name
    
    
employee = Employee("John Terang", 120000)

print(employee.first_name)
employee.first_name = 'Ganesh'
print(f"Name of the employee is : {employee.name} and salary is : {employee.salary}/month")
