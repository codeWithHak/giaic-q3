from agents import (
    Agent,
    Runner,
    InputGuardrailTripwireTriggered,
    input_guardrail,
    GuardrailFunctionOutput,
    set_default_openai_api,
    enable_verbose_stdout_logging, #type:ignore
    RunContextWrapper,
    TResponseInputItem
)

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class RudeBehaviourGuardrail(BaseModel):
    reasoning:str
    is_rude_behaviour:bool


user_rude_behaviuor_checking_agent = Agent(
    name="User Rude Behaviour Checking Agent",
    instructions="You are a guardrail agent that checks if user is talking or querying in rude tone or is angry.",
    model="gpt-4o-mini",
    output_type=RudeBehaviourGuardrail
) 

@input_guardrail
async def input_behaviour_guardrail(ctx:RunContextWrapper, agent:Agent, input:str) -> GuardrailFunctionOutput:
    result = await Runner.run(user_rude_behaviuor_checking_agent, input, context=ctx.context) # context=ctx.context hata kar dekho sirf ctx laga kar dekho context = ctx karke dekho 
    
    return GuardrailFunctionOutput(
        output_info=result.final_output.reasoning,
        tripwire_triggered=result.final_output.is_rude_behaviour
    )

agent = Agent(
    name="Helpful Assitant",
    instructions="you are a helpful assistant",
    model="gpt-4o-mini",
    input_guardrails=[input_behaviour_guardrail]
)
try:
    user_input = input("Ask me anything: ")
    result = Runner.run_sync(agent, user_input)
    print(result.final_output)
except InputGuardrailTripwireTriggered:
    print("Input Guardrail Triggered")