# Class : Class is a blueprint or a template. Eg. Form for an Recruitment that contains name, age, position, father's name etc.

# Object : Specific instance created from the template (class). Eg. Form which contains the data for me or you

class employee:
    company = "HP"
    
    def get_salary(self): # self is important here because self is a way to reference the object of the class being created.
        return 34000
    

e1 = employee() # An object of class employee is created here.
print(e1.get_salary()) # employee e's get salry method is called

e2 = employee()
print(e2.get_salary())
print(e2.company)
