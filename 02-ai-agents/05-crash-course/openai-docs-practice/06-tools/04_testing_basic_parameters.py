from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool, RunContextWrapper
import os
import asyncio
from rich import print
from dotenv import load_dotenv
enable_verbose_stdout_logging()

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_weather(city:str) -> str:
    return f"Weather in {city} is sunny!"



# failure_error_function
def error_func(ctx:RunContextWrapper, err:Exception):
    print("An very very khatarnak error occured:", err)
    return "Internal server error he, kal aana."

# function_tool to demonstrate failure_error_function
@function_tool(failure_error_function=error_func)
def get_user_info(id:int):
    "Gets id of user and matchit with stored id."
    if id == 123:
        return "User matched"
    else:
        raise ValueError(f"Could not find user with id {id}.")


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[function_tool(func=get_weather, name_override="get_paris_weather", strict_mode=False,failure_error_function=error_func)]
    # tools=[get_user_info]
)

async def main():
    print("\n")
    result = await Runner.run(starting_agent=agent, input="hello id is 222")
    print(result.final_output)

asyncio.run(main())