def main():
    phonebook = {}
    while True:
        user_name = input("Name: ")
        if user_name == "":
            break
        else:
            user_number = int(input("Number: "))

            phonebook[user_name] = user_number
        
        
        
        for num in phonebook:
            print(f"Name: {num} Number: {phonebook[num]}")
        
    while True:
        user_name = input("Search Name: ")
        if user_name == "":
            break
        
        if user_name not in phonebook:
            print("This name dosent exist")
        else:
            print(phonebook[user_name])
    
main()