from agents import Agent, Runner,enable_verbose_stdout_logging, trace, function_tool, RunContextWrapper
from agents.tracing import util
from dotenv import load_dotenv
from rich import print
from dataclasses import dataclass


load_dotenv()

enable_verbose_stdout_logging()

@dataclass
class UserInfo:
    user_name:str
    user_age:int

@function_tool
def fethc_user_age(ctx:RunContextWrapper[UserInfo]):
    return f"The user is {ctx.context.user_age} years old."

affan = UserInfo(user_name="Affan",user_age=19)

agent = Agent(
    name="assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    tools=[fethc_user_age]
)


result = Runner.run_sync(starting_agent=agent, input="How old is affan", context=affan)

print("result:",result.final_output)