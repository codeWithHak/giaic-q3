# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18.
# Handle it with try...except.

class InvalidAgeError(Exception):
    
    def __init__(self,age):
        self.age = age
        super().__init__(f"invalid age! Age must be in positive integers.")
        
def set_age(age):
    if age > 0:
        self.age = age
        print(f"age is now {age}")
    else:
        raise InvalidAgeError(age)
    
set_age(-10)