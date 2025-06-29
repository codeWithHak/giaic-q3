# # user se pehle key lo
# # phir uski value lo
# # key ke sath value ko map karke aik dict me daldo
# # jab tak user empty key n ade repeat the process\
# # agar key duplicate ho yani aik key user 2 bar dede to warn karo or value ipdate kardo
# # dict print karado


# def main():
    
#     # Initialize Dictionary
#     user_dict = {}
        
#     while True:
#         # read key
#         key = input("Key: ")
        
#         # Check if not empty
#         if key != "":
                        
#             # Check if duplicate
#             if key in user_dict:
#                 print("Warning: Duplicate key value will be replaced")
#                 value = input("Value: ")
#                 user_dict[key] = value

#             # add ke withour warning
#             else:
#                 value = input("Value: ")
#                 user_dict[key] = value
#             # read value
            

#         # break if key is ""
#         else:
#            break 

#     # print dictionary
#     print(user_dict)

# main()


# ----- instructor way ---------

d = {}

while True:
    
    # read key
    key = input("Enter key: ") 
    
    # Check if empty
    if key == "":
        break
    
    # Check if it's a duplicate
    if key in d:
        print("Warning: Duplicate key, value will be overwritten")
    
    # Read value
    value = input("Enter value: ")
    
    # Insert key-value pair
    d[key] = value
    
    