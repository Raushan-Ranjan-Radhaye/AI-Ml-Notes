# Load environment variables from .env file (e.g., API keys for MistralAI)
from dotenv import load_dotenv
load_dotenv()

# Import LangChain components:
# - ChatMistralAI: The LLM model from Mistral AI
# - ChatPromptTemplate: Template to structure prompts for the LLM
# - StrOutputParser: Parses the raw LLM response into a readable string
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# --- Prompt Definition ---
# Create a prompt template that takes a "topic" input from the user
# and asks the AI to explain that topic in simple words
prompt = ChatPromptTemplate.from_template(
    "Expalin {topic} in simple words"
)

# Initialize the Mistral AI model (small variant)
model = ChatMistralAI(model="mistral-small-2506")

# Create a string output parser to convert LLM responses into plain text
parser = StrOutputParser()

# --- Sequential Chain ---
# The pipe (|) operator chains components together sequentially:
# 1. prompt: Takes input {"topic": "Machine Learning"} and formats it into a full prompt message
# 2. model: Sends the formatted prompt to Mistral AI, which generates a response
# 3. parser: Converts the AI's raw response into a clean string
# The output of one component becomes the input of the next
chain = prompt | model | parser

# --- Invocation ---
# Execute the chain by passing the input data
# The chain will:
#   1. Format the prompt with topic="Machine Learning"
#   2. Send to Mistral AI for explanation
#   3. Parse and print the plain text response
print(chain.invoke({"topic": "Machine Learning"}))