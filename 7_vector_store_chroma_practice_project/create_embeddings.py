import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# --- Step 1: Create embedding function from Hugging Face
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --- Step 2: Initialize Chroma with persistent storage
client = chromadb.PersistentClient(path="my_chroma_db")

# --- Step 3: Create or get the collection
collection = client.get_or_create_collection(
    name="my_docs",
    embedding_function=embedding_function
)

# --- Step 4: Add your sample documents with metadata
docs = [
    "Artificial intelligence is transforming industries across the world.",
    "The Eiffel Tower is located in Paris and attracts millions of visitors each year.",
    "Machine learning allows computers to learn patterns without being explicitly programmed."
]

metadatas = [
    {"source": "tech_article", "category": "AI"},
    {"source": "travel_blog", "category": "Tourism"},
    {"source": "education_note", "category": "Machine Learning"}
]

ids = ["doc1", "doc2", "doc3"]

# Add to Chroma
collection.add(
    documents=docs,
    metadatas=metadatas,
    ids=ids
)

print("✅ Documents added successfully and embeddings stored in 'my_chroma_db' folder!")
