from agents import Agent, Runner, enable_verbose_stdout_logging, set_default_openai_api, RawResponsesStreamEvent
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
import os
import asyncio
from rich import print

enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",

)

async def main():
    print("\n")
    result = Runner.run_streamed(starting_agent=agent, input="Hello")

    # async for event in result.stream_events():
    #     if event.type == 'run_item_stream_event':
    #         print("\n[EVENT]\n")
    #         print(event)
        
    async for event in result.stream_events():
        # if event.type == 'raw_response_event':
            print("\n[EVENT]\n")
            print(event)

asyncio.run(main())