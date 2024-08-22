import requests
import streamlit as st

def communicate_chatbot(input_text):
    response = requests.post("http://localhost:8080/helpme/invoke", 
                             json={'input':{'question':input_text}})
    

    return response.json()['output']


st.title('My Practise')
input_text = st.text_input('Type any thing you can')

if input_text:
    st.write(communicate_chatbot(input_text))
