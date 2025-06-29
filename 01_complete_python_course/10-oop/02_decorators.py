class Person:
    def __init__(self,name):
        self.name = name
       
    @staticmethod   # decorator
    def print_hello():
        print("Hellooo")
        

huzair = Person("Huzair")
huzair.print_hello()