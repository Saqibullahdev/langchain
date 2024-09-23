from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
import os
import json

content = f"""
Agents in Langchain:

Sometimes, we need to perform tasks like retrieving live weather data or calling an API to get specific information. By default, Large Language Models (LLMs) cannot handle such tasks, but we can use Langchain Agents to enable this functionality.

How It Works:
1. Tools:
   - We create tools that can perform specific tasks.
   - A tool is a simple function designed to accomplish a particular task.
   - Each tool must have:
     - Name: The identifier of the tool.
     - Description: A brief explanation of what the tool does.
     - Input: The required input for the tool to function.

2. Agents:
   - We create an agent and add these tools to the agent.
   - When interacting with an LLM, if we need to do something beyond its capabilities (e.g., fetching live weather data), the agent can handle the task using the appropriate tool.

Real-World Example:
Consider a web application where a user signs up by interacting with an LLM. The user can communicate with the LLM through voice or text, providing details like their name, phone number, and email. The LLM can then call an API to register the user and return a confirmation.

By default, an LLM cannot perform this kind of action (API calls, for instance), but by using Langchain Agents, it can be equipped with the necessary tools to achieve this task.
"""


# Load environment variables
load_dotenv()

# Create a tool
@tool
def regester_user(llmresult: str) -> str:
    """This tool processes the extracted user information."""
    print("Tool called")
    print("LLM result:", llmresult)

@tool
def getWeather(city: str) -> str:
    """This tool fetches live weather data for a specific city."""
    # Assume this function calls an external API to get weather data
    return f"Current weather in {city}: 25°C, sunny"
@tool
def bitcoinPrice(llm:str) -> str:
    """This tool fetches the current Bitcoin price."""
    # Assume this function calls an external API to get Bitcoin price
    return "Current Bitcoin price: $50,000"
    


# Ensure the API key is loaded
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables")

# Initialize the LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

# Create a prompt template with input variables
prompt = PromptTemplate(
    input_variables=["question"], 
    template=("You have to act as a tool caller. If someone asks '{question}', "
              "you have to pass the user data in JSON form to another tool. "
              "User will give name, phone number, and email. If any one of field "
              "is missing, send JSON with status: false. "
              "Format the output as 'name': 'name', 'phone_number': 'number', 'email': 'email'.")
)

# # Create a runnable sequence
# chain = RunnableSequence(
#     prompt,
#     llm,
#     regester_user  # Middle step: LLM processing
# )

# Provide the question as input
# res = chain.invoke({"question": "my name is Saqib and phone number is 1234567890 and email is saqin@gmail.com"})

# Print the final result from the tool
# print(res)



agent=initialize_agent(
    llm=llm,
    agent_type=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    tools=[getWeather, bitcoinPrice],
    verbose=True,
    max_iterations=4
)

while True:
    user_input = input("You: ")
    res=agent.run(user_input)
    print("Agent:", res)
    if user_input.lower() == "exit":
        break