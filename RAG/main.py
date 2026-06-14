from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# We are Loaded the data 
data = TextLoader("document loaders/notes.txt")
# data varible me ham store kar rahi hai document loaders/notes.txt file ka content. Ye file me hamara text hoga jise ham summarize karna chahte hai.
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [("system", "You are a AI assistant that summarizes the text"),
    #  "system la matlab hi ki ham ai ko bata rahi hai ki wo kay kaam karega mera data ke sath"
     ("human", "{data}")]
    # give the my data 
)

prompt = template.format_messages(data=docs[0].page_content)
# jo to temletea hai wo prompt varible me store kar ke ham 0 index maltble starting se start kargene read kar na aur staring ka hi data dega only
# page_content ka matlab hi ki ye hamko maeta data nahi dena only content

model = ChatMistralAI(model = "mistral-small-2506")
result = model.invoke(prompt)
# apne deta ko ham ai ko de rahi hia reade kar ke process kaega 
print(result.content)