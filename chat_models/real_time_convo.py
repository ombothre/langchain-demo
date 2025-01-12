from dotenv import load_dotenv
from settings import utils

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# Loading the model
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model=utils.gemini_pro)

chat_history = [SystemMessage("You are a talkative extrovert friend")]

while True:
    query = input("You: ")
    if query == "exit" or query == "bye":
        break
    chat_history.append(HumanMessage(content=query))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print(f"AI: {result.content}")

print(f"Chat History: {chat_history}")