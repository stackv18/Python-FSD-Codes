import streamlit as st

st.set_page_config(page_title="Forth NUmber",page_icon="🐇",layout="centered")
st.title("Number Input DEmo")
age = st.number_input("Enter your age",min_value=10,max_value=80,value=18)
ratings = st.slider("GIve rating",min_value=0,max_value=10,value=7,step=2)
st.write(age)
