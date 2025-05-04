# 14. Aggregation

# Assignment:

# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self,name):
        self.name = name
        
    def welcome(self):
        print(f"Welcome to {self.name} department")

class Employee:
    
    def __init__(self,name,department):
        self.name = name
        self.obj_department = department
        
    def greet(self):
        print(f"Helllo {self.name}")
        self.obj_department.welcome()    
        
department = Department("IT")
emp = Employee("Huzair",department=department)

emp.greet()
