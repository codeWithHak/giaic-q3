def decorator_function(func):
    def wrapper(*args,**kwargs):
        print("Hello")
        func(*args,**kwargs)
        print("Thanks for coming")
    return wrapper

@decorator_function
def greet(name):
    print("Welcome", name)

greet("Huzair")