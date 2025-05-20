class Dog:
    def speak(self):
        return "woof"
    
class Cat:
    def speak(self):
        return "meow"
    
def animal_factory(animal_type):
    if animal_type == "cat":
        return Cat()
    if animal_type == "dog":
        return Dog()
    
print(animal_factory("dog").speak())