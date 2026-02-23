import streamlit as st

st.markdown("""
<style>
            .stButton>button {
                background-color: red;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }        
            
</style>         
            
            
            
            """,unsafe_allow_html=True)
st.title("welcome to app2")
age=st.slider("select your age",1,100)
city=st.selectbox("select your city",["New York","Los Angeles","Chicago"])

if st.button("show details"):
    st.write(f"Your age is {age} ")
    st.write(f"You live in {city}")