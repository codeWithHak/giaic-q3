from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:int
    in_stock:bool
    
soap = Product(id=113, name="Dove",price=180, in_stock=True , )    
print(soap)