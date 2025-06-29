class Car:
    
    def __init__(self):
        
        self.key = False
        self.clutch = False
        self.engine = False
        
    def start(self):
        self.key = True
        self.clutch = True
        self.engine = True
        print("Car started")
        
mehran = Car()
mehran.start() 