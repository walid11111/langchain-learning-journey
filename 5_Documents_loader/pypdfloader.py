from langchain_community.document_loaders import PyPDFLoader, PDFPlumberLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os


loader = PyPDFLoader('Lecture_05_Stacking.ppt[1].pdf')

docs = loader.load()

# print(docs)
# print(len(docs))
print(docs[0])



# loader1= PDFPlumberLoader('sample_tables.pdf')
# docs1=loader1.load()
# print(docs1)