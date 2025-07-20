"""
Python class methods-The behavior of objects made from that class 
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def display_area(self):
        print(f"Area of rectangle: {self.base * self.height} square units.")


new_rectangle = Rectangle(12, 111)
new_rectangle.display_area()

