#3. Write a Python program to calculate the area of a circle (use π = 3.14).



#4. Write a Python program to swap two variables without using a third variable.
# the way I solved the problem, very inefficient :)

# a = 10
# b = 100

# jab tak a ki value b ke barabar na hojaey matlab hundred tab tak a me 1 increment karte raho
# while a < b:
#     a+=1
#     print("A =",a)

# jab tak b ki value 10 na hojaey aik decrement karte raho
# while b != 10:
#     b-=1
#     print("B =",b)

# print both values
# print(a) #output - 100
# print(b) #output - 10


# correct way, using tuple unpacking
def main():
    x = int(input("Give the value of x: "))
    y = int(input("Give the value of y: "))
    x,y = y,x
    return f"X:{x} Y:{y}"

print(main())
