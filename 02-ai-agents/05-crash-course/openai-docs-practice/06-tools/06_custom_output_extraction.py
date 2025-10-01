from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool,ToolCallOutputItem, RunResult
import os
import asyncio
from rich import print
from dotenv import load_dotenv
enable_verbose_stdout_logging()

load_dotenv()



def get_weather(city:str) -> str:
    return f"Weather in {city} is sunny!"


weather_agent = Agent(
    name="Weather Agent",
    instructions="Return weather in a json structure", 
    model="gpt-4o-mini"
)


async def extract_json_payload(run_result: RunResult) -> str:
    # Scan the agent’s outputs in reverse order until we find a JSON-like message from a tool call.
    for item in reversed(run_result.new_items):
        if isinstance(item, ToolCallOutputItem) and item.output.strip().startswith("{"):
            return item.output.strip()
    # Fallback to an empty JSON object if nothing was found
    return "{}"


json_tool = weather_agent.as_tool(
    tool_name="get_data_json",
    tool_description="Run the data agent and return only its JSON payload",
    custom_output_extractor=extract_json_payload,
)



agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[json_tool]
)


async def main():
    result = await Runner.run(starting_agent=agent, input="What's the weather in hyderabad.")
    print(result.final_output)

asyncio.run(main())