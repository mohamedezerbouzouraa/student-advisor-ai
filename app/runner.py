import asyncio
from google.api_core.exceptions import ResourceExhausted
from app.agent import model, build_prompt

class SimpleRunner:
    async def run_async(self, user_id, session_id, new_message):
        try:
            full_prompt = build_prompt(new_message)
            loop = asyncio.get_running_loop()
            response = await loop.run_in_executor(
                None, lambda: model.generate_content(full_prompt))
            class Event:
                def __init__(self, text):
                    self._text = text
                def is_final_response(self):
                    return True
                @property
                def content(self):
                    class Content:
                        def __init__(self, text):
                            self.parts = [type("Part", (), {"text": text})()]
                    return Content(self._text)

            yield Event(response.text)

        except ResourceExhausted:
            yield Event("⚠️ Quota exceeded. Try again later.")

        except Exception as e:
            yield Event(f"❌ Error: {str(e)}")
