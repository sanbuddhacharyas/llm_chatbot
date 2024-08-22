from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn

import os

from dotenv import load_dotenv

load_dotenv()

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assitant. Please help the user to solve the problem. Do not provide any suggetions or information only proivde what is asked "),
        ("user", "Question:{question}")
    ]
)

llm = Ollama(model='llama2')
output_parsers = StrOutputParser()
chain = prompt|llm|output_parsers

# Create a fast api app
app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A simple chatbot'
)

add_routes(
    app,
    prompt | llm,
    path='/helpme'
)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)