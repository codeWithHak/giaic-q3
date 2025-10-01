# 10. Instance Methods

# Assignment:

# Create a class Dog with instance variables name and breed.
# Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Come on", self.name)    
        

dog1 = Dog('tommy', "bull dog")
print(dog1.name)
dog1.bark()