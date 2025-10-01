# Task: Modify the class to hide marks and provide proper getter/setter methods with validation
# (e.g. marks must be between 0–100).

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
    
    



