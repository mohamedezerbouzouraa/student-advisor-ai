from config.settings import AGENT_MODEL, SYSTEM_PROMPT
import google.generativeai as genai

model = genai.GenerativeModel(AGENT_MODEL)

def build_prompt(user_message: str) -> str:
    return SYSTEM_PROMPT + "\n\nStudent: " + user_message
