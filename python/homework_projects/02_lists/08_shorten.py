"""
Problem Statement
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list,
and prints each item it removes until lst is MAX_LENGTH items long.
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
We've written a main() function for you which gets a list and passes it into your function once you run the program.
For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
"""

def main(lst):
    lst_len = len(lst)
    print(lst_len)
    MAX_LENGTH = 3
    while True:
        if lst_len > MAX_LENGTH:
            print("Before pop: ", "lst: ", lst, "lst_len: ", lst_len)
            lst.pop()
            lst_len -= 1
            print("After pop: ", "lst: ", lst, "lst_len: ", lst_len)
        else:
            print(lst)
            break
main([1,2,3,4,6,6,7])