"""
Problem Statement
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time,
you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available
and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy,
and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5

"""

def main():
    MANGO = 20
    KIWI = 10
    BANANA = 5
    PINEAPPLE = 8
    GAVA = 9
    ORANGE = 4
    
    mango = int(input("How many mangos do you want: "))
    kiwi = int(input("How many kiwis do you want: "))
    banana = int(input("How many bananas do you want: "))
    pineapple = int(input("How many pineapples do you want: "))
    orange = int(input("How many oranges do you want: "))
    
    