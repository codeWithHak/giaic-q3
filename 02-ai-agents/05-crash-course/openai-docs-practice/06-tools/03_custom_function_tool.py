from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool, FunctionTool
from agents.function_schema import function_schema
# from agents.
import os
import asyncio
from rich import print
from dotenv import load_dotenv
enable_verbose_stdout_logging()

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# @function_tool
def get_weather(city:str="KARACHI") -> str:

    """Fetch and return weather for a particular city
    Args: city(str)
    returns: weather of that city
    """

    print("\n[function_tool]\n")
    print(function_tool)
    
    print("\n[get_weather]\n")
    print(get_weather)

    return f"Weather in {city} is sunny!"


schema = function_schema(get_weather)
print("\n[schema]\n")
print(schema)

schema.name = "Hacked"
schema.params_json_schema["required"] = []

print("\n[New Schema]\n")
print(schema)

# get_weather = FunctionTool(
#     name="get_weather",
#     description=""
# )

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    # tools=[schema]
)

async def main():
    print("\n")
    result = await Runner.run(starting_agent=agent, input="What's the weather in karachi")
    print(result.final_output)

asyncio.run(main())