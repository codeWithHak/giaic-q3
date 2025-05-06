    # Create a custom exception InvalidAgeError.
    # Write a function check_age(age) that raises this exception if age < 18.
    # Handle it with try...except.

class InvalidAgeError(Exception):
    
    def __init__(self,age):
        self.age = age
        super().__init__(f"Exception Raised: Invalid age! Age must be in positive integers.")
        
def check_age(age):
        if age < 18:
            raise InvalidAgeError(age)
        else:
            print(f"Allowed")
            
try:
    check_age(-10)
except InvalidAgeError as e:
    print(e)