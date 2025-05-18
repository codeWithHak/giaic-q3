import streamlit as st
import string
import random
import streamlit.components.v1 as components


# Title and subtitle only for better UI
st.title("A Strong Password is Like Wings")
st.subheader("We test wether your wings are strong enough or not!")

# input that takes passowrd
password = st.text_input(
    "Check Your Passowrd's Strength",
    type="password",
    help="Type your password te see it's strength.",
    placeholder="Your Password"
    )

# function that checks password's strength
def check_password_strength(password):
    special_characters = "!@#$%^&*"
    pass_len = len(password)
    
    # first check if password has special characters
    if any(char in special_characters for char in password):
        
        # then check if it has digits
        if any(char.isdigit() for char in password):
            
            # then check length
            if pass_len >= 8:
                st.write("✅ Strong, you are ready to fly high and safe.")
                
            elif pass_len < 8:
                st.write("⚠️  Medium, Increase length.")     
            
        else:
            st.write("❌ Weak, Include atleast one number.")
    else:
        st.write("❌ Weak, Include atleast one special character.")

# run the method that checks password
if password:
    check_password_strength(password)


# a method that generates strong password
def generate_password():
    
    # initialize an empty passwod
    generated_password = ''
    
    # take alphabets and numbers from string module
    strings = string.ascii_letters # a-z and A-Z
    numbers = string.digits # 0123456789
    
    # take hard coded special characters (string module provides useless characters as well like brackets etc)
    special_characters = "!@#$%^&*"
    
    # now we want to an index so we can take random value from the strings, numbers and special_characters.
    # for that we will first take len of each variable so we know a range to pick from.
    # because numbers(10) are less in len, strings(52) are more and special_charatcers(8) are also have different len
    
    # count len of each varaible 
    strings_len = len(strings)
    numbers_len = len(numbers)
    special_characters_len = len(special_characters)
    
    
    # run a loob 2 times that will set our password
    for i in range(2):
        
        # add a string that is on a random index but within strings length (52)
        generated_password += strings[random.randrange(strings_len)]
        
        # add a number that is on a random index but within numbers length (10)
        generated_password += numbers[random.randrange(numbers_len)]
        
        # add a special charatcer that is on a random index but within special_charatcers length (8)
        generated_password += special_characters[random.randrange(special_characters_len)]
        
        # add a string again that is on a random index but within strings length (52)
        generated_password += strings[random.randrange(strings_len)]
        
        # now we have 4 strings 2 special characters and 2 numbers, that's a pretty solid password.
    
    # show generated password    
    st.write(generated_password)
    
    # custom button component to copy password to clipboard 
    components.html(f"""
                    <button
                    onclick="navigator.clipboard.writeText('{generated_password}')"
                    style="
                        padding:0.5em 1em;
                        color:white;
                        border-radius:0.60em;
                        background-color:transparent;
                        border:1px 0px solid gray;
                        cursor:pointer;
                        "
                    >Copy</button>""")

# generate password onclick
if st.button("Generate Strong Password"):
    generate_password()
    
