from langchain_openai import OpenAI # lanchain_openAi is module or pakage and openAI is a class that we import from it
from dotenv import load_dotenv    # dotenv is also a package  and the laod_dotenv is a function inside it. it used to load your api keys from .env file
load_dotenv()

llm =open(model="gpt-3.5-turbo-intruct")
Result=llm.invoke("what is the capital if indua")
print(Result) # this will print the result of the llm.invoke method which is the response from the model

# this will not print the result becuse i have not api paid key just learn that how it works
# not used this code becuse it is old we will be used the chat model