class  Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    # we can cahnge the value of a private attribute by a method
    def change_age(self,age):
        self.__age = age
        
    # we can see private attrivutes outside the class with methods    
    def get_age(self):
        return self.__age
    
man = Person('huzair',22)
print(man.name)
print(man.name)

# getting the value of age which is a private attribute
print(man.get_age())

# cahnging the value of age which is a private attribute
man.change_age(33)
print(man.get_age())
