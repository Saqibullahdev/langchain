
"""
- sometime we want to store chat history 
if user ask question related to previous question then 
we can use this chat history to answer the question

- Langchain provide memory buffer to store chat history

Different type of memory buffer
1 ConversationBufferMemory
   - It store all chat history
   - drawback: it store all chat history so it can increase input size
   - while llm model have input size limit

2 ConversationBufferWindowMemory
    - It store chat history in window of size k
    - It store only k chat history
    - It can be useful when we want to store only recent chat history
    example: if we want to store only last 3 chat history then we can use k=3
    -it will never increase input size
3- ConversationSummaryMemory

    Instead of remembering the exact conversation, 
    can we summarize the previous conversation context and hence 
    help the LLM in answering the upcoming question? 
    This is how Summary Memory helps.
    It keeps on summarizing the previous context and 
    maintains it for use in next discussion.
    example:
    memory= ConversationSummaryMemory(llm=llm, max_token_limit=100)

4- ConversationSummaryBufferMemory
    ConversationSummaryBufferMemory combines the ideas behind BufferMemory and ConversationSummaryMemory.
    It keeps a buffer of recent interactions in memory,
    but rather than just completely flushing old interactions
    it compiles them into a summary and uses both. 
    Unlike the previous implementation though,
    it uses token length rather than number of 
    interactions to determine when to flush interactions.
    
    it has argument= max_token_limit
    base on this token limit it can generate summary
    if token_limit=100
    it will generate summary of 100 token



"""

from langchain.memory.buffer import ConversationBufferMemory
from langchain.memory.buffer_window import ConversationBufferWindowMemory
from langchain.memory import ConversationSummaryMemory
from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
from langchain.chains.conversation.base import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

# meomry=ConversationBufferMemory()
# meomry=ConversationBufferWindowMemory(k=3)
# meomry=ConversationSummaryMemory(llm=llm) #it take llm for summarization
meomry=ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
chain=ConversationChain(memory=meomry, llm=llm)

while True:
    user_input=input("You: ")
    response=chain.invoke(user_input)
    print("Bot: ",response)
    if user_input=="exit":
        break