# 3. Public Variables and Methods

# Assignment:

# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.


# create a Car class
class Car:
    
    # an init method taht takes name
    def __init__(self,brand):
        self.brand = brand
    
    # a satrt method that prints car satrted
    def start(self):
        print(f"{self.brand} started")
        

# iniitalize both classes
corolla = Car("Corolla")
mehran = Car("Mehran")

# print brand names
print(corolla.brand)
print(mehran.brand)

# call start method
corolla.start()
mehran.start()
