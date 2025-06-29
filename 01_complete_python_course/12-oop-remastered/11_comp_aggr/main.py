# class Hand:
#     def wave(self):
#         print("Waving form hand")

# class Body:
#     def run(self):
#         print("Running")
#         w = Hand()
#         w.wave()
        
# b = Body()
# b.run()

# class Hand:
#     def wave(self):
#         print("Waving form hand")

# class Body:
    
#     def __init__(self):
#         self.hand = Hand()
        
#     def run(self):
#         print("Running")
#         self.hand.wave()
        
# b = Body()
# b.run()


class Hand:
    def wave(self):
        print("Waving form hand")

class Body:
    
    def __init__(self,hand):
        self.hand = hand
        
    def run(self):
        print("Running")
        self.hand.wave()

hand = Hand()        
b = Body(hand)
b.run()

class Engine:
    def start(self):
        print("Engine started")
        
class SideMirrors:
    def set_mirror(self):
        print("Mirror is set")
        
        
class Car:
    def __init__(self,mirror):
        self.engine = Engine()
        self.mirror = mirror
        
    def start(self):
        self.engine.start()
        self.mirror.set_mirror()
        
sm = SideMirrors()        
mehran = Car(sm)
mehran.start()

class Singleton:
    
    var = None
    
    def __new__(cls):
        if cls.var is None:
            print("creating new class")
            cls.var = super().__new__(cls)
        else: 
            print("using old class")
            print(cls.var)
        return cls.var
    
s = Singleton()
d = Singleton()