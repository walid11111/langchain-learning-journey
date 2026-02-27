from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
print(os.getenv("GROQ_APY_KEY"))

# Ist component 
prompt1=PromptTemplate(
    template="Generate details Report about user {topic}",
    input_variable=['topic']

)
model=ChatGroq(
    model="llama-3.3-70b-versatile"
)  # second component

parser = StrOutputParser()  #third component 

# now start chaining (and below when we create chain using this | its call langchain expression language)
chain= prompt | model | parser # now this my chain pipline
# next just trigger out it automatically run 
Result=chain.invoke({'topic':'footbal'})
print("result.content",Result)

chain.get_graph().print_ascii()    # just below print the prompt in flowchart