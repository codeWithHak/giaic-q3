# # welcome message
print(f"\n{'-'*20} Welcome To Anagram Checker {'-'*20}\n")

# inputs forom user
word1 = input("First word: ").lower().replace(" ", "")
print(word1)
word2 = input("Second word: ").lower().replace(" ", "")

sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

if sorted_word1 == sorted_word2:
    print("\nThey are anagrams")

else:
    print("\nThey are not anagrams") 
