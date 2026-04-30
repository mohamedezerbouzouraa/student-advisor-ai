import asyncio
from runner_setup import runner, USER_ID, SESSION_ID
async def call_agent_async(query: str):
    final_response_text = "No response."
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=query):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            break
    print(f"\n🎓 Advisor: {final_response_text}")
