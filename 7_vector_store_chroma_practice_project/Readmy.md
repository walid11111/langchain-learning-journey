📁 Folder Structure for Your ChromaDB Practice Project
📂 chroma_practice_project/
│
├── create_embeddings.py        # ✅ Run once to create & store embeddings
├── query_chroma.py             # ⚡ Run anytime to query instantly
│
├── requirements.txt            # (Optional) List of dependencies
│
└── 📂 my_chroma_db/            # 🧠 Persistent Chroma Database (auto-created)
    ├── chroma.sqlite3          # Stores metadata, doc info, IDs
    ├── collections/            # Contains info about each collection (like “my_docs”)
    ├── index/                  # Stores actual embedding vectors
    └── lock                    # Internal file (ignore)