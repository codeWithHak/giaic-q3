# initialize your first class
class Person:
    pass

# reate an object
p1 = Person()

# add an attribute "name" to p1
# p1.name = 'john'
# print(p1.name)


# create a constructor
class Teacher:
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print(self.name, self)
        
hamzah = Teacher("Hamzah", age=24)
print(hamzah.name)
print(hamzah.age)

huzair = Teacher("Huzair", age=19)
print(huzair.name)
print(huzair.age)


# class Teacher:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name, self)
        
# hamzah = Teacher("Hamzah", age=24)
# print(hamzah.name)
# print(hamzah.age)

# huzair = Teacher("Huzair", age=19)
# print(huzair.name)
# print(huzair.age)