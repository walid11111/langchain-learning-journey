# this below code only for static webside 
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# # ✅ Load a normal webpage (not PDF)
# url = "https://www.uetmardan.edu.pk/uetm/about"
# loader = WebBaseLoader(url)
# docs = loader.load()

# page_text = docs[0].page_content[:2000]  # take first 2000 chars for speed

# # Prepare the model
# template = PromptTemplate(
#     template="Answer the question: {question}\nUsing the following context:\n{text}",
#     input_variables=["question", "text"]
# )

# model = ChatGroq(model="llama-3.3-70b-versatile")

# parser = StrOutputParser()

# chain = template | model | parser

# # Ask the question
# question = "what is the Message of  Vice Chancellor of UET Mardan?"
# result = chain.invoke({"question": question, "text": page_text})

# print(result)



# the above code not give the output becuse  The page “https://www.uetmardan.edu.pk/uetm/Site/vcmessage”
#  is dynamically rendered — meaning the message content (the text you see in the screenshot) is loaded by JavaScript after the page loads in your browser.

# But WebBaseLoader (and requests under the hood) can only fetch static HTML — it doesn’t execute JavaScript.
# So the actual message text never appears in the HTML it downloads.

# That’s why your model says:

# “The provided context does not contain the actual message...”


# Way to fix it 
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

urls = ["https://www.uetmardan.edu.pk/uetm/Site/vcmessage"]

loader = SeleniumURLLoader(urls=urls)
docs = loader.load()

page_text = docs[0].page_content

template = PromptTemplate(
    template="Answer the question: {question}\nUsing the following context:\n{text}",
    input_variables=["question", "text"]
)

model = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()
chain = template | model | parser

question = "What is the message of the Vice Chancellor of UET Mardan?"
result = chain.invoke({"question": question, "text": page_text})

print(result)
