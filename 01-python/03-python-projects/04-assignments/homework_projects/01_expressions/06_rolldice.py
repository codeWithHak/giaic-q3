from random import randint
# Question:

"Simulate rolling two dice, and prints results of each roll as well as the total."


def dice1():
    dice1 = randint(1,6)
    return dice1

def dice2():
    dice2 = randint(1,6)
    return dice2

def main():
    diceroll1 = dice1()
    diceroll2 = dice2()
    print(f"Dice 1: {diceroll1}")
    print(f"Dice 2: {diceroll2}")
    print(f"Total: {diceroll1 + diceroll2}")
    
main()