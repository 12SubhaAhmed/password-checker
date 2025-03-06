import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Subha Sajjad", page_icon="🛠️", layout="centered")

# Custom CSS
st.markdown(""" 
    <style>
            .main{text-align: center;}
            .stTextInput {width : 60% !important; margin : 5%}
            .stButton button {width : 40%; background-color : #6F42C1; color: white; font-size: 18px; }
            .stButton button:hover {background-color : #4E2A7E; color: white;}
            </style>
 """, unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Checker 🔒")
st.write("Enter Your Password To Check Its Security Level")

# Function to check password strength
def checkPswrd(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # Increase score by one
    else:
        feedback.append("⚠️ Password should be at least **EIGHT** characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Password should include **both uppercase (A-Z) and lowercase (a-z)**")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Password should include **at least one number**")

    # Special character check
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Include **at least one special character** (!@#$%&*)")

    # Display password strength
    if score == 4:
        st.success("✔️ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("🟡 **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions to strengthen your password.")

    # FEEDBACK
    if feedback:
        with st.expander("💡 **Improve Your Password**"):
            for item in feedback:
                st.write(item)


password = st.text_input("Enter Your Password:", type="password", help="Ensure Your Password Is Strong!")

# Button working
if st.button("Check Strength"):
    if password:  # Make sure password is entered
        checkPswrd(password)
    else:
        st.warning("⚠️ Please **enter your password** first!")