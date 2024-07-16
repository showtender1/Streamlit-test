import streamlit as st

st.write(':blue-background[아이디]')
id = st.text_input("answersheet")
st.write(':blue-background[비밀번호]')
password = st.text_input("answersheet")
submit = st.button("Login", type="primary")
if id and password:
    st.session_state.id = id
    st.session_state.password = password