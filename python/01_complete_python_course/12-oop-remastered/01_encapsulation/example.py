class BankAccount:
    
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"{amount} deposited")
    
    def get_balance(self):
        print(f"Balance is {self.__balance}")
        
b = BankAccount("huzair",7000)
b.get_balance()
b.deposit(1)
b.get_balance()
print(b._BankAccount__balance)