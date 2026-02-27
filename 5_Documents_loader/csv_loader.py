from langchain_community.document_loaders import CSVLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


loader = CSVLoader('sample_data.csv')

docs = loader.load()

#print(docs)
print(len(docs))
print(docs[0])    # it consider one row 



# now if you have so much big csv file then you can used the lazy_load instead of load()