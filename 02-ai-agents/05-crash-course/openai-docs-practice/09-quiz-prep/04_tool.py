from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from dotenv import load_dotenv
from rich import print

#type:ignore 

load_dotenv()
enable_verbose_stdout_logging()

@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is sunny"


agent:Agent = Agent(
    name="Assistant",
    instructions='You are a helpful assistant', #type:ignore
    model='gpt-4o-mini',
    tools=[get_weather],
)

print("\n[white]agent.tools")
print(agent.tools)

print("\n[white]agent")
print(agent)
print("\n[white]Agent(name=1)")

try:
    print(Agent(name=1)) #type:ignore
except TypeError as e:
    print(" TypeError str", str(e))

    
print("\n[white]Agent(name='test agent')")
print(Agent(name="test agent"))
result = Runner.run_sync(
    starting_agent=agent,
    input="What's the weather in karachi",
    # max_turns=,
)


#* If you use max_turns = 1 and use a tool it will definitely throw the MaxTurnsExceeded exception.
#* But if you use too_use_behaviour = "stop_on_first_tool" the tool will return the output by itself.
