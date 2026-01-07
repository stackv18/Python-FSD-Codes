
import streamlit as st

st.set_page_config(page_title="Streamlitpage3",page_icon="🍰",layout="centered")
st.title("Number Input Demo")
age=st.number_input("Enter your Age:",min_value=0,max_value=80,value=25)
rating=st.slider("Give Rating:",min_value=0,max_value=10,value=7,step=2)
st.write(age)
