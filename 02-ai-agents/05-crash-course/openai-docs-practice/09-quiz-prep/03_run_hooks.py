from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, RunHooks, RunContextWrapper, TContext, TResponseInputItem
from agents.lifecycle import TAgent
from agents.exceptions import MaxTurnsExceeded
from dotenv import load_dotenv
from rich import print

load_dotenv()
enable_verbose_stdout_logging()

@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is sunny"


@function_tool
def internet_speed_query_handler() -> str:
    return f"The internet speed is slow because shark ne taar khaali"

 
 
class Hook(RunHooks):
    total_agents_used:int = 0
    total_turns:int = 0
    total_tool_calls:int = 0

    async def on_agent_start(self,context:RunContextWrapper[TContext],agent:TAgent):
        print(f"[blue]AGENT {agent.name} STARTED")
        Hook.total_agents_used += 1
        # print(agent_start_count)
    
    async def on_agent_end(self,context,agent,output):
        print(f'[blue]AGENT {agent.name} ENDED WITH OUTPUT: {output}')
    
    async def on_llm_start(self, context, agent, system_prompt, input_items):
        print(f'[blue]CALLING LLM WITH: {input_items}')
        # print(f"[blue] TURN NO. {Hook.total_turns}")
        # print("\n[blue]SELF")
        # print(self)
        # print("\n[blue]AGENT")
        # print(agent)
        # print("\n[blue]CONTEXT")
        # print(context)
        # print("\n[blue]SYSTEM PROMPT")
        # print(system_prompt)
        # print("\n[blue]INPUT ITEMS")
        # print(input_items)
        Hook.total_turns += 1      
    
    
    async def on_llm_end(self,ctx,agent,response): 
        print(f"\n[green]GOT LLM'S RESPONSE: {response}")
        
    async def on_tool_start(self, ctx, agent, tool):
        print(f'\n[cyan]{tool.name} TOOL INVOKED')
        Hook.total_tool_calls+=1
        
    async def on_tool_end(self,context,agent,tool,result):
        print("[blue]GOT TOOL RESPONSE")
        print("[cyan]TOOL RESULT")
        print(result)
        
    async def on_handoff(self,context, from_agent, to_agent):
        print(f'[blue]HANDED OFF TO {to_agent.name} FROM {from_agent.name}')
        # print(source)
        


  
customer_support_agent = Agent(
    name="Customer Support Agent",
    instructions="You are a Customer Support Agent handle all the queries related to customer support!",
    model="gpt-4o-mini",
    # hooks=Hook(),
    tools=[get_weather, internet_speed_query_handler]
)  


        

agent = Agent(
    name="Assistant",
    instructions='You are a helpful assistant',
    model='gpt-4o-mini',
    # tools=[get_weather],
    # tool_use_behavior="stop_on_first_tool",
    # reset_tool_choice=False,
    # hooks=Hook(),
    handoffs=[customer_support_agent]
    
)
try:
    result = Runner.run_sync(
        starting_agent=agent,
        input="Why my internet speed is slow?, and want to know the current weather of karnatika",
        # max_turns=,
        hooks=Hook()
    )
    # print("\n[cyan]result")
    print("[cyan]result.final_output")
    print("\n",result.final_output)
    print(f"[blue]TOTAL AGENTS:{Hook.total_agents_used}")
    print(f"[blue]TOTAL TURNS:{Hook.total_turns}")
    print(f"[blue]TOTAL TOOLS:{Hook.total_tool_calls}")
    
    
except MaxTurnsExceeded:
    print("[red]Max Turns Exceeded.")


