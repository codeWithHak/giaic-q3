from agents import (
    Agent,
    Runner,
    OutputGuardrailTripwireTriggered,
    output_guardrail,
    GuardrailFunctionOutput,
    set_default_openai_api,
    enable_verbose_stdout_logging, #type:ignore
)

from pydantic import BaseModel
from dotenv import load_dotenv
enable_verbose_stdout_logging()

load_dotenv()

class MathGuardrail(BaseModel):
    reasoning:str
    is_math:bool


guardrail_agent = Agent(
    name="Guardrail",
    instructions="Check if output includes any math.",
    model="gpt-4o-mini",
    output_type=MathGuardrail
) 

@output_guardrail
async def output_behaviour_guardrail(ctx, agent, output) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output, context=ctx.context) # context=ctx.context hata kar dekho sirf ctx laga kar dekho context = ctx karke dekho 
    
    return GuardrailFunctionOutput(
        output_info=result.final_output.reasoning,
        tripwire_triggered=result.final_output.is_math
    )

agent = Agent(
    name="Helpful Assitant",
    instructions="you are a helpful assistant",
    model="gpt-4o-mini",
    output_guardrails=[output_behaviour_guardrail]
)
try:
    user_input = input("Ask me anything: ")
    result = Runner.run_sync(agent, user_input)
    print(result.final_output)
    result = Runner.run_sync(guardrail_agent, user_input)
    print(result.final_output.is_math)
    print(result.final_output.reasoning)
except OutputGuardrailTripwireTriggered:
    print("Output Guardrail Triggered")