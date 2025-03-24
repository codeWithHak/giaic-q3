# Q- print a table that takes input from user and prints it table from 0 to 10

def main (value:int)->str:
    for i in range(11):
        priresunt(f"{value} x {i} = {value * i}")

main(5)