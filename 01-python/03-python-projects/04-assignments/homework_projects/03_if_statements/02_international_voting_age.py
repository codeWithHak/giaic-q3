"""
Problem Statement
Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages.
In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

Here's a sample run of the program (user input is in blue):

How old are you? 20
You can vote in Peturksbouipo where the voting age is 16.
You cannot vote in Stanlau where the voting age is 25.
You cannot vote in Mayengua where the voting age is 48.
"""

def main():
    try:
        user_age = int(input("What's your age: "))
        voting_age_peturksbouipo = False
        voting_age_stanlau = False
        voting_age_mayengua = False

        if user_age >= 16:
            voting_age_peturksbouipo = True

        elif user_age >= 25:
            voting_age_peturksbouipo = True
            voting_age_stanlau = True

        elif user_age >= 48:
            voting_age_peturksbouipo = True
            voting_age_stanlau = True
            voting_age_mayengua = True

        if voting_age_peturksbouipo:
            print("You can vote in Peturksbouipo where the voting age is 16.")   
            print("You cannot vote in Stanlau where the voting age is 25")
            print("You cannot vote in Mayengua where the voting age is 48.")

        elif voting_age_stanlau:
            print("You can vote in Peturksbouipo where the voting age is 16.")   
            print("You can vote in Stanlau where the voting age is 25")
            print("You cannot vote in Mayengua where the voting age is 48.")

        elif voting_age_mayengua:
            print("You can vote in Peturksbouipo where the voting age is 16.")   
            print("You can vote in Stanlau where the voting age is 25")
            print("You can vote in Mayengua where the voting age is 48.") 

        else:
            print("You can't vote anywhere kiddo, Grow Up First!")
            
    except ValueError:
        print("Invalid value, please provide a number!")
    
    
main()