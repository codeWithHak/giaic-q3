# duck typing
class Bird:
    
    def __init__(self,name):
        self.name = name
    
    def fly(self):
        print(f"A {self.name} is Flying")
        
        
class Plane:
    
    def __init__(self,name):
        self.name = name
    
    def fly(self):
        print(f"A {self.name} is Flying")
        
def check_duck(name):
    return name.fly()

check_duck(Bird("duck"))
check_duck(Plane("J10C"))



# __new__

first_name,last_name = ("john","doe")
print(first_name)
print(type(first_name))
print(last_name)
print(type(last_name))

