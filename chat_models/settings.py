from dotenv import load_dotenv
import os

load_dotenv()

class Utils:
    gemini_flash: str = "gemini-1.5-flash"
    gemini_pro:str = "gemini-1.5-pro"

    fire_proj_id = os.getenv("FIRE_PROJ_ID")
    session_id = "user_session_new"
    collection = "chat_history"
utils = Utils()