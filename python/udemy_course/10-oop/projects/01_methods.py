class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        print(f"{sum(self.marks) / 3:.2f}")
        
huzair = Student('Huzair',[90,80,90])
print(huzair)

huzair.average()