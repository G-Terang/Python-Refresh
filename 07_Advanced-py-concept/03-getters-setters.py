class employee:
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
    
    
    # Lets change and split the first name, last name as well
    @property
    def first_name(self):
        l = self.name.split(' ')
        print(l) # This is to print in the list
        return l[0] # This will return the first name
    
    
    # Let's change the first name 
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(' ')
        new_first_name = f"{first} {l[1]}"
        self.name = new_first_name

e = employee("Michel Jackson", 50123)
# e.project = 10
# print(e.project)

# print(e.first_name())



# first = "Michel Jr."
# e.set_first_name(first)
# print(e.name)

print(e.first_name)
e.first_name = "Jr. Michel"
print(e.name)