import streamlit as st

st.set_page_config(page_title="Third NUmber",page_icon="🐇",layout="centered")
st.title("Text Input DEmo")
name=st.text_input("Enter your name:")
comment=st.text_area("Feed ur back:")

st.write("Live output:")
if name:
    st.write(f"Hello {name}")
    
if comment:
    st.write(f"Te evu lahyu che ke {comment}")
