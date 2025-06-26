from decouple import config
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel,Runner
import asyncio

my_key= config("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = my_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

math_teacher = Agent(
    name="liza",
    instructions="You are a math teacher,you solve complex math problems your name is liza and give detail answers",
    model=MODEL
)

async def main ():
    result = await Runner.run(math_teacher,"what is 20+200?")
    print(result.final_output)
    
asyncio.run(main())    
