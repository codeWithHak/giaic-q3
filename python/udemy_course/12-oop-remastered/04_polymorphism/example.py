# operator
print(10 + 10)
print("hello " + "world")

class Duck:
    def speak(self):
        print("quack quack")
        
class Dog:
    def speak(self):
        print("woof woof")
        

def display(duck):
    duck.speak()
    
d = Dog()
display(d)