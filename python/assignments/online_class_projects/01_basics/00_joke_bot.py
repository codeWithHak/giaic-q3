JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
SORRY = "Sorry I only tell jokes"
user_input = input("Provide an input: ")


def joke_bot ():
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)    
joke_bot()        