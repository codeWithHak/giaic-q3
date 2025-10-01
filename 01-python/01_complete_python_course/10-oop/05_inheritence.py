class Car:
    
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car started!")
    
    @staticmethod
    def stop():
        print("Car stopped...")            
        
        
class ToyotaCar(Car):
    
    def __init__(self,name,type):
        self.name = name
        self.type = type
        
car1 = ToyotaCar("Corolla","electric")
print(car1.name)

car1.start()
print(car1.type)