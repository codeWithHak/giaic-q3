# Task: Modify the class to hide marks and provide proper getter/setter methods with validation
# (e.g. marks must be between 0–100).
from abc import ABC,abstractmethod
from math import pi

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
        
    def set_marks(self,marks):
        if (marks > 0 and marks < 100):
            self.__marks = marks
            
    def get_marks(self):
        return f"Marks: {self.__marks}"

    def display(self):
        print(f"{self.name} scored {self.__marks}")

# std1 = Student("Huzair", 98)
# print(std1.get_marks())
# std1.set_marks(70)
# print(std1.get_marks())




# ❓ Task: Complete the implementation using abc module and test all shapes with their area() methods.



# Fill in the missing parts to make this code work using abstraction

class Shape(ABC):
    # Make this class abstract and add abstract method area
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # implement area method
    def area(self):
        return pi * (self.radius**2)
        
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # implement area method
    def area(self):
        return self.length * self.width
        
# r = Rectangle(20,20)
# print(r.area())

# c = Circle(20)
# print(c.area())




# Q3. Banking System (Encapsulation)
# Design a BankAccount class:

# Private attributes: __balance

# Methods:

# deposit(amount)

# withdraw(amount)

# get_balance()

# Validate all inputs: no negative deposits/withdrawals, no overdrafts

# Bonus: Add logging of every transaction using a list __transactions

class BankAccount:
    def __init__(self,balance):
        
        self.__balance = balance
        self.__transactions = {'deposit':[],'withdraw':[]}
        
            
    def deposit(self,amount):
        
        if amount > 0:
            self.__balance += amount
        
            self.__transactions['deposit'].append(amount)
        
            return "Deposited",amount
        
        else:
            return "Invalid amount"
        
        
    def withdraw(self,amount):
        if amount > 0:
            self.__balance -= amount
            
            self.__transactions['withdraw'].append(amount)
            
            return amount, "withdrawn"
        
        else:
            return "Invalid amount"
        
    def get_balance(self):
        return f"Current balance: {self.__balance}"
    
    def list_transactions(self):
        
        print("\nDeposit Transactions")
        for index,d in enumerate(self.__transactions['deposit']):
            print(f"{index+1} - {d}")
        
        print("\nWithdraw Transactions")
        for index,w in enumerate(self.__transactions['withdraw']):
            print(f"{index+1} - {w}")
    
# acc1 = BankAccount(100)
# print(acc1.get_balance())        
# acc1.deposit(2000)
# acc1.deposit(1000)
# print(acc1.get_balance())        
# acc1.withdraw(2000)
# acc1.withdraw(1000)
# print(acc1.get_balance())        
# print(acc1.list_transactions())        
    
    
# Q4. File System (Abstraction)
# Create an abstract class File with:

# Abstract methods: open(), read(), close()

# Concrete subclasses: TextFile, PDFFile, CSVFile that implement
# those methods differently (print what each method does)

class File(ABC):
    
    @abstractmethod
    def open():
        pass
    
    @abstractmethod
    def read():
        pass
    
    @abstractmethod
    def close():
        pass
    
class TextFile(File):
    def open(self):
        print("Opened text File")
    
    def read(self):
        print("Read Text File")
        
    
    def close(self):
        print("Closed Text File")
        


class PDFFile(File):
    def open(self):
        print("Opened PDF File")
        
    
    def read(self):
        print("Read PDF File")
        
    
    def close(self):
        print("Closed PDF File")
        


class CSVFile(File):
    def open(self):
        print("Opened CSV File")
        
    
    def read(self):
        print("Read CSV File")
        
    
    def close(self):
        print("Closed CSV File")
        
    
# tf = TextFile()
# csv = CSVFile()
# pdf = PDFFile()

# tf.open()
# csv.open()
# pdf.open()


# Excercise 1

class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
  
        
# p = Person('huzaifa',20)        
# print(type(p))
# e = Employee("huzair",25,2)
# print(type(e))
# print(e.employee_id)
# print(e.name)

# Excercise 2

# Add a method say_hello() in Person that prints "Hello, I'm [name]"
# In Employee, override say_hello() to also say "and my ID is [employee_id]"

# Use super() in the overridden method to call the original one first.

class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, I'm {self.name}")    
        

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    
    def say_hello(self,):
        super().say_hello()
        print(f"and my ID is {self.employee_id}") 
        
# e = Employee("huzair",20,2)
# e.say_hello()



# Exercise 3

# Add a new class Manager that inherits from Employee and adds a team_size

# Use super() in Manager to initialize everything properly

class Manager(Employee):
    def __init__(self,name,age,employee_id,team_size):
        super().__init__(name,age,employee_id)
        self.team_size = team_size
    def say_hello(self):
        super().say_hello()
        print(f"and i manage a team of {self.team_size} people")
        
# m = Manager("huzair",18,1,99)
# print(m.name)
# print(m.age)
# print(m.employee_id)
# print(m.team_size)
# m.say_hello()



# Excercise 4

# The Diamond Inheritance Problem
# Here’s the setup:
    
# Run d = D() and observe the output.

# Explain why the order is like that (hint: MRO – Method Resolution Order).

# Try changing the inheritance order of class D to class D(C, B) and see how the output changes.

# Bonus: Use super() in every class (as done) and explain why we use super() instead of directly calling A.__init__(), etc.

class A:
    def __init__(self):
        print("A init called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init called")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init called")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init called")

