
from dotenv import load_dotenv

load_dotenv()
# ye sab ham dotenv file ko import kar rahi hai data aayega waha se


from langchain.chat_models import init_chat_model
# ye ham langchain ko import kar rah hai
model = init_chat_model('gemini-2.5-flash-lite', model_provider='google_genai', temperature=0.7)
# (temperature) jaise jaise increase hoga waise waise model ke ans me creativity aayegi, 0.7 ek acha value hai, isse zyada karne se ans me galtiya aane ke chances badh jate hai

# init_model me ham ye likete hai ki konsa model use hoga

# print(model)
# isise pata chalte hai ki kons sa model use ho raha hai

response = model.invoke("what is the story of Ramayana?")
# invoke karne se hma koi bhi question puch sakte hai aur iska answer mil jayega
print(response.content)
# (content) ye bass ans ko print karne ke liye use hota hai baki kuch nahi readaable format ke liya

