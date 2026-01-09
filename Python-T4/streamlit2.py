import streamlit as st

st.set_page_config(page_title="Hello 1",page_icon="😴",layout="centered")
st.title("Faculty Profile")
st.sidebar.header("Profile Settings")
faculty = st.sidebar.text_input("Faculty Name","Prof. VRAJ")
department = st.sidebar.selectbox("DEPARTMENT", ['CSE','CE','IT','AIML'])
exp = st.sidebar.slider("Years of Experience",0,70,10)
st.sidebar.markdown("================")
col1,col2 = st.columns([1,2])
with col1:
    st.write("Basic INformation")
    st.write(f"**Name**:{faculty}")
    st.write(f"**Department**:{department}")
    st.write(f"**Years Of Experience**:{exp}")
    
with col2:
    st.subheader("ABout")
    st.markdown("----------------")

with st.expander("Subjects Taught"):
    st.write(" -- Python")
    st.write(" -- Java")
    st.write(" -- DBMS")
