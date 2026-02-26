'''
Q2. Getters and Setters

    1.  Create a class Employee with a private attribute _salary .
    
        1.  Use @property to define a getter for salary .
        2.  Use @salary.setter to prevent setting negative values (print a warning instead).
        3.  Create an object and test by setting positive and negative salaries.


'''


class Employee:
    def __init__(self, salary):
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if(value<0):
            print("Do not set a negative value.")
        else:
            self._salary = value
            
emp = Employee(34)
emp.salary = -12
print(emp.salary)
    