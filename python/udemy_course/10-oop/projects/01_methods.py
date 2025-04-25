class Student:
    def __init__(self,name,english,urdu,islamiat):
        self.name = name
        self.english = english
        self.urdu = urdu
        self.islamiat = islamiat
        
    def average(self):
        print((self.english + self.urdu + self.islamiat) / 3)
        
huzair = Student('Huzair',90,80,90)
print(huzair)

huzair.average()