from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model='text-embidding-3-large',dimentions=32)

documents = [
     "my name is walid ",
     "from paskistan",
     "what is your country name"
 ]
result=embedding.embed_documents(documents)
print(str(result))

# but this not work becuse this is a code for embeddding and used the paid embedding model


