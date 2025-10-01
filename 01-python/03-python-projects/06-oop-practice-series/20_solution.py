    # Create a custom exception InvalidAgeError.
    # Write a function check_age(age) that raises this exception if age < 18.
    # Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self,age):
        self.age = age
        return super().__init__(f"Exception Raised: Age is less then 18! - {age}")
    
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is greater then 18")
        
check_age(17)