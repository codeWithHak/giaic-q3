from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from agents.exceptions import MaxTurnsExceeded
from dotenv import load_dotenv
from rich import print

#type:ignore 

load_dotenv()
enable_verbose_stdout_logging()

@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is sunny"


agent = Agent(
    name="Assistant",
    instructions='You are a helpful assistant', #type:ignore
    model='gpt-4o-mini',
    tools=[get_weather],
    # tool_use_behavior="stop_on_first_tool",
    reset_tool_choice=False
    
)
try:
    result = Runner.run_sync(
        starting_agent=agent,
        input="What's the weather in karachi",
        # max_turns=,
    )
    print(result)
    print("\n\n",result.final_output)
    
except MaxTurnsExceeded:
    print("[red]Max Turns Exceeded.")


#* If you use max_turns = 1 and use a tool it will definitely throw the MaxTurnsExceeded exception.
#* But if you use too_use_behaviour = "stop_on_first_tool" the tool will return the output by itself.
