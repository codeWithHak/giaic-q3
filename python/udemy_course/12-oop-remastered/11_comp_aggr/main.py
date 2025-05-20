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