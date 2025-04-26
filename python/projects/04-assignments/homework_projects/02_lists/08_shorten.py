"""
Problem Statement
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list,
and prints each item it removes until lst is MAX_LENGTH items long.
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
We've written a main() function for you which gets a list and passes it into your function once you run the program.
For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
"""

def main(lst):
    
    # storing the length of the list in a variable so we can compare it with MAX_LENGTH
    lst_len = len(lst)    
    
    # set maximum length to three
    MAX_LENGTH = 3
    
    # run a loop until the elements in the list are not 3
    while True:
        if lst_len > MAX_LENGTH:
            
            # this will remove an element from the end of the list and the update the cuurent length of the list
            lst.pop()
            lst_len -= 1
            
        else:
            
            # when len is equal to max len this will run
            print(lst)
            break
        
main([1,2,3,4,6,6,7])