from langchain_community.document_loaders import WebBaseLoader
# WebBaseLoader loads data from web page
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
# give the url of the web page from which we want to load the data
data = WebBaseLoader(url)
# data varible me ham store kar rahi hai url se data load kar ke
docs = data.load()

print(len(docs))
print(docs[0].page_content)
# jo to temletea hai wo prompt varible me store kar ke ham 0 index maltble starting se start kargene read kar na aur staring ka hi data dega only
