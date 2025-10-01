from agents import Agent, Runner, enable_verbose_stdout_logging, set_default_openai_api
from dotenv import load_dotenv
import os
import asyncio
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

# returns a RunResult Object
# print("\n")
# result = Runner.run_sync(starting_agent=agent, input="Hello which llm e.g(gemini) and model e.g(gemini-2.5-flash) is this")
# print(result)
# print("\n")


#returs a RunResultStreamingObject
async def main():
    
    # create an empty history
    history = []
    
    # run a loop
    while True:
        
        # take the user's input
        user_input = input("Ask me anything: ")

        # if history is empty, then current input will be user's input means it's the first input.
        if not history:
            current_input = user_input

        # if the history has inputs so we need to append in those inputs.
        else:
            current_input = history + [{"role":"user", "content":user_input}]

        # run the agent
        result = await Runner.run(starting_agent=agent, input=current_input)

        # add previous history to history varaible
        history = result.to_input_list()


        print('\n\n[DIR(RESULT)]\n\n')
        print(dir(result))

        print('\n\n[RESULT.NEW_ITEMS]\n\n')
        print(result.new_items)

        print('\n\n[RESULT.NEW_ITEMS[0].raw_item]\n\n')
        print(dict(result.new_items[0].raw_item))
        
        items = []

        for item in result.new_items[0].raw_item:
            items.append(item)
            print('\n\n[ITEMS LOOP]')
            print(items)
        print('\n\n[ITEMS]')

        print('\n\n[RESULT.INPUT]\n\n')
        print(result.input)

        print("\nAssistant:", result.final_output)
        print("\nHistory:", history)

asyncio.run(main())