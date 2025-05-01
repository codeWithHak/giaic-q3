# 4. Class Variables and Class Methods

# Assignment:

# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.

class Bank:
    
    bank_name = "Meezan Bank Limited"
    
    @classmethod        
    def change_bank_name(cls,bank_name):
        cls.bank_name = bank_name
        
mcb = Bank()
mcb.change_bank_name("Bank Al Habib - jo naam he aitemad ka")
print(mcb.bank_name)
        
ncb = Bank()
print(ncb.bank_name)