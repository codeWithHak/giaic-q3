def decorator_function(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@decorator_function
def greet():
    print("Hello")

greet()