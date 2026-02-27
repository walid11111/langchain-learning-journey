from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnableParallel
import os

load_dotenv()

print(os.getenv("GROK_API_KEY"))

prompt1=PromptTemplate(
    template="Describe the concept of the topic in two lines {topic} ",
    input_variable=["topic"]
)

prompt2=PromptTemplate(
    template=" Generate the Question only from the {text}",
    input_varaible=['text']
)

model=ChatGroq(
      model="llama-3.3-70b-versatile"
)


parser=StrOutputParser()




chain=RunnableParallel({
    "concept" : RunnableSequence(prompt1, model, parser),
    "Question" : RunnableSequence(prompt2, model, parser)
})
result= chain.invoke({"topic : pakistan"})
print("Result:",result)