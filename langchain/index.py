from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import Ollama

# Prompt

promt=ChatPromptTemplate.from_messages([
    ("system","Hello, I am a language model trained on the Bible. I can help you with any questions you have about the Bible. if any question, out of bible, I will try to answer that i dont know."),
    ("user","What is the {question}?"),
])

# set model
llm=Ollama(model="qwen:1.8b")

# set output parser
output_parser=StrOutputParser()

# Chain
chain=promt|llm|output_parser
result=chain.invoke({'question':st.text_input("Please enter your question:")})
print(result)
