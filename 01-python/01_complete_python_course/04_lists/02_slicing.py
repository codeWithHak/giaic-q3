# create a list of name
my_list:list[str] = ["huzair","huzaifa","khizar"]
# print(id(my_list))
# slice form index 0,1 - only remove first elemnt
# print(my_list[0:1])

# remove all elements except last elemnt
# print(my_list[0:])

# my_list[1:2] = ["Abdullah"]
# print(my_list)

# concatenation

num_list_concatenate= [1,2] + [3,4]
# print(num_list_concatenate) # output - [1,2,3,4]
num_list_multiply = [1,2] * 4
# print(num_list_multiply) # output - [1,2,1,2,1,2,1,2]

# append and insert
# my_list.append('tariq')
# print("Append tariq", my_list)
# print(id(my_list))

# my_list.insert(3,"haha")
# print("Insert haha in place of Tariq",my_list) # tariq will move to right (last index in this case)
# print(id(my_list))


# my_list.remove('haha')
# print("remove haha", my_list)
# print(id(my_list))
# remove middle elemnt only
# list_len = len(my_list)
# mid_index = list_len // 2
# del my_list[mid_index]
# print(my_list)

# ----------------- Built-in Methods -----------------------

# min,max
# num_list = [10,20,33,45,31]
# print(min(num_list)) # output - 10
# print(max(num_list)) # output - 45

# # sum
# summed_list = sum(num_list)
# print("Sum:" ,summed_list) # output 139   
# print("Original", num_list) # output 139  

# count
count_list = ["apple","apple","apple"]

# list comprehension
# count_a = sum(word.count('a') for word in count_list)
# print(count_a)

# numbers = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in numbers]
# print(squares)

# fruits = ["apple", "banana", "cherry"]
# upper_fruits = [fruit.upper() for fruit in fruits]
# print(upper_fruits)

# extend 
# names:list[str] = ['Huzair',"John"]
# nums:list[int] = [1,2]
# names.extend(nums)
# print(names)


# index_list = ['tyrion', 'john', 'jamie', 'tyrion']
# print(index_list[-1])
# print(index_list.index('tyrion', 1, -1))

# remove
my_new_list = ['john', 'james', 'jamie']
my_new_list.remove('jamie')
print(my_new_list)


# sort
num_list = [10,4,7,1,2]
print(num_list)
num_list.sort()
print(num_list)
