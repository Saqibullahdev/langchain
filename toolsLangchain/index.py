# # 


# from langchain.tools import StructuredTool
# from langchain_core.tools import ToolException

# def execption(s:str):
#     raise ToolException(s)
# def test():
#     return "test" 

# test=StructuredTool.from_function(
#     func=test,
#     name="test",
#     description="Test function",
#     handle_tool_error=True
    
# )    



from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Look up things online."""
    return "LangChain"

print(search.args)  # {'query': {'title': 'Query', 'type': 'string'}}


from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def search(query: str) -> str:
    """Look up things online."""
    return "LangChain"

# print(search.name)  # "custom_search_tool"
# print(search.description)  # "Perform an online search."
# print(search.args)  # {'query': {'title': 'Search query text', 'description': 'Search query text', 'type': 'string'}}
# print(search.return_direct)  # True
# print(search.args_schema)  # <class 'SearchInput'>

from langchain_core.tools import ToolException
from langchain.tools import StructuredTool

def search_tool1(s: str):
    raise ToolException("The search tool1 is not available.")

search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="A bad tool",
    return_direct=True,
)

