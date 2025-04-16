def IsPalindrome(word):
    if word == '':
        print('empty string')
    
    word_lower = word.lower()
    
    reversed = ''
    
    if word_lower[0] == word_lower[1]:
        IsPalindrome()