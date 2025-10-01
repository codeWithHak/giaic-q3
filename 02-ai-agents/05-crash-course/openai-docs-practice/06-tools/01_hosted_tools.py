from agents import Agent, Runner, enable_verbose_stdout_logging, WebSearchTool, FileSearchTool, ComputerTool, Computer
from dotenv import load_dotenv
import os
import asyncio
from rich import print

enable_verbose_stdout_logging()
# set_default_openai_api("chat_completions")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",

    # tools=[WebSearchTool()] - works on gpt-4o-mini

    # tools=[FileSearchTool(
    #     vector_store_ids=["vs_68a338f8513c81919e4d202f66445af4"],
    #     max_num_results=3
    #     )]

)

async def main():
    print("\n")
    
    # Runner for testing WebSearchTool
    # result = await Runner.run(starting_agent=agent, input="I need the link of Huzair Ahmed Khan's LinkedIn. Also search and see what is his LinkedIn headline!")

    result = await Runner.run(starting_agent=agent, input="Create a folder on the desktop named Agent_Created_Folder")
    print(result.final_output)

asyncio.run(main())