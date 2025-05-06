# 17. Class Decorators

# Assignment:

# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.

class Decorator:
    
    def add_greeting(cls):
        def greet(self):
            print("Hello from Decorator!")
            
        cls.greet = greet
        return cls

@Decorator.add_greeting
class Person:
    pass

obj1 = Person()
obj1.greet()