# initialize a list
list1 = [1,2,3,4,5]

# same reference 
"""list2 = list1
list2.append(0) # 0 will be added in list 1 as well
print(list1)"""

# new copy new reference
"""list2 = list1.copy()
list2.append(0) # 0 will not be added in list 1
print(list1)"""


# another way to take copy with new reference
# list2 = list1[:]
# list2.append(0) # 0 will not be added in list 1 
# print(list1)

