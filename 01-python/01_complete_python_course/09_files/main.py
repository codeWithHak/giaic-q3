import shutil
import os

# -- write --

# # open file
# f = open('countries.txt', 'wt')

# # modify file
# f.write("lumber 1 country\n")
# f.write("lumber 2 country\n")
# f.write("lumber 3 country\n")
# f.write("lumber 4 country\n")

# # close file


# # -- read open() -- 

# f = open('countries.txt')
# content = f.read()
# print(content)

# read --with--

# with open("countries.txt") as f:
#     content = f.read()
#     print(content)
# print(content)

# if True:
#     x = 20
    
# print(x)

# read [length]

# with open('countries.txt') as f:
    
    # iterate over countries.txt
    # while True:
        
    #     # read three characters
    #     s = f.read(3)
        
    #     # if empty break
    #     if s == '':
    #         break
        
    #     # else print those 3 cahracters
    #     else:
    #         print(f"<{s}>") 
    

# with open("countries.txt") as f:
#     lines = f.readlines(17)
#     for line in lines:
#         print(line, end="")
    
# with open('countries.txt') as f:
#     for line in f:
#         print(line,end='')

# tell and seek

# with open("countries.txt") as f:
    
#     p = f.tell()
#     print(p)    

#     line = f.readline()
#     print(line, end='')    

#     f.seek(p)
    
#     line = f.readline()
#     print(line, end='')
    
    

os.rename('haha.txt','countries.txt')
shutil.copy('countries.txt', 'countries2.txt') 
cwd = os.getcwd()
os.remove('countries2.txt')