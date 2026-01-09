
import streamlit as st

st.set_page_config(page_title="Streamlitpage3",page_icon="🍰",layout="centered")
st.title("Text Input Demo")
name=st.text_input("Enter your Name")
comments=st.text_area("Feedback:")

st.write("Live Output:")

if name:
    st.write(f"Hello {name}")
if comments:
    st.write("Your Feedback:")
    st.write(comments)
