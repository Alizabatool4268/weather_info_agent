from agents import FunctionTool,RunContextWrapper
import requests
import os
from dotenv import load_dotenv



load_dotenv(override=True)
weather_api= os.getenv("WEATHER_API")

async def get_weather_func(ctx:RunContextWrapper,city: str):
    response = requests.get("http://api.weatherapi.com/v1/current.json", 
                            params={"key":weather_api, "q": city})
    data = response.json()
    return {
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }


weather_tool = FunctionTool(
    name= "get_weather",
    description="Fetches the current weather for a given city",
    on_invoke_tool= get_weather_func,
    params_json_schema={
        "type": "object",
        "properties": {
            "city": {
                "type": "string", 
                "description": "Name of the city "
            }
        },
        "required": ["city"]
    },
    is_enabled=True
)
