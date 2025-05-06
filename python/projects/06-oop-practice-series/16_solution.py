# 16. Function 

# Assignment:

# Write a decorator function log_function_call that prints "Function is being called"
# before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is bieng called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("hello world")
    
say_hello = log_function_call()