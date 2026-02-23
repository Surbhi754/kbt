import streamlit as st
st.title("simple chat bot")
user_input = st.text_input("ask me anything")
if st.button("send"):
    st.write(f"You asked: {user_input}")
    st.write("Sorry, I am just a simple bot and cannot answer your question.")