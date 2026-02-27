# build-in_tool DuckDuckGo Search ---> is ky through ap direct web search se kuch be search akr sakty hu
from langchain_community.tools import DuckDuckGoSearchRun
search_tool= DuckDuckGoSearchRun()
Result=search_tool.invoke("what is the current situation of pakistan")
print(Result)
