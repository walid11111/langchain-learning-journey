import chromadb
from chromadb.utils import embedding_functions

# --- Step 1: Load the same embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --- Step 2: Connect to existing ChromaDB
client = chromadb.PersistentClient(path="my_chroma_db")

# --- Step 3: Load the collection
collection = client.get_collection(
    name="my_docs",
    embedding_function=embedding_function
)

# --- Step 4: Ask a question
query = input("💬 Ask something: ")

results = collection.query(
    query_texts=[query],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)

# --- Step 5: Show results with similarity scores
print(f"\n🔍 Query: {query}\n")
for doc, meta, score in zip(
    results["documents"][0],
    results["metadatas"][0],
    results["distances"][0]
):
    print(f"📄 Document: {doc}")
    print(f"🏷️ Metadata: {meta}")
    print(f"🎯 Similarity Score: {1 - score:.3f}\n")
