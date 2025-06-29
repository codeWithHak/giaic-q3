class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def credit(self, amount):
        self.balance += amount 
        
    def debit(self, amount):
        self.balance -= amount
        
    def print_balance(self):
        print(self.balance)

acc1 = BankAccount("huzair",1000)

print(acc1.name)
acc1.print_balance()
acc1.credit(200)
acc1.print_balance()
