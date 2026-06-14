# Load environment variables from .env file (e.g., API keys for MistralAI)
from dotenv import load_dotenv
load_dotenv()

# Import LangChain components:
# - ChatMistralAI: The LLM model from Mistral AI
# - ChatPromptTemplate: Template to structure prompts for the LLM
# - StrOutputParser: Parses the raw LLM response into a readable string
# - RunnableParallel: Allows running multiple chains in parallel
# - RunnablePassthrough: Passes input data through unchanged (useful for splitting pipelines)
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


# Initialize the Mistral AI model (small variant, released in 2025/06)
model = ChatMistralAI(model="mistral-small-2506")
# Create a string output parser to convert LLM responses into plain text
parser = StrOutputParser()

# --- Prompt 1: Code Generator ---
# This prompt instructs the AI to act as a code generator
# Takes a "topic" (e.g., "palindrome in python") and generates code for it
code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

# --- Prompt 2: Code Explainer ---
# This prompt instructs the AI to explain code in simple, beginner-friendly terms
# Takes the generated "code" and explains what it does
explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
])

# --- Chain 1 (seq): Sequential pipeline to generate code ---
# Steps:
# 1. code_prompt: Takes input {"topic": "..."} and formats the prompt
# 2. model: Sends the formatted prompt to Mistral AI to generate code
# 3. parser: Converts the AI response into plain text (the generated code)
seq = code_prompt | model | parser 

# --- Chain 2 (seq2): Parallel pipeline using generated code ---
# RunnableParallel runs multiple chains simultaneously on the same input.
# Input to this chain will be the output of seq (the generated code).
# Structure:
# - "code" key: RunnablePassthrough passes the input through AS-IS
#   (so the generated code is stored under result['code'])
# - "explanation" key: Runs another chain that:
#   1. explain_prompt: Takes the input (the generated code) and creates an explanation prompt
#   2. model: Sends it to Mistral AI to get an explanation
#   3. parser: Converts to plain text
#   Result stored under result['explanation']
seq2 = RunnableParallel(
    {"code": RunnablePassthrough(),
     "explanation": explain_prompt | model | parser
    }
)

# --- Full Pipeline: Code Generation → Parallel Code + Explanation ---
# Steps:
# 1. seq: Takes {"topic": "..."} → generates code
# 2. seq2: Takes the generated code and:
#    a. Passes it through as-is (stored under "code")
#    b. Creates an explanation of the code (stored under "explanation")
chain = seq | seq2

# --- Execution ---
# Invoke the entire pipeline with a topic for code generation
result = chain.invoke({"topic": "please write a code of palindrome in python "})

# Print the generated palindrome code
print(result['code'])
# Print the explanation of what the code does
print(result['explanation'])