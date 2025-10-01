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
@function_tool
def fetch_user_profile(user_id: int) -> dict:
    """
    Fetch user profile from DB.
    Returns structured data for both success and error cases.
    """
    try:
        # Pretend DB lookup
        if user_id != 123:
            raise ValueError("User not found in DB")

        return {
            "status": "success",
            "data": {
                "user_id": user_id,
                "name": "Alice",
                "email": "alice@example.com"
            }
        }
    except Exception as e:
        # Instead of failing, return structured error
        print("\n")
        print("type(e).__name__")
        print(type(e).__name__)
        print("\n")
        print("str(e)")
        print(str(e))
        print("\n")
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "message": str(e)
        }


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[fetch_user_profile]
)

async def main():
    print("\n")
    result = await Runner.run(starting_agent=agent, input="hello id is 121")
    print(result.final_output)

asyncio.run(main())