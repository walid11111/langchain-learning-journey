# code to used the Anthropic model
from langchain import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model=ChatAnthropic(model="cloud-3.5-sqnnet-20241022")
Result=model.invoke(" what is the capital of india")
print(Result)