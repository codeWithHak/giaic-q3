from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a great an old programmer with 20 years of experience.",
    model="gpt-4o-mini"
)

result = Runner.run_sync(
    starting_agent=agent,
    input="Hello world"
)

print(result.final_output)
