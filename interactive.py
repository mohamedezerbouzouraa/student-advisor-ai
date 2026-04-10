import asyncio
from app.utils import welcome_message
from agent_caller import call_agent_async
async def interactive_mode():
    welcome_message()
    while True:
        user_input = input("🧑 Your question: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        await call_agent_async(user_input)
