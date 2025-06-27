from dataclasses import dataclass, field
from typing import ClassVar, Final

@dataclass
class Person:
    """
    Represents a person
    
    Attributes:
        name(str): Person's name
        age(int): Person's age
        voice(str): Person's voice
        species(ClassVar[str]): Person's voice
    """
    # instance attributes
    name:str
    age:int
    voice:str
    
    #class attributes
    species:ClassVar[str] = "Homo sapien"
    
    # class attribute final
    PlanetType: Final = "Earth"
    planet:ClassVar[str] = PlanetType
    
    countries_visited:list[str] = field(default_factory=list)
    
    def speak(self) -> str:
        return f"{self.name} is saying {self.voice}"
    
    
    def get_species(self) -> str:
        return f"{self.name} is {self.species}"
        
    def get_planet(self):
        return f"{self.name} lives on {self.planet}"

p1:Person = Person("Huzair",19,"hello")

print(p1)
print(p1.speak())
print(p1.get_species())
print(p1.get_planet())
print(Person.species)


