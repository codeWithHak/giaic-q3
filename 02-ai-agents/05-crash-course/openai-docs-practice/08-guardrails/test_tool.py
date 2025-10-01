from agents import Agent, Runner, enable_verbose_stdout_logging, GuardrailFunctionOutput, input_guardrail,InputGuardrailTripwireTriggered, set_default_openai_api, function_tool
from dotenv import load_dotenv
import asyncio
from rich import print
from pydantic import BaseModel

enable_verbose_stdout_logging()
load_dotenv()
set_default_openai_api("chat_completions")


@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is Karachi."

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[get_weather]
)

async def main():
    result = await Runner.run(starting_agent=agent, input="what's the weather in Karachi")
    print(result.final_output)

asyncio.run(main())