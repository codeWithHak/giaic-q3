# operator
print(10 + 10)
print("hello " + "world")

# with a function
class Duck:
    def speak(self):
        print("quack quack")
        
class Dog:
    def speak(self):
        print("woof woof")
        

def display(duck):
    duck.speak()
    
d = Duck()
display(d)


# with class
class Duck:
    def speak(self):
        print("quack quack")
        
class Dog:
    def speak(self):
        print("woof woof")
        
class Display:
    def display(self,duck):
        duck.speak()
    
obj = Dog()
d = Display()
d.display(obj)