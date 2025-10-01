from agents import Agent, Runner, enable_verbose_stdout_logging, set_default_openai_api, RunResult, RunContextWrapper, handoff, function_tool, ModelSettings
from dotenv import load_dotenv
import os
import asyncio
from rich import print

enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@function_tool
def get_weather(city:str) -> str:
    return f"the weather in {city} is sunny."

detective = Agent(
    name="Detective Holmes",
    instructions="You are a detective",
    model="gpt-4o-mini",
    handoff_description="handoff to this agent if task is related to detetive or investigation related."

)
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    handoffs=[handoff(agent=detective,tool_name_override="detective_holmes",tool_description_override="An agent that is a detective and handle all investigation related queries")],
    tools=[get_weather],
    model_settings=ModelSettings(parallel_tool_calls=False)
)

#returs a RunResultStreamingObject
async def main():
    result = Runner.run(starting_agent=agent, input="Hello, i've got a murder case for you to solve? are you shaana enoguh meri jaaan? Geooo, and what's the weather in karachi")
    print("\n")
    print(await result)

# test= RunResult(input="lala", new_items=[],raw_responses=[],context_wrapper=RunContextWrapper(context=None),final_output="Final output yeahhh",input_guardrail_results=[],output_guardrail_results=[],_last_agent=agent)
# print("\n[TEST]\n")
# print(test)
# print("\n")


asyncio.run(main())