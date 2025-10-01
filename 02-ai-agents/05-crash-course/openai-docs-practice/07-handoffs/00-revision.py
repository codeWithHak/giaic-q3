from agents import Agent, Runner, RunResult, enable_verbose_stdout_logging, RunConfig, set_default_openai_api, ModelSettings, function_tool, handoff
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv
import asyncio
from rich import print
from agents.extensions import handoff_filters

load_dotenv()
# enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")

#* TRY HANDOFFS
# data = """Daewoo Coach is going from karachi to lahore it is taking 3000 for one ticket if passenger is an adult,
# if an old man above 60 then it takes 1500 and if a child below 8 it also takes 1500, there is capacity if 45 passengers, 20 ladies and 25 gents, route goes from pindi islamabad and pattoki,
# or gaari chohtay me gum rahegi and it has poyo oil filled.
# """

# @function_tool
# def get_weather(city:str) -> str:
#     return f"The weather in {city} is sunny"

# driver_agent:Agent = Agent(
#     name="Driver Agent",
#     instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are a bus driver, your task is to drive the bus and tell the passengers about route if they ask.", 
# )

# luggage_carrying_agent:Agent = Agent(
#     name="Luggage Carrier",
#     instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are responsible for carrying luggage of all the passengers."
# )

# ticket_collector_agent = Agent(
#     name="Ticket Collector",
#     instructions=f"{RECOMMENDED_PROMPT_PREFIX} You are responsible for checking tickets and verifying that all the passengers are traveling legally."

# )

# triage_agent:Agent = Agent(
#     name="Triage Agent",
#     instructions="Your job is to handoff the task to other agents based on their specific roles.",
#     handoffs=[handoff(agent=driver_agent, input_filter=handoff_filters.remove_all_tools()),handoff(agent=luggage_carrying_agent),handoff(agent=ticket_collector_agent)],
#     tools=[get_weather],
# )

# run_config = RunConfig(
#     model="gpt-4o-mini",
#     model_settings=ModelSettings()
# )

# async def main() -> RunResult:
#     result = await Runner.run(
#         starting_agent=triage_agent, 
#         input="Tell me the detailed pricing of Daewoo express",
#         run_config=run_config,
#         context=data
#     )
#     print(result.final_output)
#     # print(result)
#     return result


agent = Agent(
    name="Assistant",
    instructions="You area helpful assistant",
    model="gpt-4o-mini"
)

async def main() -> RunResult:
    result = await Runner.run(
        starting_agent=agent, 
        input="Hello world",
    )
    print(result.final_output)
    # print(result)
    return result

asyncio.run(main())