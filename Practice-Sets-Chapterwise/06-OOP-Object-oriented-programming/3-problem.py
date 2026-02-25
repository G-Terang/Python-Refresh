'''
3. Simple Inheritance

    Create a base class Animal with a method sound() that prints "Some sound" .
    Create a derived class Dog that overrides sound() to print "Bark!" .
    Create an object of Dog and call sound() .

'''
class Animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

dog = Dog("Bruno")
dog.speak()