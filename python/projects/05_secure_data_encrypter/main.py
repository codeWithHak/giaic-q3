import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# ----- 🔐 Initialization -----
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"
if 'fernet_key' not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.fernet_key)

cipher = st.session_state.cipher

# ----- 🔑 Utility Functions -----
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    if encrypted_text in st.session_state.stored_data:
        if st.session_state.stored_data[encrypted_text]["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    st.session_state.failed_attempts += 1
    return None

# ----- 🎨 UI Layout -----
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu, index=menu.index(st.session_state.current_page))

if st.session_state.failed_attempts >= 3 and choice != "Login":
    st.session_state.current_page = "Login"
    choice = "Login"

# ----- 🏠 Home -----
if choice == "Home":
    st.session_state.current_page = "Home"
    st.subheader("🏠 Welcome to the Secure Data System")
    st.markdown("Encrypt your sensitive data securely. Navigate using the sidebar.")
    st.info("Use a unique passkey to store and retrieve your secrets.")

# ----- 💾 Store Data -----
elif choice == "Store Data":
    st.session_state.current_page = "Store Data"
    st.subheader("📂 Store Data Securely")

    with st.form("store_form"):
        user_data = st.text_area("Enter Data:", height=100)
        passkey = st.text_input("Enter Passkey:", type="password")
        submit = st.form_submit_button("Encrypt & Save")

        if submit:
            if user_data and passkey:
                encrypted_text = encrypt_data(user_data)
                st.session_state.stored_data[encrypted_text] = {
                    "passkey": hash_passkey(passkey)
                }
                st.success("✅ Data encrypted and stored!")
                st.code(encrypted_text, language='text')
            else:
                st.error("⚠️ Please enter both data and passkey.")

# ----- 🔓 Retrieve Data -----
elif choice == "Retrieve Data":
    st.session_state.current_page = "Retrieve Data"
    st.subheader("🔍 Retrieve Encrypted Data")

    with st.form("retrieve_form"):
        encrypted_text = st.text_area("Paste Encrypted Data:", height=100)
        passkey = st.text_input("Enter Passkey:", type="password")
        submit = st.form_submit_button("Decrypt")

        if submit:
            if encrypted_text and passkey:
                result = decrypt_data(encrypted_text, passkey)
                if result:
                    st.success("✅ Decrypted Successfully!")
                    st.text_area("Decrypted Data:", result, height=100)
                else:
                    st.error(f"❌ Incorrect passkey. {3 - st.session_state.failed_attempts} attempt(s) remaining.")
                    if st.session_state.failed_attempts >= 3:
                        st.warning("🔒 Locked out due to too many failed attempts.")
                        st.session_state.current_page = "Login"
                        st.rerun()
            else:
                st.error("⚠️ Both fields are required!")

# ----- 🔑 Admin Login -----
elif choice == "Login":
    st.subheader("🔑 Admin Login Required")

    with st.form("login_form"):
        master_key = st.text_input("Enter Master Password:", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if master_key == "admin123":
                st.session_state.failed_attempts = 0
                st.session_state.current_page = "Retrieve Data"
                st.success("✅ Access restored.")
                st.rerun()
            else:
                st.error("❌ Incorrect master password.")
