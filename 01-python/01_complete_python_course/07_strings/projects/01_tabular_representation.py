# title and director with = 20 characters
# other 2 has 6 char width
# all separated by atlese one space

movies = [
    ("The Shining", "Stanley Kubrick", 1980, 8.36),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.21),
    ("Gone with the Wind", "Victor Fleming", 1939, 8.14)
]


print(f"{'Title':<20} {'Director':<20} {'Year':<6} {'Score':<6}")
print("="*54)
for i in movies:
    # print(i)
    print(f"""{i[0]:<20} {i[1]:<20} {i[2]:<6} {i[3]:<6.1f}""")    
