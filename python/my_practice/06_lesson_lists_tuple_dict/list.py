# initialize a list
my_list = ["huzair", "huzaifa", "khizar", "huzaifa"]

# remove first occurence of huzaifa by using remov()
"""
my_list.remove("huzaifa")
print(my_list)
"""

# remove elemnt with pop(), pop function takes index instead of number 
""" 
my_list.pop(1)
print(my_list)
"""

# list comprehension

my_num_list = [1,2,3,4,5,6]
my_new_num_list= [num**2 for num in my_num_list]
print(my_new_num_list)
print(my_num_list)