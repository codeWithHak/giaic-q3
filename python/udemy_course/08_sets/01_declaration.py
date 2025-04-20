# se use curly braces to declare set or the set function

# set could be decalred as
my_set1 = {1,2,3,4}
print("my_set1:",my_set1)
print("type(my_set1):",type(my_set1))

# or with function
my_set2 = set([1,2,3,4])
print("my_set2:",my_set2)
print("type(my_set2):",type(my_set2))

# now see how set will ignore the duplicate value
my_set3 = {1,1,2,3,2,5,6}


# my_set3.discard(5)


# discard multiple items    
# for i in range(1,6):
#     print(i)
#     my_set3.discard(i)

# remove multiple items
for i in {1,2,3}:
    my_set3.remove(i)

print(my_set3)

my_set3.add(9)
print(my_set3)
my_set3.update([9,10,11,"helloo"])
print(my_set3)