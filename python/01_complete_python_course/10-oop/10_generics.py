from typing import TypeVar,Generic
from dataclasses import dataclass

T = TypeVar("T")
nums = [1,2,3]
name = "Huzair"
letters = list(name)

# Remove Spaces
# letters = [ch for ch in name if ch != " "]

def get_first_element(nums:list[T]) -> T:
    return nums[0]

print(get_first_element(nums))
print(get_first_element(letters))

def greet(name:T)->T:
    return name

print(greet("Huzair"))


N = TypeVar("N")

# @dataclass
# class Person(Generic[N]):
#     name:str
    
#     def get_name(self) -> str:
#         return self.name
    
#     def set_name(self,name:N) -> None:
#         self.name = name
#         print(f"Name has been set to {self.name}")
        
    
# p1:Person = Person("Huzair")
# print(p1)
# print(p1.get_name())
