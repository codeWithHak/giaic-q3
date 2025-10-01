from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool, FunctionTool
import os
import asyncio
from rich import print
from dotenv import load_dotenv
import json
enable_verbose_stdout_logging()

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@function_tool
def get_weather(city:str) -> str:
    return f"Weather in {city} is sunny!"


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[get_weather]
)

get_changed = [tool.name for tool in agent.tools]

async def main():
    print("\n")
    result = await Runner.run(starting_agent=agent, input="What's the weather in paris")
    print(result.final_output)
    print("\nresult")
    print(result)

for tool in agent.tools:
    print("\ntool")
    print(tool.name)
    # tool.name= "get_changed"
    # print(tool.name)
    # print(tool.description)
    # print(json.dumps(tool.params_json_schema, indent=2))

asyncio.run(main())