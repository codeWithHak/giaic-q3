# The Diamond Inheritance Problem
# Here’s the setup:
    
# Run d = D() and observe the output.

# Explain why the order is like that (hint: MRO – Method Resolution Order).

# Try changing the inheritance order of class D to class D(C, B) and see how the output changes.

# Bonus: Use super() in every class (as done) and explain why we use super() instead of directly calling A.__init__(), etc.

class A:
    def __init__(self):
        print("A init called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init called")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init called")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init called")

# obj = D()
# print(D.mro())