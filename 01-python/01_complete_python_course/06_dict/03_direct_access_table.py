# dat = [None] * 10
# print(dat)
# dat[3] =  "huzair"
# for i in dat:
#     print(i)
    
keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
dat = [None] * 10

for i in range(len(keys)):
    dat[keys[i]] = values[i]
    print("dat2[keys[i]]:",dat[keys[i]])
