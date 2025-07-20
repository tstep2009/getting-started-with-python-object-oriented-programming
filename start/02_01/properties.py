"""
Python class properties
"""

class Rectangle: # Template for Rectangle (Create a base value and height value )
    def __init__(self, base, height): # class definition (AKA the constructor)
        self.base = base
        self.height = height

# Create an instance called new_rectangle (object of the class rectangle )
new_rectangle = Rectangle(12, 10) # 12 and 10 are the parameters to be alocate via the constructor

print(new_rectangle.base) # Use dot notation to access the constructor-base property or attribute 
print(new_rectangle.height)

new_rectangle.base = 5 # Override original parameters for base

print() # no parameters were passed 
print(new_rectangle.base) 

