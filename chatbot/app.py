# Import Langchain packages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

# Define environment
os.environ['LANGCHAIN_TRACKING_V2'] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_message(
    [
        ("system", "You are a helpful assitant. Please help the user to solve the problem"),
        ("user", "Question:{question}")
    ]
)


