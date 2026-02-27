from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_groq import ChatGroq   # ✅ Groq integration
import logging

# --- Logging Setup ---
logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

# 1. Define Documents
docs = [
    Document(page_content="The sun is a star at the center of the solar system."),
    Document(page_content="Solar energy is a renewable source of energy."),
    Document(page_content="Planetary orbits are governed by gravitational forces."),
    Document(page_content="Mars is known as the Red Planet and is the fourth planet from the Sun."),
    Document(page_content="Jupiter, the largest planet, has a Great Red Spot, a massive storm."),
    Document(page_content="Quantum computing uses principles of quantum mechanics to process data."),
    Document(page_content="The development of large language models (LLMs) has accelerated AI progress."),
    Document(page_content="LLMs are trained on vast amounts of text data to predict the next word."),
    Document(page_content="Retrieval-Augmented Generation (RAG) improves LLM factual accuracy."),
    Document(page_content="The core of the Earth is extremely hot and mostly iron-nickel alloy.")
]

# 2. Create Embeddings and Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding=embeddings)
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. Create Groq LLM
llm = ChatGroq(
    model="llama3-8b-8192",  # ✅ Fast and smart Groq model
    temperature=0,
    groq_api_key="YOUR_GROQ_API_KEY"  # 🔑 Replace with your actual API key
)

# 4. Create MultiQueryRetriever
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm,
    include_original=True
)

# 5. Define Query
query = "What information do you have about planets and AI technologies?"

print(f"\n--- Original Query: '{query}' ---\n")

# 6. Run the retriever
retrieved_docs = multi_query_retriever.invoke(query)

# 7. Print Results
print("\n" + "="*50)
print(f"Total Unique Documents Retrieved: {len(retrieved_docs)}")
print("="*50)

for i, doc in enumerate(retrieved_docs):
    print(f"--- Document {i+1} ---")
    print(doc.page_content)
