# Q- print a table that takes input from user and prints it table from 0 to 10

def main (value:int)->str:
    for i in range(11):
        print(f"{value} x {i} = {value * i}")
    return 's'
main(5)