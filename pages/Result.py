import streamlit as st

st.title('Results Page')
score = 0
if 'quiz1' in st.session_state:
    score += 40
else:
    st.write("틀렸는데 ㅋ")
if 'answer2' in st.session_state:
    if st.session_state.answer2 == '어사일럼':
        score += 60    
else:
    st.write("틀렸는데 ㅋ")
st.write(score)