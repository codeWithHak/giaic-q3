from agents import Agent, Runner, enable_verbose_stdout_logging, set_default_openai_api
from dotenv import load_dotenv
import os
from rich import print

enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
)

result = Runner.run_sync(starting_agent=agent, input="Hello")
print(result.final_output)