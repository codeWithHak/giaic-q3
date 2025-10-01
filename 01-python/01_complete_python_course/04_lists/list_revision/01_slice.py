my_list = [1,2,3,4,5]

# positive indexing
print("id(my_list):",id(my_list))
print("my_list[0]:",my_list[0])
print("my_list[:]:",my_list[:])
print("my_list[1:]:",my_list[1:])
print("my_list[:1]:",my_list[:1])
print("my_list[0:2]:",my_list[0:2])
print("id(my_list):",id(my_list))

# negative indexing
print("my_list[-1]:",my_list[-1]) # last elemen only in str
print("type(my_list[-1]):",type(my_list[-1])) # last elemen only in int
print("my_list[-1:]:",my_list[-1:]) # last element only but in list not in str
print("type(my_list[-1]):",type(my_list[-1:])) # last elemen only in str
print("my_list[:-1]:",my_list[:-1]) # all elements as list except last
print("my_list[-3:-1]:",my_list[-3:-1]) 

# update list
print(my_list)
my_list[:] = [9,8,7,6]
print(my_list)



