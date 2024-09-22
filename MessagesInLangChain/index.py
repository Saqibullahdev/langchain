from langchain.schema import HumanMessage,AIMessage ,SystemMessage

"""
    Why Messages is important?

    Messages are the core of the conversation. They are the way the user and the system communicate with each other.
    Types of messages:
    1- HumanMessage: A message from the user Like 'what is C++'.
    2- AIMessage: A message from the system Like OpenAi or gemini etc. 'E.g. C++ is a programming language'.
    3- SystemMessage: A message for the System e,g 'Give Response in JSON format '.

    The schema module provides classes for these messages.

    for creating Chatbot that maintains a conversation with the user, we need to create a chain of messages.
    example:
    1- user ask a question
    2- system respond to the question
    3- user ask another question so
        without the chain of messages, the system will not be able to maintain the conversation 
        and will response according to New Prompt.

        with the chain of messages, the system will be able to maintain the conversation and respond 
        according to the previous message.
        the system will have contrext of the conversation.
"""


messages=[
    HumanMessage(content="what is C++"),
    SystemMessage(content="Answer Should be in JSON format"),
    AIMessage(content="C++ is a programming language"),
    HumanMessage(content="what is Python"),
    AIMessage(content="Python is a programming language")
]

messages.append(HumanMessage(content="what is Java"))

for message in messages:
    if isinstance(message,HumanMessage):
        print(f"User Asked: {message.content}")
    if isinstance(message,AIMessage):
        print(f"Ai response: {message.content}")    