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
st.title("Student Form")
name = st.text_input("Enter your name")
last_name = st.text_input("Enter your last name")
age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Pune", "Mumbai", "Nashik"])  
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
email = st.text_input("Enter your email")
if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Last Name: {last_name}")
    st.write(f"Age: {age}")
    st.write(f"City: {city}")
    st.write(f"Gender: {gender}")
    st.write(f"Email: {email}")
