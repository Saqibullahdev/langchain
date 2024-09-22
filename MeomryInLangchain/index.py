"""
Meomry In Langchain

when you want to remember something,and give back to LLM, you can use this tool to help you.

for example:
when user ask five questions, and when user ask what is the answer of question 1, by default,LLM don't know the answer,
but we  can use langchain function to remember the answer of question 1, 
and give back to LLM, so that LLM can answer the question next time.


challenge:
keeping chat history in memory, and give back to LLM is
a big challenge, because the memory is limited,
2nd challenge is how LLM can process this large input 
as LLM has limited input size.

solution:
langchain function can help to solve this problem,

like: save summary of chat history
save window of chat history,mean
keep track of previous 5,10 chat history
"""


from langchain.schema import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


llm=GoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-1.5-flash")

prompt=ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant! Your name is Bob."),
])

"""
This is a simple example of how to use langchain to remember something, and give back to LLM
but this is not effiective way to remember something, because 
it increase the input size, and LLM has limited input size.
"""
while True:
    userInput=input("ask me something:")
    message=HumanMessage(content=userInput)
    prompt.append(HumanMessage(content=userInput))
    res=llm(prompt.format())
    print("Ai response:",res)
    prompt.append(AIMessage(content=res))
    print("prompt till now:",prompt.format())
