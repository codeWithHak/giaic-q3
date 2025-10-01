from typing import Callable
from dataclasses import dataclass

@dataclass
class Calculator:
    operation: Callable[[int,int], str]
    
    def __call__(self, a:int, b:int) -> str:
        return self.operation(a,b)
    
def sum(a:int, b:int) -> str:
    return str(a+b)
    
calc = Calculator(operation=sum)
print(calc(10,20))
