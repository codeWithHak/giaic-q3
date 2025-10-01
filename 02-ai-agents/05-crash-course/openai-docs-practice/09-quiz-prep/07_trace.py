from agents import Agent, Runner, enable_verbose_stdout_logging, trace
from dotenv import load_dotenv
from rich import print
from pydantic import BaseModel
#type:ignore 
load_dotenv()
enable_verbose_stdout_logging()


agent = Agent(
    name="Assistant",
    instructions='You are a helpful assistant',
    model='gpt-4o-mini',
)
    

with trace ("First Workflow"):
    
    result = Runner.run_sync(
        starting_agent=agent,
        input="How many a's are in apple?"
    )
    print("\nresult.final_output")
    print(result.final_output)
    
    new_result = Runner.run_sync(
        starting_agent=agent,
        input=f"{result.final_output} and how many p's?"
    )
    print("\nnew_result.input")
    print(new_result.input)

    print("\nnew_result.final_output")
    print(new_result.final_output)

print("\n[bright_red]------------------- NEW WORKFLOW --------------------------")

with trace ("Second Workflow"):
    
    result = Runner.run_sync(
        starting_agent=agent,
        input="How many a's are in apple?"
    )
    print("\nresult.final_output")
    print(result.final_output)
    
    new_result = Runner.run_sync(
        starting_agent=agent,
        input=f"{result.final_output} and how many p's?"
    )
    print("\nnew_result.input")
    print(new_result.input)

    print("\nnew_result.final_output")
    print(new_result.final_output)