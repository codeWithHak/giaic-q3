# TODO:
# 1. Create a class `Logger`.
# 2. Override both `__new__()` and `__init__()`.
# 3. Print messages inside each to show execution order.
# 4. Create an object and see which method runs first.

class Logger:
    def __new__(cls):
        print("Object created")
        return super().__new__(cls)
    
    def __init__(self):
        print("Object initialized")
    
# l = Logger()


# -------------------------------------------------------------

# TODO:
# 1. Create class `Ghost`.
# 2. In `__new__()`, print a message and return None.
# 3. Add a print in `__init__()` too.
# 4. Try creating an instance and observe what happens.
#    Does __init__() run?
class Ghost:
    def __new__(cls):
        print("Object created")
        
    def __init__(self):
        print("This will not run")
        
g = Ghost()