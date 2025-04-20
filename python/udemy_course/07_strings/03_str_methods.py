my_str = 'my name is huzair'
print(my_str.find('a'))
print(my_str.find('a',5))
print(my_str.find('a',5,7)) # -1
# print(my_str.index('a',5,7)) # error

s= "i am a good guy! yes i am"
print(s.replace("am","was"))

# split method convert str into list and takes a delimeter

# , by default
print(s.split())

# ! as delimeter
print(s.split("!"))

names = ['huzair','huzaifa','hashir']
# joins all the strings with a delimeter in between

# emty string no delimeter
print("".join(names))

# - as a delimeter
print("-".join(names))

# startswith
# checks if the str starts with the given sub-str, returns true or false
print(my_str.startswith('m')) # True
print(my_str.startswith('y')) # False


# endswith
# opposite of startswith
print(my_str.startswith('r')) # False
