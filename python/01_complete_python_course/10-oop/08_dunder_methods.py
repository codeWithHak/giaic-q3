# create your owno len function

# dunder methods are used to change the default behaviuor of python's default function

# diuble underscore = dunder

class Person:
    name = "huzair"
    
    def __len__(self):
        n = 0
        for i in self.name:
            n = n + 1
        return n
    
obj1 = Person()
print(obj1.name)
print(len(obj1))