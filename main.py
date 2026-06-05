import asyncio
import sys
from interactive import interactive_mode

if __name__ == "__main__":
    if "ipykernel" in sys.modules:
        loop = asyncio.get_running_loop()
        task = loop.create_task(interactive_mode())
        try:
            loop.run_until_complete(task)
        except asyncio.CancelledError:
            pass
else:
        asyncio.run(interactive_mode())
