# def IsPalindrome(word):
#     if word == '':
#         print('empty string')
#         return False
    
#     word_lower = word.lower()
#     word_lower_len = len(word_lower)
    
#     if word_lower_len <= 1:
#         return True
    
#     reversed = ''
    
#     if word_lower[0] == word_lower[-1]:
#         print(type(word))
#         list(word)
#         print(type(word))
#         word.pop(0)
#         IsPalindrome(word)
#         print('word', word)
#     else:
#         print('false case')
#         return False
        
# print(IsPalindrome("refer"))


def IsPalindrome(text, left=0, right=0):
    
    # default value for rght 
    if right == 0:
        right = len(text) - 1
    
    # number of characters in substring
    n = right - left + 1

    # Base case
    if n<=1:
        return True
    
    # check if first and last char are equal
    
    if text[left] != text[right]:
        return False
    
    # Make recursive call
    return IsPalindrome(text, left+1, right-1)
    
         
print(IsPalindrome('refer',1,3))