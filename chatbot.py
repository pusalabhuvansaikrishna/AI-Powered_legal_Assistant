import streamlit as st
st.title('AI Powered DOC Summary')

with st.chat_message("User",avatar='🤖'):
  st.write("Hello")

if "messages" not in st.session_state:
  st.session_state.messages=[]

for message in st.session_state.messages:
  with st.chat_message(message['role']):
    st.markdown(message['content'])


if prompt:=st.chat_input("Enter your Query"):
  with st.chat_message('user'):
    st.markdown(prompt)


st.session_state.messages.append({"role":"user","content":prompt})

response='Echo: hellooo'

with st.chat_message('assitant'):
  st.markdown(response)

st.session_state.messages.append({'role':'assitant','content':response})