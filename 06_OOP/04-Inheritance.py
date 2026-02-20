class Animal:
    location = "Austrelia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking now....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class and this super() allows us to do it.
        print("Woof!")
        
# class Cat(Animal):
#     def speck(self):
#         print("Meow")


# a = Animal()
# a.speck()

d = Dog("Bruno")
d.speak()
print(d.location)