# Exercise 1: Custom Calculator with *args
# Create a class Calculator that has a method add_numbers which takes any number of numeric arguments
# and returns their sum using *args.

class Calculator:
    
    def add_numbers(self,*args):
        self.args = args
        return sum(self.args)
    
c = Calculator()
# print(c.add_numbers(10,20,30))



# Exercise 2: Profile Generator with **kwargs
# Create a class UserProfile that takes any number of keyword arguments like name, age, email, etc.
# Store them in a dictionary and display the profile using a method show_profile.


class User_Profile:
    
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        
    def show_profile(self):
        print(self.kwargs)
    
u = User_Profile(name="huzair",age=19)
# u.show_profile()



# Exercise 3: Logger with Both *args and **kwargs
# Create a class Logger with a method log that accepts any number of messages (*args) and tags (**kwargs).
# Print the messages with optional tags like level="INFO" or source="System".

class Logger:
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def log(self):
        for i in self.args:
            print(i)
        
        for key,value in self.kwargs.items():
            print(f"{key} = {value}")
            
l = Logger('System Started', "Running Smoothly", level="INFO", source="SYSTEM")
l.log()
    