
import streamlit as st

st.set_page_config(page_title="Streamlitpage3",page_icon="🍰",layout="centered")
st.title("Selection Widgets Demo")
course=st.selectbox("select course",['Python','FSD','DE','PS'])
days=st.multiselect("Select prefered days",['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday'])
mode=st.radio("Select delivery mode",['online','offline'])
sub=st.checkbox("You want to subscribe?")

st.markdown("---------")
st.write(f"**Course** {course}")
st.write(f"**days** {','.join(days) if days else "none"}")
st.write(f"**mode** {mode}")
st.write(f"subscribed {'Yes' if sub else 'No'}")
