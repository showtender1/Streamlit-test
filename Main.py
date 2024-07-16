import streamlit as st

st.title('MY BLOG')
st.markdown('''
            :rainbow[Fun facts about streamlit!]''')
st.markdown('''***streamlit*** can help you design :red-background[E A S Y !]''')

st.header('Explanation about tags with :rainbow[cool divider]', divider='rainbow')
st.subheader('st.write')
st.markdown(''':rainbow[st.write write every texts!!!]''')
code = '''import streamlit as st
st.write('Hello, *World!* :sunglasses:')'''
st.code(code, language='python')

st.subheader(':rainbow[Solve Quiz!!!!!!!!!!!]')
st.subheader(':rainbow[Quiz 1!!!!]')
quiz1 = st.radio(
    ":rainbow[What is the best movie of the world?]",
    [":red[성냥팔이 소녀의 재림]", ":orange[클레멘타인]", ":blue[드래곤볼 실사판]", ":green[300(made in china)]"]
)
quiz1_submit = st.button("Submit Quiz 1", type="primary")

if quiz1_submit:
    if quiz1 == ":red[성냥팔이 소녀의 재림]":
        st.session_state.quiz1 = 'correct'
    else:
        st.session_state.quiz1 = 'false'

st.subheader(':rainbow[Quiz 2!!!!!!!!]')
st.image('샤크네이도.webp')
st.write(':blue-background[위 작품의 제작사는 어디인가]')
answer2 = st.text_input("answersheet")
quiz2_submit = st.button("Submit Quiz 2", type="primary")
if quiz2_submit and answer2:
    st.session_state.answer2 = answer2

