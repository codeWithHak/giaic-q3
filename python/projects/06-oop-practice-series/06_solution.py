# 6. Constructors and Destructors

# Assignment:

# Create a class Logger that prints a message when an object is created (constructor)
# and another message when it is destroyed (destructor).

class Logger():
    def __init__(self):
        print("A new conctructor is created")
        
    def __del__(self):
        print("Constructor deleted")
        
obj1 = Logger()    

del obj1
    