from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables (.env se GROQ_API_KEY uthayega)
load_dotenv()

# Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",  # aap yahan koi bhi supported Groq model rakh sakte ho
    temperature=0.1,
    max_tokens=512
)

# Directly use invoke
result = llm.invoke("What is the capital of Pakistan?")
print(result.content)
