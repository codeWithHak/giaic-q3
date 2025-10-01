# 13. Composition

# Assignment:

# Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

# an engine class
class Engine:
    
    def sieze(self):
        print("Engine siezed")

# a car that has engine init                
class Car:
    
    # initialize car object with engine
    def __init__(self):
        self.car = Engine()
    
    # a repair method that calls a m seize
    def repair(self):
        self.car.sieze()
        print("Please repair")
        
obj1 = Car()
obj1.repair()