from dataclasses import dataclass

@dataclass
class Person:
    """
    Represents a person
    
    Attributes:
        name(str): Person's name
        age(int): Person's age
        voice(str): Person's voice
    """
    name:str
    age:int
    voice:str
    
    @dataclass
    class UnderPerson:
        under_name:str
        under_age:int
        under_voice:str

        
        def speak(self):
            print(f"{self.under_name} is saying {self.under_voice} from under")
    
    def speak(self):
        print(f"{self.name} is saying {self.voice}")
        

p1 = Person("Huzair",19,"hello")
p2 = Person.UnderPerson("Huzaifa",20,"bachaaaoooo")
print(p1)
p1.speak()
print(p2)
p2.speak()