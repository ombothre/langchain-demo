from settings import utils

from google.cloud import firestore

from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

PROJ_ID = utils.fire_proj_id
SESSION_ID = utils.session_id
COLLECTION = utils.collection

# Firestore
client = firestore.Client(project=PROJ_ID)

# Chat History
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION,
    client=client
)
print("Current chat history: ", chat_history.messages)

# Chat Model

model = ChatGoogleGenerativeAI(model=utils.gemini_pro)

print("\n\nGemini 1.5 pro\n\n")
while True:
    query