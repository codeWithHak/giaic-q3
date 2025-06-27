# initialize two lists
first_names = ["Huzair","Huzaifa"]
last_names = ["Khan","Farooqui"]

# Operator +
# concatenate both lists
full_namess = first_names + last_names

# see result
print(full_namess) # ['Huzair', 'Huzaifa', 'Kha', 'Farooqui']


# Operator *
multi_first_names = first_names * 3
print(multi_first_names) # ['Huzair', 'Huzaifa', 'Huzair', 'Huzaifa', 'Huzair', 'Huzaifa']


# Operator del 
del first_names[0] # deletes first element from list
print(first_names[0]) # shift Huzaifa to index 0 because Huzair is deleted 
# del first_names # delets whole list
# print(first_names) # NameError


# built-in function all()
print(all([])) # True
print(all([1,2,3,4,5])) # True
print(all([""]))
print(all([0]))

if []:
    print("Empty list is True")
else:
    print("Empty list is False")  # ➝ This will run

print(any([]))
print(any([""]))
print(any([0]))
print(any([1]))
print(any([False]))
print(any([True,False,True]))


# append on lists
list1 = [1,2,3]
list2 = [4,5,6]
# list1.append(list2) # appends list 2 as an array
print(list1)

# min
print(min(list1))

# max
print(max(list1))

# clear
list1.clear()
print(list1)
# print("max:",max(list1)) #ValueError
# print("min:",min(list1)) #ValueError

# count()
