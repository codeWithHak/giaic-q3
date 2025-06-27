# we cannot instantiate abstract class

from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    def __init__(self,tyres):
        self.tyres = tyres
    @abstractmethod    
    def start(self):
        pass
