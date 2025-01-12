from dotenv import load_dotenv
from settings import utils

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Loading the model
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model=utils.gemini_pro)

result = model.invoke("What is 60 + 9?")
print(result)
print(result.content)