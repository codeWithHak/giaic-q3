# in operator (membership in operator)

person_age = {
    "huzair":19,
    "khizar":22,
    "huzaifa":18
}

for name in person_age:
    print(f"{name} is {person_age[name]} years old" )
    

# sorted

sorted_dict = sorted(person_age)
print(sorted_dict)
    
    
# .fromkeys()

d = {}
vowels = d.fromkeys(['a','e','i','o','u'],'vowel')
print(vowels) # output: {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel'}


print(vowels.get('a')) # value of a will be printed
print(vowels.get('b', 'default value'))  # b is not a key so default value will be printed 