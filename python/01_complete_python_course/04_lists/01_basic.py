# create a list with two names
my_list:list[str] = ["huzair", "huzaifa"]
print("Id:", id(my_list), "List", my_list)

# add another name in the end
my_list.append("khizar")
print("Id:", id(my_list), "List", my_list)

# delete an element from list
del my_list[1] # deleting elemnt on first index
print(my_list)

# find length of list
print(len(my_list))


#insert in the middle
