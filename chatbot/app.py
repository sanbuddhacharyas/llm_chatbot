# Import Langchain packages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

# Define environment
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY']     = os.getenv("LANGCHAIN_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assitant. Please help the user to solve the problem. Do not provide any suggetions or information only proivde what is asked "),
        ("user", "Question:{question}")
    ]
)


# Streamlit framework
st.title("ChatBot")
input_text = st.text_input("What do you want to ask?")

# OpenAI LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo")
# output_parsers = StrOutputParser()
# chain = prompt | llm | output_parsers

# OLAMMA
llm = Ollama(model='llama2')
output_parsers = StrOutputParser()
chain = prompt | llm | output_parsers

if input_text:
    st.write(chain.invoke({'question':input_text}))

