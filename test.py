import streamlit as st

st.write("Hello, Please enter a number and I will tell its square..")
num = st.text_input("Hello, Please enter a number and I will tell its square..")
num = int(num)
out = num*num
st.write("The square value is ",out)
