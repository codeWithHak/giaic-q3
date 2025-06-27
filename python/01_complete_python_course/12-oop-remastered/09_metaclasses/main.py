class Meta(type):
    def __new__(cls,*args,**kwargs):
        print("Class created")
        return super().__new__(cls,*args,**kwargs)
    
class MyClass(metaclass=Meta):
    pass

class NewClass(metaclass=Meta):
    pass
    
class TypeClass:
    pass

class AnotherClass(metaclass=Meta):
    pass

m = MyClass()
n = NewClass()

t = TypeClass()