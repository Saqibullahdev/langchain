from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
import os
import json

# Load environment variables
load_dotenv()

# Create a tool
@tool
def regester_user(llmresult: str) -> str:
    """This tool processes the extracted user information."""
    print("Tool called")
    print("LLM result:", llmresult)

    # Parse the result (assuming LLM returns JSON)
    try:
        data = json.loads(llmresult)
        if not all(key in data for key in ['name', 'phone_number', 'email']):
            return json.dumps({"status": False, "message": "Missing required fields"})
        return json.dumps({"status": True, "message": "User registered successfully", "data": data})
    except json.JSONDecodeError:
        return json.dumps({"status": False, "message": "Invalid data format"})

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

# Create a runnable sequence
chain = RunnableSequence(
    prompt,
    llm,
    regester_user  # Middle step: LLM processing
)

# Provide the question as input
res = chain.invoke({"question": "my name is Saqib and phone number is 1234567890 and email is saqin@gmail.com"})

# Print the final result from the tool
print(res)
