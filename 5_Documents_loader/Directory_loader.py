

# when we have mutiple files in folder like multiple pdf files so you just save it in one folder and the DirectoryLoader ke through ap ussy sary files ku load kar sakty hai. 

# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# loader = DirectoryLoader(
#     path=r'D:\Langchain\files',  # ✅ full absolute path
#     glob='*.pdf',
#     loader_cls=PyPDFLoader
# )

# docs = loader.load()

# # print(docs)
# #print(len(docs))
# print(docs[1])







# # when you have multiple types of files present in the folder then you  can load it like this below 

# import glob
# from langchain_community.document_loaders import (
#     PyPDFLoader,
#     TextLoader,
#     CSVLoader,
#     UnstructuredWordDocumentLoader
# )

# path = r"D:\Langchain\files"
# docs = []

# for file in glob.glob(f"{path}/**/*", recursive=True):
#     if file.endswith(".pdf"):
#         loader = PyPDFLoader(file)
#     elif file.endswith(".txt"):
#         loader = TextLoader(file, encoding="utf-8")
#     elif file.endswith(".csv"):
#         loader = CSVLoader(file_path=file)
#     elif file.endswith(".docx"):
#         loader = UnstructuredWordDocumentLoader(file)
#     else:
#         continue  # skip unknown file types

#     docs.extend(loader.load())

# print(f"✅ Total documents loaded: {len(docs)}")
# print(docs[0].metadata)
# print(docs[0].page_content[:500])




# load()-------> Loads all documents immediately into memory (RAM). Returns a list of Document objects.
# Lazy load concept ---->  Loads documents one by one (like a generator) — doesn’t keep everything in memory at once. You can iterate over them gradually.


from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path=r"D:\Langchain\files",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

for doc in loader.lazy_load():  # loads one document at a time
    print(doc.metadata)
