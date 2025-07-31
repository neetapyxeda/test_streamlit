import streamlit as st

st.write("Hello, Please enter a number and I will tell its square..")
num = st.text_input("Hello, Please enter a number and I will tell its square..")
out = int(num)*int(num)
st.write("The square value is ",out)
