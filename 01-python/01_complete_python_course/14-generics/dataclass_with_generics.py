from dataclasses import dataclass, field
from typing import TypeVar, Generic, ClassVar

T = TypeVar("T")

@dataclass
class Stock(Generic[T]):
    
    items:list[T] = field(default_factory=list)
    limit:ClassVar[int] = 10
    
    def push_item(self, item:T) -> None:
        self.items.append(item)
        
    def pop_item(self) -> T:
        return self.items.pop()
    
    
stock_of_ints = Stock[int]()
stock_of_ints.push_item(10)
stock_of_ints.push_item(20)
stock_of_ints.pop_item()
stock_of_ints.push_item(30)
print(stock_of_ints)
    
        
# stock_of_ints = Stock[str]()