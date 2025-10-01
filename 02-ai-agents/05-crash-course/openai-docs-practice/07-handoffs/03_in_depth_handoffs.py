from agents import Agent, Runner, RunResult, enable_verbose_stdout_logging, RunConfig, set_default_openai_api, function_tool, handoff
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv
import asyncio
from rich import print
from agents.extensions import handoff_filters

load_dotenv()
enable_verbose_stdout_logging()
# set_default_openai_api("chat_completions")


marketing_agent = Agent(
    name="Marketing Agent",
    instructions="You are an expert in marketing, and telling marketing campaigns and strategies for buinesses.",
    model="gpt-4o-mini",
    handoff_description="handle all tasks related to marketing, branding, brand campaning."
)

@function_tool
def get_price():
    print("Price is x")

@function_tool
def get_lead():
    print("10000 leads recieved")

sales_agent = Agent(
    name="Sales Agent",
    instructions="You are an expert in sales, and building sales funnels and leads for buinesses.",
    model="gpt-4o-mini",
    handoff_description="handle all tasks related to sales, lead gen, client hunting.",
    tools=[get_price,get_lead]
)

agent = Agent(
    name="Triage Agent",
    instructions="You are a triage agent you have 2 sub agents 1- Marketing Agent, 2- Sales Agent. Give them tasks that are related to their queries.",
    model="gpt-4o-mini",
    handoffs=[
        handoff(agent=marketing_agent, tool_name_override="Maketing_Waala_Mama"),
        handoff(agent=sales_agent,
                tool_name_override="Sales_Wala_Shapaatar",
                tool_description_override="This is for sales purposes!",
                input_filter=handoff_filters.remove_all_tools),
        ]
)

# print("[yellow]agent.handoffs")
# print(agent.handoffs)
print("[yellow]sales_agent")
print(sales_agent)

print("[yellow]agent")
print(agent)

async def main() -> RunResult:

    result = await Runner.run(
        starting_agent=agent, 
        input="I need to master B2B sales.",
    )

    # print(result.final_output)
    # print(result)
    return result

asyncio.run(main())