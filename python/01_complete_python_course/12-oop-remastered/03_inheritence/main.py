class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
  
# p = Person('huzaifa',20)        
# print(type(p))
# e = Employee("huzair",25,2)
# print(type(e))
# print(e.employee_id)
# print(e.name)



# Add a method say_hello() in Person that prints "Hello, I'm [name]"
# In Employee, override say_hello() to also say "and my ID is [employee_id]"

# Use super() in the overridden method to call the original one first.

class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, I'm {self.name}")    
        

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    
    def say_hello(self,):
        super().say_hello()
        print(f"and my ID is {self.employee_id}") 
        
# e = Employee("huzair",20,2)
# e.say_hello()




# Add a new class Manager that inherits from Employee and adds a team_size

# Use super() in Manager to initialize everything properly

class Manager(Employee):
    def __init__(self,name,age,employee_id,team_size):
        super().__init__(name,age,employee_id)
        self.team_size = team_size
    def say_hello(self):
        super().say_hello()
        print(f"and i manage a team of {self.team_size} people")
        
# m = Manager("huzair",18,1,99)
# print(m.name)
# print(m.age)
# print(m.employee_id)
# print(m.team_size)
# m.say_hello()



# Modify the Employee and Manager classes from before
# Instead of explicitly writing parameters, use *args and **kwargs to pass them around

# Create a Manager instance and make sure all attributes are still set



class Employee(Person):
    def __init__(self,*args,employee_id,**kwargs):
        super().__init__(*args, **kwargs)
        self.employee_id = employee_id
    
    def say_hello(self,):
        super().say_hello()
        print(f"and my ID is {self.employee_id}") 

class Manager(Employee):
    def __init__(self,*args, team_size, **kwargs):
        super().__init__(*args, **kwargs)
        self.team_size = team_size
    def say_hello(self):
        super().say_hello()
        print(f"and i manage a team of {self.team_size} people")
        
        
m = Manager("huzair",18,employee_id = 1,team_size = 99)
# print(m.name)
# print(m.age)
# print(m.employee_id)
# print(m.team_size)
# m.say_hello()


class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can mimic a duck!")

def make_it_quack(thing):
    thing.quack()  # No type check!

d = Duck()
p = Person()
make_it_quack(d)    # Output: Quack!
make_it_quack(p)  # Output: I can mimic a duck!