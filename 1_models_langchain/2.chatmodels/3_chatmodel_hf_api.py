from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"   # ✅ correct argument
)


model= ChatHuggingFace(llm=llm)
result=model.invoke('what is the capital of india')
print(result.content)


# this is model this time give error becuse it server is busy