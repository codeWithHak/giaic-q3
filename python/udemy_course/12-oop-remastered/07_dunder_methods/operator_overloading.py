# how operatos are called behind the scened
# print(int.__add__(10,5))
# print(int.__sub__(10,5))
# print(int.__abs__(10))

class Student:
    def __init__(self,eng,urdu):
        self.eng = eng
        self.urdu = urdu
        
    def __add__(self,other):
        return Student(self.eng + other.eng, self.urdu + other.urdu)
    
    def __str__(self):
        return f"English: {self.eng}, Urdu: {self.urdu}"
        
    def __gt__(self,other):
        s1 = self.eng + self.urdu    
        s2 = other.eng + other.urdu 
        return s1 > s2   
        
s1 = Student(11,71)
s2 = Student(82,65)
s3 = Student(62,65)
s4 = Student(62,65)
s5 =  s1 + s2 + s3 + s4
print(s5)



if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
    
    
# how operatos are called behind the scened
# print(int.__add__(10,5))
# print(int.__sub__(10,5))
# print(int.__abs__(10))

# class Student:
#     def __init__(self,*args, **k):
#         self.eng = eng
#         self.urdu = urdu
        
#     def __add__(self,other):
#         return Student(self.eng + self.urdu,other.eng + other.urdu)
    
#     def __str__(self):
#         return f"Student1: {self.eng}, Student2: {self.urdu}"
        
#     def __gt__(self,other):
#         s1 = self.eng + self.urdu    
#         s2 = other.eng + other.urdu 
#         return s1 > s2   
        
# s1 = Student(11,71)
# s2 = Student(82,65)

# s3 = s1 + s2
# print(s3)
# print(91+71)

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")
    