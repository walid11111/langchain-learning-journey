from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os

load_dotenv()

print(os.getenv("GROK_API_KEY"))

prompt1=PromptTemplate(
    template="write a joke of a topic {topic}",
    input_variable=["topic"]
)

model=ChatGroq(
      model="llama-3.3-70b-versatile"
)


parser=StrOutputParser()


prompt2=PromptTemplate(
    template="Explain the following joke {text}",
    input_varaible=['text']
)

chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result= chain.invoke({"topic : pakistan"})
print("Result:",result)