# code to used the openAI paid model
from langchain_openai import ChatOpenAi
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAi(model="gpt-4",temperature=0.3,max_completion_token=10) # max_completion_token=10 mean llm resonce should bee 10 tokensit pad so according to your need tka eit
Result=model.invoke(" what is the capital of india")
print(Result)




