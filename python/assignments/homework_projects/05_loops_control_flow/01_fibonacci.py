"""
Problem Statement

Write a program to print terms in the Fibonacci sequence up to a maximum value.

In the 13th century, the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population of rabbits,
devised a mathematical sequence that now bears his name. The first two terms in this sequence, Fib(0) and Fib(1), are 0 and 1,
and every subsequent term is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:

Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than
10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
"""

fib1 = 0 # 1 #1
fib2 = 1 # 1 #2
fib3 = 0 # 1 #2 #3
while fib3 < 10000:
    print(fib1)
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    
