def main(name:str) -> str:
    cool_case = ''
    name_length = len(name)
    for i in range(0,name_length,2):
        cool_case += name[i].upper()
    for i in range(1,name_length,2):
        cool_case += name[i].lower()
    return cool_case

print(main("Huzair"))