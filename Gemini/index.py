from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

"""
1- Create a new instance of the GoogleGenerativeAI class.
2- Pass the API key and model name to the constructor.
3- The model name is gemini-1.5-flash.
"""


"""
1- One way to use the GoogleGenerativeAI class is to call the invoke method.

"""
llm=GoogleGenerativeAI(model="gemini-1.5-flash", api_key=gemini_api_key)
# res=llm.invoke("Hello, how are you?")


"""
         creating prompt template 1st way
 1- Create a new instance of the PromptTemplate class.
 2- Call the from_template method to create a new prompt template.
3- Pass the template string to the from_template method
"""
prompt=PromptTemplate.from_template("what is mean by {word}")

chain= prompt | llm


"""
    2nd Method to create prompt template
1- Create a new instance of the PromptTemplate class.
2- Pass the template string to the constructor.
3- Pass the input_variables list to the constructor.
4- The input_variables list contains the names of the variables in the template string.


"""


prompt2=PromptTemplate(template="what is mean by {word}" ,input_variables=['word'])
chain2= prompt2 | llm
# print(chain2.invoke({'word':'apple'}))


"""
Passing multiple variables to the prompt template
"""


prompt3=PromptTemplate(template="what is mean by {word} and {word2}" ,input_variables=['word','word2'])
chain3= prompt3 | llm
# print(chain3.invoke({'word':'apple','word2':'orange'}))