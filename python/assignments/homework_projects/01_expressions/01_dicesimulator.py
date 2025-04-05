# Question:
"""
Simulate rolling two dice, three times. Prints the results of each dice roll. This program is used to show how variable scope works.

"""

# Solution:
from random import randint

def main():
    for i in range(1,4):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        res = dice1 + dice2
        print(res)
main()