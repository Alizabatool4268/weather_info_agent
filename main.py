import os
from agents import Runner, OpenAIChatCompletionsModel, set_tracing_disabled,Agent
from openai import AsyncOpenAI
from dotenv import load_dotenv
from my_tools.tools import weather_tool

load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
my_base_url =os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key= my_key,
    base_url= my_base_url
)    
MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client,
)

weather_assistant= Agent(
    name="Allie",
    model= MODEL,
    instructions="your name is allie. You are a helpful agent which will help users about weather. dont answer questions if they are not related to weather you can answer if the user asks your name only. ",
    tools=[weather_tool]
    
)
prompt = input("what is your question: ")

set_tracing_disabled(True)
result = Runner.run_sync(
    starting_agent= weather_assistant,
    input = prompt
)
print(result.final_output)