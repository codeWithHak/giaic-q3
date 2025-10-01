# 7. Access Modifiers: Public, Private, and Protected

# Assignment:

# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    
    name = "Huzair"
    _salary = 1500000
    __ssn = 9898
    
obj1 = Employee()

# print public att name
print(obj1.name) # Huzair

# change the name attribute and print again
obj1.name = "huzaifa" # will be cahnged successfully
print(obj1.name) # huzaifa


# print protected att _salary
print(obj1._salary)

# change protected att and print again
obj1._salary = 2000000 # will be changed successfully
print(obj1._salary)



# -------- below is just my research --------
# print pricate att __ssn

try:
    print(obj1._Employee__ssn) # will throw an exception " AttributeError: 'Employee' object has no attribute '__ssn' "
    print(obj1.__ssn) # will throw an exception " AttributeError: 'Employee' object has no attribute '__ssn' "
    obj1.__ssn = 1111 # is this changing the ssn? why it is not throwing an error? 
    print(obj1.__ssn) # exception AttributeError
except AttributeError:
    print("Hence Proved 'AttributeError' is an Exception!")


try:
    x = int("abc")  # Raises ValueError
except (ValueError, AttributeError, NameError) as e:
    print(f"Caught an exception: {type(e)} - {e}")

print(issubclass(ValueError, BaseException))
print(issubclass(Exception, BaseException))
print(issubclass(NameError, Exception))

print(type(AttributeError))