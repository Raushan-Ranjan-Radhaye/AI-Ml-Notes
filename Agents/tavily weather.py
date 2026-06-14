from dotenv import load_dotenv
load_dotenv()

import os

import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool

from langchain_core.prompts import HumanMessage, ToolMessage
from langchain_core.output_parsers import StrOutputParser
from tavily import TavilyClient

def get_weather(city:str) -> str:
    """ Get Current weather of a city """
    tavily = TavilyClient(os.getenv("TAVILY_API_KEY"))
    return tavily.get_weather(city)
