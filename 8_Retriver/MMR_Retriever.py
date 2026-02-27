# MMR Retriever using FAISS (version-safe)
# ---------------------------------------

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Step 1: Create LangChain Documents
docs = [
    Document(page_content="Climate change increases global temperature.", metadata={"source": "Doc 1"}),
    Document(page_content="Rising CO2 levels cause global warming.", metadata={"source": "Doc 2"}),
    Document(page_content="Melting glaciers are caused by high temperatures.", metadata={"source": "Doc 3"}),
    Document(page_content="Climate change affects farming and food production.", metadata={"source": "Doc 4"}),
    Document(page_content="Climate change leads to floods and rising sea levels.", metadata={"source": "Doc 5"}),
]

# Step 2: Create Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 3: Create FAISS Vector Store
vectorstore = FAISS.from_documents(docs, embedding=embeddings)


# Step 5: Use FAISS’s built-in MMR search
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.5}    # LAmbda mean ke aghr 1 hu to normal smiler search ke tarah mmr ksearch karigha and below one then revellent and divecse search
)

# Step 4: Define the query
query = "effects of climate change"

# ✅ Step 6: Get top 3 results using MMR
results = retriever.invoke(query)

# ✅ Step 7: Print results
print("\n=== Top 3 Results from MMR (FAISS built-in) ===")
for i, doc in enumerate(results, 1):
    print(f"Result {i}: {doc.page_content} (Source: {doc.metadata['source']})")
