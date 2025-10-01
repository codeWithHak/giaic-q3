from agents import Agent, Runner, RunResult, enable_verbose_stdout_logging, RunConfig, set_default_openai_api, ModelSettings, function_tool, RunContextWrapper
from dotenv import load_dotenv
import asyncio
from rich import print
from pydantic import BaseModel
import time
import logging

logger = logging.getLogger(__name__)

load_dotenv()
enable_verbose_stdout_logging()
set_default_openai_api("chat_completions")


#! Issue is when you pass context as string it only takes the first word as context not the whole string
#! Like in our case we passes context "name:huzair, age:20, gender:male" but only got "name" in our context
#  
#* 01- Basic Context
context = "name:huzair, age:20, gender:male"

# * 02- Advanced Context
class MyInformation(BaseModel):
    name:str
    age:int
    gender:str



#* 02- Advanced Context
@function_tool
def access_context(context:RunContextWrapper[MyInformation]) -> MyInformation:
    print("[red]TEST",flush=True)
    print("\ncontext",flush=True)
    print(context,flush=True)
    print("\ncontext.context.model_config",flush=True)
    print(context.context.model_config,flush=True)
    print(context,flush=True)


    return context.context


async def say_hello():
    print("[yellow]\n How are you Huzair")
    print("[yellow]\n How are you Huzair")
    print("[yellow]\n How are you Huzair")

print("\n[blue] Outsite Tool")
print("\naccess_context.description")
print(access_context.description)
print("\naccess_context")
print(access_context)
print("[blue]\naccess_context.on_invoke_tool")
# print(access_context.on_invoke_tool(say_hello))


#* 01- Basic Context
# @function_tool
# def access_context(context:RunContextWrapper[str]) -> str:
#     print("\ncontext")
#     print(context)
#     print("\ncontext.context")
#     print(context.context)
#     return context.context


# @function_tool
# def access_context(context):
#     print("\ncontext")
#     print(context)
#     print("\ncontext.context")
#     print(context.context)
#     return context.context

my_rag_agent = Agent(
    name="My Rag Agent",
    instructions="Kindly provide all the info about me",
    model='gpt-4o-mini',
    tools=[access_context]
)

#* 02- Advanced Context
# context = MyInformation(name="Huzair", age=20, gender="Male")



result = Runner.run_sync(
    starting_agent=my_rag_agent,
    input="What is my name",
    context=context
)

print(result.final_output)