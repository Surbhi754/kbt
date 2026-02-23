import streamlit as st
st.title("Hello World")
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.write(f"Hello, {name}!")