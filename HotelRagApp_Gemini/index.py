import streamlit as st
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings  # Importing the GoogleGenerativeAI and GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader  # Loading the text from the file
from langchain.indexes import VectorstoreIndexCreator  # Storing the Embeddings in memory
from langchain.text_splitter import CharacterTextSplitter  # Splitting the text into characters
from dotenv import load_dotenv  # Loading the environment variables
import os  # Importing the os module

# Load environment variables
load_dotenv()

# Creating the instance of the GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

# Creating the instance of the GoogleGenerativeAIEmbeddings
llm_emb = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GEMINI_API_KEY"))

# Loading the text from the file
try:
    text = TextLoader("data.txt")
except Exception as e:
    st.error(f"Some error occurred: {e}")

# Splitting the text into characters
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# Creating the instance of the VectorstoreIndexCreator
index_creator = VectorstoreIndexCreator(embedding=llm_emb, text_splitter=text_splitter)

# Creating the index from the text
index = index_creator.from_loaders([text])

# Setting the title of the web app
st.title("HotelRagApp")
st.subheader("Welcome to the HotelRagApp Built with Langchain 🦜 + Google Gemini")

# Input field for user question
HumanQuestion = st.text_input("Ask a question related to the hotel")

# Querying the index with the user's question
if HumanQuestion:
    resultFromIndexDb = index.query(question=HumanQuestion, llm=llm)

    # Displaying the result from the index
    if resultFromIndexDb:
        st.write(resultFromIndexDb)
    else:
        st.write("No results found.")
