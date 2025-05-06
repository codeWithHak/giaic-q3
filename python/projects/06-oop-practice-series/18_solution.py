# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self):
        self.__price = 0
    
    @property        
    def price(self):
        print(self.__price)
        
    @price.setter
    def price(self,price):
        print(f"Updated price from {self.__price} to {price}")
        self.__price = price
        
    @price.deleter
    def price(self):
        print("Deleted price")
        del self.__price
        
p = Product()
p.price = 10
p.price
del p.price

