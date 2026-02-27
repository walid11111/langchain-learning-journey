from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

Text = """Artificial Intelligence is changing the way we live and work. From voice assistants to recommendation systems,
         AI helps us make faster and smarter decisions every day. It learns from data and improves its performance with time.

         In education, healthcare, and business, AI offers endless possibilities. It helps teachers personalize lessons,
         doctors detect diseases early, and companies serve customers more efficiently."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0

)

result = splitter.split_text(Text)
print(len(result))
print(result)