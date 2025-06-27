class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def print(self):
        print(f"{self.name} is {self.age} years old")
        
    def is_underage(self):
        # return True if self.age < 18 else False
        return self.age < 18
        
    def print_name(self):
        print(self.name)

john = Person("john",20)
smith = Person("smith",10)
   
print(john.is_underage())
print(smith.is_underage())