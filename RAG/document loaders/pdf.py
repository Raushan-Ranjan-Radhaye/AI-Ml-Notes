from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders/GRU.pdf")
# PyPDFLoader loads pdf files
docs = data.load()
# pdf ka data ko load karega
print(docs[0].page_content)
# (0) ka matlab hi ki indexing hai jo first index se data show hoga 
print(len(docs))
# its give the length on the data ki pdf me kitna page hai
