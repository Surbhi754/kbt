import streamlit as st
st.title("welcome to app2")
age=st.slider("select your age",1,100)
city=st.selectbox("select your city",["New York","Los Angeles","Chicago"])

if st.button("show details"):
    st.write(f"Your age is {age} ")
    st.write(f"You live in {city}")