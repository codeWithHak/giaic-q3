import re
password = input("Give me a password: ")
score = 0

if len(password) >= 8:
    score +=1
else:
    print("Weak password")    
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[0-9]", password):
    score+=1
print("Your score is", score)


