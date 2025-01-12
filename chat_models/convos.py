from dotenv import load_dotenv
from settings import utils

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# Loading the model
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model=utils.gemini_pro)

# Conversations
# System Mesaage - Default prompt
# Human and AI messages

messages = [
    SystemMessage(content="Solve the given math problems"),
    HumanMessage(content="What is 70 + 45?"),
    AIMessage(content="adding 45 to 70 gives 115"),
    HumanMessage(content="What is 60 + 9?")
]

result = model.invoke(messages)
print(result.content)