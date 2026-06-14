from langchain_community.document_loaders import TextLoader

data = TextLoader("document loaders/notes.txt")
# Text Loader loads text files
docs = data.load()

# print(docs)
# ye ham data ko print karnge but metadata ke sath

print(docs[0].page_content)
# jo to temletea hai wo prompt varible me store kar ke ham 0 index maltble starting se start kargene read kar na aur staring ka hi data dega only

# ye ham data ko print karnge but metadata ke sath nahi only content

print(len(docs))
# its give the length on the data
