from agents import Agent, run_demo_loop, enable_verbose_stdout_logging, set_default_openai_api
from dotenv import load_dotenv
import os
import asyncio
from rich import print

# enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",

)

async def main():
    await run_demo_loop(agent)
    

asyncio.run(main())