# ------------- Testing version (success) ----------------
# def Palindrome(word):
#     # convet in lowercase
#     lower = word.lower()
    
#     # check for first and last char
#     if lower[0] == lower[-1]:
#         print("same first and last lowers")
#         print(lower)
        
#         reversed = ''
#         for word in lower:
#             print(f"reversed: {reversed}, word:{word}")
#             reversed = word + reversed
#             if reversed == lower:
#                 print("Palindrome")
#     print(word)
    
# Palindrome("refer")


# ------------------ Poduction Version --------------------

def Palindrome(word):
    # convert whole word to lowercase
    word_lower = word.lower()
    
    # placeholder for reversed string
    reversed = ''
    
    # loop that concatinate values in revrsed
    for char in word:
        reversed = reversed + char
        
    # compare reversed string with original string    
    if reversed == word_lower:
            print("Palindrome")
    else:
        print("Not a Palindrome")    
    
# execute function
Palindrome('refer')