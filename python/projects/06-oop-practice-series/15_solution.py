# 15. Method Resolution Order (MRO) and Diamond Inheritance

# Assignment:

# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A():
    def show(self):
        print("\nShow method from A Class")
        
class B(A):
    def show(self):
        print("\nShow method from B Class")
        
class C(A):
    def show(self):
        print("\nShow method from C Class")
        
# first D will run if show method is not in D 
# then B will run if show method is not in B 
# then his sibling C will run if show method not found in C (left,to right)
# then his parent A will run
class D(B,C):
    pass

d = D()
d.show()

# see MRO - Method Resolution Order
print(D.mro())