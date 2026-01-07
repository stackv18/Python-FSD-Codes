
import streamlit as st

st.set_page_config(page_title="Streamlitpage",page_icon="🍕",layout="centered")
st.title("Welcome to streamlit")
st.header("This is Header")
st.subheader("This is subheader")
st.text("This is text")
st.write("This is **_st.write()**")
st.markdown("This is Markdown")
code="""
def add(a,b):
    return a+b
result=add(6,7)
print(result)
"""

st.code(code,language='python')
st.code(code,language='C')
