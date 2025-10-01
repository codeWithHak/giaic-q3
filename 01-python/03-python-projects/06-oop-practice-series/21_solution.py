# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__()
# to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self):
        self.start = 10
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= 1:
            val = self.start
            self.start -= 1
            return val
        else:
            raise StopIteration
    
c = Countdown()

for i in c:
    print(i)