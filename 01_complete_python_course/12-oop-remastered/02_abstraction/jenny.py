from abstract_class import Vehicle

class Super:
    pass

print(type(Super))
print(issubclass(type,object))

def add():
    pass

print(isinstance(add,object))

class Type(object):
    pass

my_class = Type()

print(isinstance(type,object))

s = Super()
print(type(s))
print(type(Super))