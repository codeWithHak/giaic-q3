class Multiplier:
    def __init__(self,number):
        self.number = number
        
    def __call__(self,other):
        return self.number * other
    

double = Multiplier(10)
print(double(10))

class Property:
    @property
    def greet(self):
        print("Hello")
        
p = Property()
p.greet