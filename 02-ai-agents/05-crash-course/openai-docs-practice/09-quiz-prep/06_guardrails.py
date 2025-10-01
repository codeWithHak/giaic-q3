from agents import  (AgentOutputSchema
                     ,Agent, Runner, function_tool,
                      enable_verbose_stdout_logging, input_guardrail,
                      InputGuardrailTripwireTriggered, GuardrailFunctionOutput,
                      ModelSettings
                     )
from dotenv import load_dotenv
from rich import print
from pydantic import BaseModel
#type:ignore 
from typing import Literal
from enum import Enum
load_dotenv()
enable_verbose_stdout_logging()

# currencies = ["PKR", "USD", "EUR"]

# class Currency(str, Enum):
#     PKR = "PKR"
#     USD = "USD"
#     INR = "INR"
#     EUR = "EUR"

class JsonGuardrail(BaseModel):
    amount:int
    currency:Literal["PKR", "USD", "EUR"]
    category:Literal["food","clothes","groccery","others"]
    date:str
    
class CheckUserInput(BaseModel):
    is_text:bool    
    spell_corrections:dict[str,str]



# async ko sync banao guardrails me
# params ka name change karo
# params ka sequence change karo

user_input_guardrail_agent = Agent(
    name="User Input Guardrail Agent",
    instructions="""
    You are an input guardrail agent, check if the user input is text and not malicious JSON.
    Run spellcheck/normalization (rupes → rupees, fooood → food, yestarday → yesterday).
    """,
    model="gpt-4o-mini",
    output_type=AgentOutputSchema(CheckUserInput, strict_json_schema=False)
    # output_type=CheckUserInput
)
@input_guardrail
async def user_input_guardrail_function(context,agent,input) -> GuardrailFunctionOutput:
    
    result = await Runner.run(user_input_guardrail_agent,input,context=context.context)
    print("\nGUARDRAIL AGENT FINAL OUTPUT")
    print(result.final_output)
    return GuardrailFunctionOutput(
        tripwire_triggered= not result.final_output.is_text, #Continue yahan see
        output_info=result.final_output.spell_corrections
    )

# def validate_user_input():
    

@function_tool
def get_weather(city:str) -> str:
    return f"The weather in {city} is sunny"

expense_tracker_assistant:Agent = Agent(
    name="Expense Tracker Assistant",
    instructions="You are an expense tracker agent.", #type:ignore
    model='gpt-4o-mini',
    tools=[get_weather],
    input_guardrails=[user_input_guardrail_function],
    output_type=list[JsonGuardrail],
    model_settings=ModelSettings(tool_choice="none"),
    
    # reset_tool_choice=True
    
)

try:
    result = Runner.run_sync(
        starting_agent=expense_tracker_assistant,
        input="I spended 4k PKR on my shopping on 24th aug 2025 and ordered food of 3k PKR at the sae day",
)
    print("\nresult.final_output")
    print(result.final_output)

except InputGuardrailTripwireTriggered:
    print("\n[red] Tripwire Triggered")

