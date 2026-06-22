import streamlit as st

from app import get_response

st.title("LangChain ChatBot")

st.write("A simple Chatbot built using LangChain, Groq and Streamlit")

user_input = st.text_input("Ask me anything: ")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)

        st.write("### Response")
        st.write(response)