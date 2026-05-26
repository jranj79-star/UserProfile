import streamlit as st

st.set_page_config(page_title="User Profile", layout="centered")

st.title("User Profile")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")
age = st.number_input("Enter Age", min_value=1, max_value=100)

if st.button("Submit"):
    st.success("Profile Created Successfully")

    st.write("### Profile Details")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Age: {age}")# trigger 1779799237
