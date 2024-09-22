from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
"""
1- Import the SimpleSequentialChain class from the langchain.chains.sequential module.
2- Import the LLMChain class from the langchain.chains.llm module.

Note: The SimpleSequentialChain can also import from langchain.chains.base module. 
"""
from langchain.chains.sequential import SimpleSequentialChain
from langchain.chains.llm import LLMChain
 
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

# chain= prompt | llm


"""
    2nd Method to create prompt template
1- Create a new instance of the PromptTemplate class.
2- Pass the template string to the constructor.
3- Pass the input_variables list to the constructor.
4- The input_variables list contains the names of the variables in the template string.


"""


# prompt2=PromptTemplate(template="what is mean by {word}" ,input_variables=['word'])
# chain2= prompt2 | llm
# print(chain2.invoke({'word':'apple'}))


"""
Passing multiple variables to the prompt template
"""


# prompt3=PromptTemplate(template="what is mean by {word} and {word2}" ,input_variables=['word','word2'])
# chain3= prompt3 | llm
# print(chain3.invoke({'word':'apple','word2':'orange'}))


# Chains in LangChain are used to combine multiple components together.

prompt1=PromptTemplate.from_template("what is mean by {word}")
prompt2=PromptTemplate.from_template("write a sentence using the word {word}")
"""
1- Create a new instance of the SimpleSequentialChain class.
2- Pass the chains list to the constructor.
3- The chains list contains the components that will be executed in sequence.

Flow: 
1- The prompt1 component is executed first. 
2- The output of prompt1 is passed to the prompt2 component.
3- The prompt2 component is executed next.
4- Output of prompt2 is returned as the final output.

Benefit Of PromptTemplate Here With SimpleSequentialChain:
1- Output of prompt1 is passed to prompt2 automatically.
2- No need to pass the output of prompt1 to prompt2 manually.


"""

"""
create chain Using LLMChain
it work with SimpleSequentialChain
if we create chain using pipe symbol it will not work
"""
chain1=LLMChain(llm=llm, prompt=prompt1)
chain2=LLMChain(llm=llm, prompt=prompt2)
# finalChain = SimpleSequentialChain(chains=[chain1,chain2])

# Call the invoke method on the chain object to execute the components in sequence.

# result=finalChain.invoke("apple")
# print(result)



"""
Another way to create llm chat instance
ChatGoogleGenerativeAI:
1- Create a new instance of the ChatGoogleGenerativeAI class.
2- Pass the API key and model name to the constructor.
3- The model name is gemini-1.5-flash.

Main Difference Between GoogleGenerativeAI and ChatGoogleGenerativeAI:
the ChatGoogleGenerativeAI class is designed 
to give responses to user queries in a conversational manner.
ChatGoogleGenerativeAI give extra field in output which is response
like: token, response, prompt, model, model_version, api_key, timestamp, id
"""
from langchain_google_genai import ChatGoogleGenerativeAI

# llm2=ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=gemini_api_key)

promptNew=PromptTemplate.from_template("what is mean by {word}")
# chainNew= promptNew | llm2
# print(chainNew.invoke({'word':'give up'}))
