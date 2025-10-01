from agents import Agent, Runner, enable_verbose_stdout_logging
from dotenv import load_dotenv
from rich import print
import asyncio

#type:ignore 
load_dotenv()
enable_verbose_stdout_logging()


agent = Agent(
    name="Assistant",
    instructions='You are a helpful assistant',
    model='gpt-4o-mini',
)
    
async def main():    
    result = Runner.run_streamed(
        starting_agent=agent,
        input="How many a's are in apple?"
    )
    print(result)
    print("\nresult.final_output")
    print(result.final_output)
    
    
    
asyncio.run(main()) 