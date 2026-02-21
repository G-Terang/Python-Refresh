'''
There are two types of modules in python
    1. Build in modules 
    2. External modules
    
    List of all the build in modules : https://docs.python.org/3/py-modindex.html

'''
import math
# import os 
import mymodule
import requests

print(math.sqrt(16))

# importing mymodule that i previously created.
mymodule.hello()

#using an external module that i previously installed with pip install method 
r = requests.get("https://www.google.com")
print(r.text)