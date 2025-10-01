# 9. Abstract Classes and Methods

# Assignment:

# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
        
obj1 = Rectangle(10,20)
print(obj1.area())