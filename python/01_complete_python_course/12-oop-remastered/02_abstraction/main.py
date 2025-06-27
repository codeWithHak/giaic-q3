from abc import ABC,abstractmethod
from math import pi

# Task: Complete the implementation using abc module and test all shapes with their area() methods.

# Fill in the missing parts to make this code work using abstraction

class Shape(ABC):
    # Make this class abstract and add abstract method area
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # implement area method
    def area(self):
        return pi * (self.radius**2)
        
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # implement area method
    def area(self):
        return self.length * self.width
        
# r = Rectangle(20,20)
# print(r.area())

# c = Circle(20)
# print(c.area())


# Q4. File System (Abstraction)
# Create an abstract class File with:

# Abstract methods: open(), read(), close()

# Concrete subclasses: TextFile, PDFFile, CSVFile that implement
# those methods differently (print what each method does)

class File(ABC):
    
    @abstractmethod
    def open():
        pass
    
    @abstractmethod
    def read():
        pass
    
    @abstractmethod
    def close():
        pass
    
class TextFile(File):
    def open(self):
        print("Opened text File")
    
    def read(self):
        print("Read Text File")
        
    
    def close(self):
        print("Closed Text File")
        


class PDFFile(File):
    def open(self):
        print("Opened PDF File")
        
    
    def read(self):
        print("Read PDF File")
        
    
    def close(self):
        print("Closed PDF File")
        


class CSVFile(File):
    def open(self):
        print("Opened CSV File")
        
    
    def read(self):
        print("Read CSV File")
        
    
    def close(self):
        print("Closed CSV File")
        
    
# tf = TextFile()
# csv = CSVFile()
# pdf = PDFFile()

# tf.open()
# csv.open()
# pdf.open()