# create a class attribute

"""class Person:
    name = "huzair"
    
    # a method to change the class attribute but it wont work
    # instead a new object attribute name will be created and changed, and the class attribute will remain same
    def change_name(self,name):
        self.name = name

# create and instance of Person
person1 = Person()

# print instance name
print(person1.name) # huzair

# call the change name method
person1.change_name("Khizar") 
print(person1.name) # khizar

# print Person class name
print(Person.name) # still huzair, because this is a class attribute and you changed object attribute
"""

# --- Different ways to change class attributes ---

# 1- change directly in a method like Class.attribute = attribute
# 2- use __class__.name instead of using class name directly like Person.name
# 3- use @classmethod - thsi is the best way

class Person:
    name = "huzair"
    
    def change_name(self,name):
        
        # 1- change the class attribute directly  
        Person.name = name
        
        # 2- use __class__ for changing class attribute
        self.__class__.name = name
        
    
    # 3- use @staticmethod
    @classmethod
    def changeName(cls,name):
        cls.name = name            

person1 = Person()
# before - huzair in both print statements        
print(person1.name)
print(Person.name)

# called the change_name method and passed khalid as name
person1.changeName("khalid")

# after - khalid in both print statements
print(Person.name)
print(person1.name)

