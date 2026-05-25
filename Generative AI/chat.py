
from dotenv import load_dotenv

load_dotenv()
# ye sab ham dotenv file ko import kar rahi hai data aayega waha se


from langchain.chat_models import init_chat_model
# ye ham langchain ko import kar rah hai
model = init_chat_model('llama-3.3-70b-versatile', model_provider='groq')
# init_model me ham ye likete hai ki konsa model use hoga

# print(model)
# isise pata chalte hai ki kons sa model use ho raha hai

response = model.invoke("what is the meaning of life?")
# invoke karne se hma koi bhi question puch sakte hai aur iska answer mil jayega
print(response.content)
# (content) ye bass ans ko print karne ke liye use hota hai baki kuch nahi readaable format ke liya

