# Load environment variables from .env file (e.g., API keys for MistralAI)
from dotenv import load_dotenv
load_dotenv()

# Import LangChain components:
# - ChatMistralAI: The LLM model from Mistral AI
# - ChatPromptTemplate: Template to structure prompts for the LLM
# - StrOutputParser: Parses the raw LLM response into a readable string
# - RunnableParallel: Allows running multiple chains IN PARALLEL on different inputs
# - RunnableLambda: Wraps a custom Python function as a LangChain runnable component
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda


# --- Shared Components ---
# Initialize the Mistral AI model (both chains will use the same model instance)
model = ChatMistralAI(model="mistral-small-2506")
# Create a string output parser to convert LLM responses into plain text
parser = StrOutputParser()

# --- Prompt 1: Short Explanation ---
# This prompt asks the AI to explain a topic very concisely (1-2 lines)
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

# --- Prompt 2: Detailed Explanation ---
# This prompt asks the AI to explain a topic in depth
detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

# --- Parallel Chain Setup ---
# RunnableParallel allows running multiple independent chains simultaneously.
# Each key in the dictionary defines a separate parallel branch:
#
# - "short" branch:
#   1. RunnableLambda(lambda x: x['short']): Extracts the "short" key from the input dict
#      (i.e., {"topic": "Machine Learning"} for the short explanation)
#   2. short_prompt: Formats the prompt with the extracted topic
#   3. model: Sends to Mistral AI
#   4. parser: Converts to plain text
#
# - "detailed" branch:
#   1. RunnableLambda(lambda x: x['detailed']): Extracts the "detailed" key from the input dict
#      (i.e., {"topic": "Deep Learning"} for the detailed explanation)
#   2. detailed_prompt: Formats the prompt with the extracted topic
#   3. model: Sends to Mistral AI
#   4. parser: Converts to plain text
#
# Both branches run in parallel (concurrently) and complete independently.
chain = RunnableParallel({
    "short": RunnableLambda(lambda x: x['short']) | short_prompt | model | parser,
    "detailed": RunnableLambda(lambda x: x['detailed']) | detailed_prompt | model | parser
})

# --- Invocation ---
# Pass a dictionary where each key corresponds to a branch name.
# Each branch receives its OWN dedicated sub-input:
# - "short" branch receives: {"topic": "Machine Learning"}
# - "detailed" branch receives: {"topic": "Deep Learning"}
result = chain.invoke({
    "short": {"topic": "Machine Learning"},
    "detailed": {"topic": "Deep Learning"}
})

# Print the short explanation of Machine Learning
print(result['short'])
# Print the detailed explanation of Deep Learning
print(result['detailed'])