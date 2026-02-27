from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os

load_dotenv()

print(os.getenv("GROK_API_KEY"))

# Load a text file
loader = TextLoader('description.txt')

# Convert into documents
documents = loader.load()
# print(len(documents))    
# print(Documents[0].page_content)
#print(Documents[0].meta_data)

prompt1=PromptTemplate(
    template="create three question from the provide text Document {documents}",
    input_variable=["documents"]
)


model=ChatGroq(
      model="llama-3.3-70b-versatile"
)


parser=StrOutputParser()

chain = prompt1 | model | parser

Result = chain.invoke(documents)

print(Result)  # shows first 2 docs
