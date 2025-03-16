import json
my_tup = (1,4,3,)
# print(my_tup[0])
# print(my_tup[-1])
# print(my_tup.count(2))
# print(my_tup.index(2))

#phonebook excercise

phonebook = {
    'david':"01234",
    'john':'05678',
    'jon':'090701'
}


# a continuos loop till user types 'close'

try:
    with open ('phonebook.json','r') as file:
        phonebook = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    phonebook={}
while True:
    user_input = input('Search for a contact (search), or add a number (add), type (close) to close the notebook: ')
    
    # add new user to contacts
    if user_input == 'add':
        new_name = input("What's the name of the person: ")
        new_contact = input("What's his contact number: ")
        phonebook[new_name] = new_contact
        print(phonebook)
    
    # search from existing users
    elif user_input == 'search':
        existing_name = input("Search for an existing contact: ")
        if existing_name in phonebook:
            print(f"{user_input}'s number is {phonebook[user_input]}")

        else:
            print("number not found")

    # close the program
    elif user_input == 'close':
        print("Closing the program...")
        with open('json.phonebook','w') as file:
            json.dump(phonebook, file)
        print("Closed!")
        break

    # if input is invalid this will run
    else:
        print("Invalid input please give input between 'search' or 'add'")

    print(phonebook)