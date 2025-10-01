from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

load_dotenv()

@function_tool
def weather(city:str) ->str:
    return f"The weather in {city} is sunny"

agent = Agent(
    name='Helpful Assistant',
    instructions='You are a helpful assistant',
    model='gpt-4o-mini',
    tools=[weather]
)

result = Runner.run_sync(
    starting_agent=agent,
    input="What's the weather in paris"
)

print(result.final_output)