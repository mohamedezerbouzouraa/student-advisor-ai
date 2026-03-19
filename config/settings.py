import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "PUT_YOUR_API_KEY_HERE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

APP_NAME = "adk_course_app"
USER_ID = "user_123"
SESSION_ID = "edu_session"

AGENT_MODEL = "gemini-2.5-flash-lite"
SYSTEM_PROMPT = """
