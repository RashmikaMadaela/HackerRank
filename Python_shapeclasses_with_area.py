#Python — Shape Classes with Area

"""Summary: Implement two classes, Rectangle and Circle, each with an area method. The Rectangle class takes two arguments (length and width) 
and calculates the area. The Circle class takes the radius as an argument and calculates the area using the constant math.pi."""

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
rectangle1 = Rectangle(3, 4)
print(rectangle1.area()) # 12

circle1 = Circle(5)
print(circle1.area()) # 78.53981633974483