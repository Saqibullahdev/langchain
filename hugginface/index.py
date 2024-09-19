# %pip install --upgrade --quiet huggingface_hub
from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

st.header("Hugging face with Langchain 🦜")

repo_id ='mistralai/Mistral-Nemo-Instruct-2407'
# connecting to specific model
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
        temperature=0.7,
    
    huggingfacehub_api_token='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',

    
)

instructions = f"""
You will receive a prompt which needs to be modified. Please follow these guidelines for the modification:

1. Clarity: Ensure the prompt is clear and unambiguous. Remove any confusing language or jargon.
2. Purpose: Clearly articulate the goal or objective of the prompt, making sure it aligns with the intended outcome.
3. Context: Provide any necessary background information or context that might influence the modification.
4. Instructions: Outline specific modifications required, including format, style, or other relevant details.
5. Examples: If applicable, include examples to guide the modification process.
6. Constraints: Adhere to any limitations or boundaries mentioned, such as length, format, or specific conditions.
7. Audience: Consider the intended audience when making modifications, ensuring the prompt is appropriate for them.
8. Formatting: Follow any formatting guidelines provided for the modified prompt.

Please ensure the modified prompt aligns with these guidelines to meet the desired requirements.
you should return the modified prompt as response.

Note : you should not answer the question in the prompt, you should only modify the prompt,
the prompt will be in the form of a question.

return only the modified prompt as String.
"""




# creating prompt template
prompt=ChatPromptTemplate.from_messages(
    [
       ('system',instructions),
       ('human',    """ Prompt  is {question} """)
    ]
)


# creating chain 
chains=LLMChain(prompt=prompt,llm=llm)
input=st.text_input("Ask from chatbot")
if input:
    res=chains.run({'question':input})
    print(res)
    if res:	
        st.write(res)