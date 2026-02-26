'''
3. Static & Class Methods

    1.  Create a class MathUtils with:
        1.  A @staticmethod called add(a, b) that returns a + b .
        2.  A @classmethod called description(cls) that prints "This is a utility class for math operations."
    
    2.  Call both methods without creating an object.


'''

class MathUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def add(a, b):
        return a+b
    
    @classmethod
    def description(self):
        print(f"This is a utility class for math operation.")

# by creating object 
# fist = MathUtils()
# print(fist.add(2,3))
# fist.description()


# without creating an object 
print(MathUtils.add(5,10))
MathUtils.description()