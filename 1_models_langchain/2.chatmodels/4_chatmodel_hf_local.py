from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
import os

os.environ['HF_HOME']='D:/huggingface_cache'
llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
      max_new_tokens=100,
      temperature=0.5
       )
    

)

'''pipe = pipeline(
    task="text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100,
    temperature=0.5
)'''

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)

# this is the method of locally download but now in my pc no space (for torch libaray install ) that why create a problem but the mathod is same
