from agents import Agent, Runner, enable_verbose_stdout_logging, GuardrailFunctionOutput, input_guardrail,InputGuardrailTripwireTriggered, set_default_openai_api
from dotenv import load_dotenv
import asyncio
from rich import print
from pydantic import BaseModel
enable_verbose_stdout_logging()

load_dotenv()
set_default_openai_api("chat_completions")

class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning:str
    

input_guardrail_agent = Agent(
    name="input guardrail agent",
    instructions="Check if the user asked a question about maths.",
    model="gpt-4o-mini",
    output_type=MathHomeworkOutput
)

@input_guardrail
async def math_guardrails(ctx, agent, input_to_guardrail) -> GuardrailFunctionOutput:

    print("\n[AGENT]")    
    print(agent)    
    print("\n[input_to_guardrail]".upper())    
    print(input_to_guardrail)    
    print("\n[CTX]")    
    print(ctx)    
    print("\n[CTX.CPNTEXT]")    
    print(ctx.context)    
    print("\n[input_guardrail]".upper())    
    print(input_guardrail)    
    print("\n[math_guardrails]".upper())    
    print(math_guardrails)   
    print("\n[orange]GuardrailFunctionOutput")   
    print(GuardrailFunctionOutput)   
   

    result = await Runner.run(input_guardrail_agent, input_to_guardrail, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info = result.final_output.reasoning,
        tripwire_triggered = result.final_output.is_math_homework
    )

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gpt-4o-mini",
    input_guardrails=[math_guardrails]
)

async def main():
    print("\n")
    try:
        result = await Runner.run(starting_agent=agent, input="what is motion")
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print("[red] Tripped baway")

asyncio.run(main())