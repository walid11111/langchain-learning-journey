from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableBranch
from langchain_core.runnables import RunnableLambda

import os
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

print(os.getenv("GROK_API_KEY"))

# Schema
class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompts
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative:\n{feedback}\n{format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=['feedback']
)

# Model
model1 = ChatGroq(model="llama-3.3-70b-versatile")

# Parsers
parser = StrOutputParser()

# Chains
classifier_chain = prompt1 | model1 | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model1 | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model1 | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

# Test
feedback = """this is very good product"""
result = chain.invoke({"feedback": feedback})
print(result)

classifier_chain.get_graph().print_ascii()
