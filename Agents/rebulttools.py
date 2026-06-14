# Load environment variables from .env file (e.g., TAVILY_API_KEY)
from dotenv import load_dotenv
load_dotenv()

# Updated import: using the new standalone langchain-tavily package
# instead of the deprecated langchain_community.tools.tavily_search
from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize Tavily search tool with max 5 results
search_tools = TavilySearch(max_results=5)

# Initialize Mistral AI model
llm = ChatMistralAI(model="mistral-small-2506")

# Create a prompt template for summarizing news into bullet points
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant 
    summarize the following news into clear bullet points
    {news}
    """
)

# Build the chain: prompt → LLM → string output parser
chain = prompt | llm | StrOutputParser()

# Run Tavily search for latest AI news of 2026
news_result = search_tools.run("Latest Ai news of 2026")

# Pass the search results into the summarization chain
result = chain.invoke({"news": news_result})

# Print the summarized bullet points
print(result)