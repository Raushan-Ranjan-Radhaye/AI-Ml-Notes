from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=10,
    # chunk_size ka matlab hi ki ham apne data ko kitne size ke hisab se split karna chahte hai.
    # Yaha ham 10 character ke hisab se split karna chahte hai.
    chunk_overlap=1,
    # chunk_overlap ka matlab hi ki ham apne data ko split karte time kitna overlap rakhna chahte hai.
    # Yaha ham 1 character ke hisab se overlap rakhna chahte hai.
    separator=""
    )

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

chunk = splitter.split_documents(docs)
print(chunk)
print(len(chunk))

# ye ham apne data ko split kar ke print karenge. Yaha hamne


for i in chunk:
    print(i.page_content)
    # ye ham apne split kiye gaye data ko print karenge. Yaha hamne page_content ka use kiya hai kyunki hamko sirf content chahiye tha metadata nahi chahiye tha.





