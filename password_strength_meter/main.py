import streamlit as st
import re
import random
import string

# Custom CSS for clean and modern UI
st.markdown("""
<style>
    .stTitle {
        color: #4A90E2;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 2px solid #4A90E2;
        width: 100%;
    }
    .feedback {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .suggested-password {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .copy-button {
        background-color: #4A90E2;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-size: 16px;
        cursor: pointer;
        margin-top: 20px;  /* Added padding-top */
        width: 100%;
    }
    .tips {
        margin-top: 20px;
        font-size: 16px;
        color: #555;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# List of commonly used weak passwords
WEAK_PASSWORDS = [
    "12345678", "password", "password123", "123456789", "qwerty", 
    "abc123", "admin", "letmein", "welcome", "monkey", "sunshine", 
    "iloveyou", "123123", "1234", "12345", "123456", "1234567"
]

# Function to generate a strong password with at least one special character
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&"
    while True:
        password = ''.join(random.choice(characters) for _ in range(12))
        # Ensure the password contains at least one special character
        if re.search("[!@#$%^&]", password):
            return password

# Initialize session state for copy confirmation
if "copied" not in st.session_state:
    st.session_state.copied = False

# App title
st.title("Password Strength Meter")

# Password input
password = st.text_input("Enter your password", type="password", placeholder="Type your password here")

# Initialize score and feedback
score = 0
feedback = []
emoji = ''

# Check if password is in the blacklist
if password and password.lower() in [p.lower() for p in WEAK_PASSWORDS]:
    feedback.append("❌ This password is too common and easily guessable.")
    emoji = "⚠️"
else:
    # Password strength checks
    if password:
        if len(password) >= 8:
            # Check for lowercase letters
            if not re.search(r"[a-z]", password):
                feedback.append("❌ Include lowercase letters.")
            else:
                score += 1

            # Check for uppercase letters
            if not re.search(r"[A-Z]", password):
                feedback.append("❌ Include uppercase letters.")
            else:
                score += 1

            # Check for digits
            if not re.search(r"\d", password):
                feedback.append("❌ Include numbers.")
            else:
                score += 1

            # Check for special characters
            if not re.search("[!@#$%^&]", password):
                feedback.append("❌ Include special characters (e.g., !@#$%^&).")
            else:
                score += 1

            # Determine password strength
            if score == 4:
                feedback = ["✅ Strong Password"]
                emoji = "🔒"
            elif score >= 2:
                feedback.append("⚠️ Moderate Password")
                emoji = "🔐"
            else:
                feedback.append("❌ Weak Password")
                emoji = "⚠️"
        else:
            feedback = ["❌ Password must be at least 8 characters long."]
            emoji = "⚠️"

# Display feedback
if password:
    st.markdown(f"<div class='feedback'>{emoji} {' '.join(feedback)}</div>", unsafe_allow_html=True)

    # Progress bar based on password strength
    if score == 4:
        st.progress(100)
    elif score == 3:
        st.progress(75)
    elif score == 2:
        st.progress(50)
    elif score == 1:
        st.progress(25)
    else:
        st.progress(0)

    # Password suggestion feature (only shown if password is weak, moderate, or blacklisted)
    if score < 4 or password.lower() in [p.lower() for p in WEAK_PASSWORDS]:
        st.markdown("### Need a stronger password? Try this:")
        suggested_password = generate_password()
        
        # Display the suggested password in a text box for easy copying
        st.code(suggested_password, language="text")
        
        # Copy confirmation button
        if st.button("Copy to Clipboard", key="copy_button"):
            st.session_state.copied = True
            st.session_state.suggested_password = suggested_password

        # Show confirmation message if copied
        if st.session_state.copied:
            st.success(f"Password '{st.session_state.suggested_password}' copied to clipboard!")
            st.markdown("**Tip:** You can also click on the password above to manually copy it.")

    # Tips for improving password strength
    if score < 4 or password.lower() in [p.lower() for p in WEAK_PASSWORDS]:
        st.markdown("<div class='tips'>💡 <strong>Tips for a stronger password:</strong></div>", unsafe_allow_html=True)
        st.markdown("- Use a mix of uppercase and lowercase letters.")
        st.markdown("- Include numbers and special characters.")
        st.markdown("- Avoid common words and phrases.")
else:
    st.markdown("<div class='feedback'>🔑 Enter a password to check its strength.</div>", unsafe_allow_html=True)