import streamlit as st

st.write("Hello, Please enter a number and I will tell its square..")
num = st.text_input("Hello, Please enter a number and I will tell its square..")
st.write("The square value is ",num*num)
