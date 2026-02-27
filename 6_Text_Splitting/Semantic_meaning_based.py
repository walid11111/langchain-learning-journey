from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# Example text
# --------------------------
text = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season.
The sun was bright, and the air smelled of earth and fresh grass.
The Indian Premier League (IPL) is the biggest cricket league in the world.
People all over the world watch the matches and cheer for their favourite teams.
Terrorism is a big danger to peace and safety.
It causes harm to people and creates fear in cities and villages.
When such attacks happen, they leave behind pain and sadness.
To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""


# Step 1: Create Document
# --------------------------
doc = Document(page_content=text)

# --------------------------
# Step 2: Use HuggingFace Embeddings
# --------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# --------------------------
# Step 3: Semantic Chunking
# --------------------------
# This line just creates (initializes) the semantic splitter object.
semantic_splitter = SemanticChunker(embeddings)   

"""👉 This below line that actually performs all the work.
When this line runs, it:

1: Takes your document (doc).
2: Splits it into small pieces (sentences or paragraphs).
3: Creates embeddings for each piece.
4: Measures their semantic similarity.
4: Groups similar sentences together into final chunks.
5: Returns those chunks in a list (like chunks = [...]).

"""
chunks = semantic_splitter.split_documents([doc])

print(len(chunks))
print(chunks)