import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("ENDPOINT_URL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
OPENAI_API_VERSION = "2024-05-01-preview"
outputparser=StrOutputParser()

prompt=ChatPromptTemplate.from_messages([
    ("system","Hello, I am an AI assistant that helps people find information. I can help you with any questions you have."),
    ("user","What is the {question}?"),
])
llm = AzureOpenAI(api_version=OPENAI_API_VERSION, azure_endpoint=AZURE_OPENAI_ENDPOINT, api_key=AZURE_OPENAI_API_KEY, azure_deployment=DEPLOYMENT_NAME)

formatted_prompt=prompt.format_messages(question="capital of pakistan")
chain =formatted_prompt|llm|outputparser
response=chain.invoke({})
print(response)
# prompt






# azure=AzureChatOpenAI({
#     "endpoint":endpoint,
#     "deployment":deployment,
#     "subscription_key":subscription_key
# })
# response=azure.chat("What is the capital of France?")
# print(response)


# Initialize Azure OpenAI client with key-based authentication
# client = AzureOpenAI(
#     azure_endpoint = endpoint,
#     api_key = subscription_key,
#     api_version = "2024-05-01-preview",
# )

# completion = client.chat.completions.create(
#     model=deployment,
#     messages= [
#     {
#         "role": "system",
#         "content": "You are an AI assistant that helps people find information."
#     },
#     {
#         "role": "user",
#         "content": "What is the capital of France?"
#     },
    
# ],
#     max_tokens=800,
#     temperature=0.7,
#     top_p=0.95,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=None,
#     stream=False
# )

# result=completion.choices[0].message.content
# print(result)