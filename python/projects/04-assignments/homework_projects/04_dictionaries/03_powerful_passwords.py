"""
Problem Statement

You want to be safe online and use different passwords for different websites.
However, you are forgetful at times and want to make a program that can match which password belongs to which website without
storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier.
This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password
hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works,
just know that hash_password(...) returns the hash for the password!)"""

import hashlib

# --------------------------- this is a one time implementation I,ll update it with while loop later ----------------------------------- 


# take input from user when it first came to your website
user_email = input("Set an email: ")
user_password = input("Set a password: ")

# create a hash for email
email_h = hashlib.sha256()
print("email_h: ",email_h)
# create a hash for password
password_h = hashlib.sha256()
print("password_h: ",password_h)


# update the hash you just created with the value that user gave
email_h.update(user_email.encode())

# update the hash you just created with the value that user gave
password_h.update(user_password.encode())

# convert the hash for password and email hash in hexadecimal format (you can use digest() to convert it in binary).
hashed_password = password_h.hexdigest()
hashed_email = email_h.hexdigest()


print("EMail:" + user_email)
print("Hashed Email: " + hashed_email)
print("Password:" + user_password)
print("Hashed password: " + hashed_password)

logged_in_users:dict = {}
logged_in_users[hashed_email] = hashed_password
print("Logged In!")
print("USers: ", logged_in_users)

print("Now you can check users")

ask_email = input("Type your email to see if you have already logged in: ")

ask_email_h = hashlib.sha256()
ask_email_h.update(ask_email.encode())
hashed_ask_email = ask_email_h.hexdigest()
print("Original mail hash: ", hashed_email)
print("Re-check mail hash: ", hashed_ask_email)

if hashed_ask_email in logged_in_users:
    print("Email exists!")
    ask_password = input("Type password: ")
    ask_password_h = hashlib.sha256()
    ask_password_h.update(ask_password.encode())
    hashed_ask_password = ask_password_h.hexdigest()

    print("Original password hash: ", hashed_password)
    print("Re-check password hash: ", hashed_ask_password)
    
    
    if hashed_ask_password in logged_in_users.values():
        print("Correct password")
    else:
        print("wrong pass")
        
else:
    print("Email dosent exist") 