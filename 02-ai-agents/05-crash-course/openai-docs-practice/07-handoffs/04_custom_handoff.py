from agents import Agent, Runner, RunResult, enable_verbose_stdout_logging, RunConfig, set_default_openai_api, function_tool, handoff, Handoff, RunContextWrapper
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv
import asyncio
from rich import print
from agents.extensions import handoff_filters

load_dotenv()
enable_verbose_stdout_logging()


# 1- Marketing Agent
marketing_agent = Agent(
    name="Marketing Agent",
    instructions="You are an expert in marketing, and telling marketing campaigns and strategies for buinesses.",
    model="gpt-4o-mini",
    handoff_description="handle all tasks related to marketing, branding, brand campaning."
)

# 2- Sales Agent
sales_agent = Agent(
    name="Sales Agent",
    instructions="You are an expert in sales, and building sales funnels and leads for buinesses.",
    model="gpt-4o-mini",
    handoff_description="handle all tasks related to sales, lead gen, client hunting.",
)

# Function that returns an Agent
async def invoke_sales_agent(ctx:RunContextWrapper, input_json:str) -> Agent:
    print("[red]\ninput_json INSIDE HANDOFF CUSTOM FUNCTION")
    print(input_json)
    return sales_agent

# Custom Handoff Object
sales_agent_custom = Handoff(
    agent_name="Sales Agent",
    tool_description="handles all the slaes related tasks",
    tool_name="Shapataer_Salesman",
    on_invoke_handoff=invoke_sales_agent,
    input_json_schema={'additionalProperties': False, 'type': 'object', 'properties': {}, 'required': []},
)

# Triage Agent
agent = Agent(
    name="Triage Agent",
    instructions="You are a triage agent you have 2 sub agents 1- Marketing Agent, 2- Sales Agent. Give them tasks that are related to their queries.",
    model="gpt-4o-mini",
    handoffs=[sales_agent_custom]
)

async def main() -> RunResult:

    result = await Runner.run(
        starting_agent=agent, 
        input="I need to master B2B sales.",
    )

    # print(result.final_output)
    # print(result)
    return result

asyncio.run(main())