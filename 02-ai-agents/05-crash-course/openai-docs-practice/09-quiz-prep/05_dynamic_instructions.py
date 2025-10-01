from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from dotenv import load_dotenv
from rich import print

#type:ignore 

load_dotenv()
enable_verbose_stdout_logging()

@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is sunny"

def dynamic_instructions(ctx,agent) -> str:
    return "You are a cheetah developer, who is expert in python programming."

agent:Agent = Agent(
    name="Assistant",
    instructions=dynamic_instructions, #type:ignore
    model='gpt-4o-mini',
    tools=[get_weather],
    
)

result = Runner.run_sync(
    starting_agent=agent,
    input="What's the weather in karachi",
    # max_turns=,
)

print(dynamic_instructions)
print(agent.instructions)
print(agent)
