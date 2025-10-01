from agents import Agent, Runner, RunConfig
from rich import print
import asyncio
from dotenv import load_dotenv

load_dotenv()


agent = Agent(name="Assistant", instructions="You are a helpful assistant, you are chill, very polite and fun loving, you are a teenager who usees genz slang.")

run_config = RunConfig(
    model="gpt-4o-mini"
)

# user_input = input("Give me an input: ")

async def main():
    
    
    while True:
        print('\n[START OF LOOP]\n')
        user_input= input("Ask me anything: ")
        result = await Runner.run(agent,input=user_input, run_config=run_config)
        print('\n[FIRST RESULT]\n')
        print(result.final_output)

        new_input = result.to_input_list() + [{"role":"user", "content":user_input}]
        print('\n[NEW INPUT]\n')
        print(new_input)
        
        second_result = await Runner.run(agent,new_input, run_config=run_config)
        print('\n[SECOND RESULT]\n')
        print(second_result.final_output)
asyncio.run(main())
    
    